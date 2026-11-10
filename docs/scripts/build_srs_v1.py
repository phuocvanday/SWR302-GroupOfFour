# -*- coding: utf-8 -*-
"""Assemble 01_SRS_GMS.docx from docs/step* team drafts. Run from repo root."""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "03_Images"
OUT = ROOT / "01_SRS_GMS.docx"


def set_doc_defaults(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii", "Times New Roman")
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi", "Times New Roman")


def add_heading(doc, text, level=1):
    return doc.add_heading(text, level=level)


def add_p(doc, text="", bold=False, italic=False, size=12):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.name = "Times New Roman"
    return p


def add_note(doc, text):
    p = doc.add_paragraph()
    run = p.add_run("[MISSING / TODO] " + text)
    run.bold = True
    run.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)
    run.font.size = Pt(11)
    run.font.name = "Times New Roman"
    return p


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            table.rows[r_i + 1].cells[c_i].text = str(val) if val is not None else ""
    doc.add_paragraph()
    return table


def try_picture(doc, path: Path, width=5.8, caption=None):
    if path.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))
        if caption:
            cap = doc.add_paragraph(caption)
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return True
    add_note(doc, f"Image not found: {path.relative_to(ROOT)}")
    return False


def parse_md_field_table(path: Path) -> list[tuple[str, str]]:
    """Parse | Field | Content | tables from UC-05 style docs."""
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(parts) < 2:
            continue
        if parts[0].lower() in {"field", "item", "---"} or set(parts[0]) <= {"-", ":"}:
            continue
        if parts[0].startswith("---") or parts[1].startswith("---"):
            continue
        # skip summary headers like "Use case ID" in alternate templates handled below
        key = re.sub(r"\*+", "", parts[0]).strip()
        val = parts[1]
        if key and val and key.lower() not in {"uc", "screen", "png file"}:
            rows.append((key, val))
    return rows


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def build():
    doc = Document()
    set_doc_defaults(doc)

    # ===== COVER =====
    for line in [
        "SOFTWARE REQUIREMENTS SPECIFICATION",
        "(Đặc tả yêu cầu phần mềm)",
        "System: GMS — Gym Management System",
        "Version: 1.0-draft (assembled from docs/step0–8 — 11/11/2026)",
        "Group: GroupOfFour – Class: SWR302 (FALL2026)",
        "Members: Văn Xuân Phước (Leader) – DE190430; Nguyễn Anh Tuấn – DE201152; "
        "Nguyễn Ngô Tâm Thiên – DE190385; Đặng Nguyễn Huy – DE201171",
        "Instructor: (điền khi nộp)",
        "Date: 11/11/2026",
    ]:
        p = add_p(doc, line, bold=line.startswith("SOFTWARE") or line.startswith("System"))
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_note(
        doc,
        "Mã lớp / tên GV trên trang bìa còn trống. Zip nộp chưa làm lại — chờ AD-01 (Tuấn #30) và SMD PNG.",
    )

    # ===== REV =====
    add_heading(doc, "Revision History", 1)
    add_table(
        doc,
        ["Version", "Date", "Author", "Description"],
        [
            ["0.1", "10/11/2026", "Phuoc", "Draft cover + §1–2 scaffold"],
            ["0.2", "10/11/2026", "Phuoc", "English SRS body + UC-05/06"],
            ["0.9", "10–11/11/2026", "Team", "Merge steps 1–7 drafts into repo"],
            [
                "1.0-draft",
                "11/11/2026",
                "Phuoc (Leader)",
                "Full assemble from docs/step*; placeholders for unfinished teammate items",
            ],
            ["1.0", "", "Team", "[MISSING] Official freeze after AD-01 + SMD PNG + peer reviews"],
        ],
    )

    # ===== 1 =====
    add_heading(doc, "1. Introduction", 1)
    add_heading(doc, "1.1 Purpose", 2)
    add_p(
        doc,
        "This SRS specifies requirements for GMS version 1.0 — a gym management system covering "
        "membership registration/activation with QR check-in/out, personal trainer (PT) services, "
        "payments, notifications, complaints, and operational reports. Readers: Gym Owner / product "
        "owner, SWR302 analysts, developers/testers, and the course instructor. Sources: "
        "docs/01_Vision_Scope_GMS.md, docs/step1/*.",
    )

    add_heading(doc, "1.2 Document Conventions", 2)
    add_p(
        doc,
        "Font: Times New Roman 12–13; IDs: BO-xx, BR-xx, UC-xx, FR-xx, NFR-<TYPE>-xx, SCR-xx, "
        "CD/UCD/AD/SMD/ERD-xx. Priority: High / Medium / Low. Keywords: shall (mandatory), "
        "should (recommended), may (optional). End-user UI language: Vietnamese; this SRS body: English "
        "(team convention). Canonical Business Rules: Vision BR-01…BR-12 in §2.6 "
        "(note: docs/step3/huy_br_glossary.md uses a different BR numbering — do not mix IDs).",
    )

    add_heading(doc, "1.3 Project Scope", 2)
    add_p(
        doc,
        "GMS centralizes gym operations: customer & PT accounts, membership packages, counter "
        "registration & activation, QR gate events, PT booking lifecycle, payments, SMS/in-app "
        "notifications, basic complaints, and Excel operational reports.",
    )
    add_p(doc, "Business objectives", bold=True)
    add_table(
        doc,
        ["ID", "Business objective", "Success metric"],
        [
            [
                "BO-01",
                "Reduce front-desk register→activate time (Thiên)",
                "≤ 5 minutes / customer for ≥ 90% paid cases within 1 month",
            ],
            [
                "BO-02",
                "Increase valid check-in compliance (Thiên)",
                "≥ 95% entries logged; 100% non-ACTIVE QR denied ≤ 2s",
            ],
            [
                "BO-03",
                "Increase PT revenue; reduce hanging bookings (Vision; Tuấn draft empty)",
                "≥ 80% Pending leave Pending within 24h; PT no-show ≤ 15%",
            ],
            [
                "BO-04",
                "Owner decisions from operational data (Huy)",
                "≥ 90% monthly Excel exports ≤ 60s; Owner opens reports ≥ 1×/week in ≥ 10/12 weeks",
            ],
        ],
    )
    add_note(doc, "Tuấn step1/tuan_vision.md vẫn trống — BO-03 lấy từ Vision chung; cần Tuấn xác nhận metric.")

    add_p(doc, "In scope / Out of scope (Release 1)", bold=True)
    add_table(
        doc,
        ["In scope (Release 1)", "Out of scope / Later"],
        [
            ["Register/login/profile for Customer, PT, Owner", "Native iOS/Android apps"],
            ["Membership packages; counter register + activate; QR", "Hardware turnstile / biometrics"],
            ["QR check-in / check-out + manual code extend", "Apple/Google Wallet pass"],
            ["PT approval; PT packages; book/confirm/reject; record session", "External PT marketplace"],
            ["Online payment + cash; SMS/in-app notify", "Full accounting ERP"],
            ["Basic complaints; operational reports + Excel export", "AI plans; multi-branch / multi-currency"],
        ],
    )

    add_heading(doc, "1.4 References", 2)
    add_table(
        doc,
        ["#", "Reference"],
        [
            ["1", "HuongDan_Assignment.md — SWR302 assignment guide (FPT)"],
            ["2", "Nghị định 13/2023/NĐ-CP — personal data protection"],
            ["3", "Wiegers & Beatty, Software Requirements, 3rd ed."],
            ["4", "IEEE Std 830-1998"],
            ["5", "Visual Paradigm Community documentation"],
            ["6", "Repo drafts: docs/step1–step8, docs/01_Vision_Scope_GMS.md"],
        ],
    )

    # ===== 2 =====
    add_heading(doc, "2. Overall Description", 1)
    add_heading(doc, "2.1 Product Perspective", 2)
    add_p(
        doc,
        "GMS is a new standalone product replacing paper logs / disconnected spreadsheets. "
        "It integrates Payment Gateway, SMS Service, and QR Service. Periodic jobs use actor Time/Scheduler.",
    )
    add_p(doc, "Figure 2.1 — CD-01 Context Diagram of GMS", bold=True)
    try_picture(doc, IMG / "CD_ContextDiagram.png", caption="Figure 2.1. CD-01 Context Diagram")
    add_p(doc, "External entities (7) and sample data flows (≥12) — from docs/step2/phuoc_cd.md:", italic=True)
    add_table(
        doc,
        ["#", "Data flow", "From", "To"],
        [
            ["1", "Account registration info", "Customer", "GMS"],
            ["2", "Login / session", "Customer/PT/Owner", "GMS"],
            ["3", "Membership register & activate request", "Gym Owner", "GMS"],
            ["4", "Membership profile / QR", "GMS", "Customer/Owner"],
            ["5", "Check-in/out event & result", "Customer", "GMS"],
            ["6", "Payment request", "GMS", "Payment Gateway"],
            ["7", "Payment result", "Payment Gateway", "GMS"],
            ["8", "PT booking request & response", "Customer/PT", "GMS"],
            ["9", "SMS content", "GMS", "SMS Service"],
            ["10", "QR request / validation result", "GMS", "QR Service"],
            ["11", "PT approval decision", "Gym Owner", "GMS"],
            ["12", "Operational report", "GMS", "Gym Owner"],
            ["13", "Time event", "Time/Scheduler", "GMS"],
            ["14", "Complaint & handling result", "Customer", "GMS"],
        ],
    )
    add_note(
        doc,
        "Peer review Thiên (#42): sửa typo nhãn trên ảnh CD (Yêu cầu/Kết quả/Nội dung SMS/Đăng ký) khi mở lại VPP.",
    )

    add_heading(doc, "2.2 User Classes and Characteristics", 2)
    add_table(
        doc,
        ["User class", "Description", "Frequency", "Skill", "Main rights", "Favored?"],
        [
            [
                "Customer",
                "Gym member (Thiên step1)",
                "High 3–6×/week",
                "Basic smartphone/web",
                "QR, book PT, feedback",
                "Yes",
            ],
            [
                "Personal Trainer",
                "Coach managing packages/sessions (Vision; Tuấn step1 empty)",
                "High",
                "Basic–medium",
                "Confirm booking, schedule, record session",
                "Yes",
            ],
            [
                "Gym Owner",
                "Owner/manager (Huy step1)",
                "Med–High",
                "Browser + Excel",
                "UC-05/06/17/21/22, packages, complaints",
                "Yes",
            ],
        ],
    )

    add_heading(doc, "2.3 Operating Environment", 2)
    add_p(
        doc,
        "OE-1 Web app on latest Chrome/Edge, responsive. OE-2 Front desk PC/tablet; gate tablet camera for QR. "
        "OE-3 Linux cloud HTTPS; shared relational DB. OE-4 REST Payment Gateway, SMS API, QR module. (Huy step1)",
    )

    add_heading(doc, "2.4 Design and Implementation Constraints", 2)
    add_p(
        doc,
        "CON-1 Decree 13/2023/NĐ-CP for PII. CON-2 UI Vietnamese; VND; UTC+7; dd/mm/yyyy. "
        "CON-3 UML/DFD/ERD in Visual Paradigm (.vpp); wireframes Figma/Stitch/draw.io. "
        "CON-4 No card PAN storage — gateway only. CON-5 Release 1 = single gym site.",
    )

    add_heading(doc, "2.5 Assumptions and Dependencies", 2)
    add_table(
        doc,
        ["ID", "Assumption / Dependency", "Impact if false"],
        [
            ["AS-01", "Authorized staff at counter during open hours", "Counter membership blocked"],
            ["AS-02", "One stable QR per ACTIVE membership", "Wrong-person check-in"],
            ["AS-03", "ACTIVE membership required to book PT", "Need walk-in exception flow"],
            ["DE-01", "Payment Gateway sandbox available", "Cannot E2E test payments"],
            ["DE-02", "SMS provider available", "Fallback in-app only"],
            ["DE-03", "QR camera usable; else ManualEntry extend", "Higher deny/retry rate"],
        ],
    )

    add_heading(doc, "2.6 Business Rules", 2)
    add_p(doc, "Canonical BR set (Vision / UC dressed). Do not confuse with Huy step3 BR renumbering.", italic=True)
    add_table(
        doc,
        ["ID", "Business rule", "Type"],
        [
            ["BR-01", "Only logged-in Gym Owner may register/activate membership at counter", "Constraint"],
            ["BR-02", "Membership becomes ACTIVE only after full fee recorded", "Constraint"],
            ["BR-03", "EndDate = activation date + package DurationMonths (end of day UTC+7)", "Computation"],
            ["BR-04", "Exactly one QR while ACTIVE; invalidate when status ≠ ACTIVE", "Constraint"],
            ["BR-05", "Valid check-in only in open hours AND ACTIVE membership", "Constraint"],
            ["BR-06", "Customer books PT only with ACTIVE membership ≥ 1 day left", "Constraint"],
            ["BR-07", "PT operates bookings only when account Approved", "Constraint"],
            ["BR-08", "PT must respond to Pending within 24h; else auto-Cancel + refund", "Action enabler"],
            ["BR-09", "Reject requires reason; paid → initiate refund", "Action enabler"],
            ["BR-10", "Record session only for Confirmed booking with remaining sessions", "Constraint"],
            ["BR-11", "Scheduler: ACTIVE with end_date < today → EXPIRED, kill QR, SMS", "Action enabler"],
            ["BR-12", "Complaint only within 7 days of related session/event", "Constraint"],
        ],
    )

    # ===== 3 =====
    add_heading(doc, "3. System Features", 1)
    add_heading(doc, "3.1 Use Case Overview", 2)
    add_p(doc, "Actors", bold=True)
    add_table(
        doc,
        ["Actor", "Type", "User class"],
        [
            ["Customer", "Primary", "Customer"],
            ["Personal Trainer", "Primary", "PT"],
            ["Gym Owner", "Primary", "Gym Owner"],
            ["Payment Gateway", "Secondary", "—"],
            ["SMS Service", "Secondary", "—"],
            ["QR Service", "Secondary", "—"],
            ["Time / Scheduler", "Secondary", "—"],
            ["User (abstract)", "Generalization parent", "Login/profile shared"],
        ],
    )
    add_p(doc, "Figure 3.1 — UCD Overview", bold=True)
    try_picture(doc, IMG / "UCD_Overview.png", width=5.5, caption="Figure 3.1. UCD-01 Overview")
    add_p(doc, "Package diagrams", bold=True)
    for name, file in [
        ("UCD Membership", "UCD_Membership.png"),
        ("UCD PT", "UCD_PT.png"),
        ("UCD Report/Feedback", "UCD_Report_Feedback.png"),
    ]:
        add_p(doc, name, italic=True)
        try_picture(doc, IMG / file, width=4.8)

    add_p(doc, "Use case catalogue (excerpt High priority — full list docs/02_UC_List_Detailed.md)", bold=True)
    add_table(
        doc,
        ["UC-ID", "Name", "Primary", "Priority", "Package"],
        [
            ["UC-05", "Register Membership (at Counter)", "Gym Owner", "H", "Membership"],
            ["UC-06", "Activate Membership", "Gym Owner", "H", "Membership"],
            ["UC-08", "Check-in by QR", "Customer", "H", "Membership"],
            ["UC-11", "Book a PT Package", "Customer", "H", "PT"],
            ["UC-12", "Confirm/Reject PT Booking", "PT", "H", "PT"],
            ["UC-15", "Record Training Session", "PT", "H", "PT"],
            ["UC-16", "Register PT Account", "PT", "H", "PT"],
            ["UC-17", "Approve/Reject PT", "Gym Owner", "H", "PT"],
            ["UC-27", "Auto-expire Membership (Time)", "Time", "H", "Membership"],
        ],
    )

    # Fully dressed UCs
    add_heading(doc, "3.2 Fully Dressed Use Cases (≥8)", 2)
    uc_files = [
        ("3.2.1 UC-05 Register Membership (at Counter)", "UC-05.md", "UI_UC-05_RegisterMembership.png", "UI_UC-05_RegisterMembership_Error.png"),
        ("3.2.2 UC-06 Activate Membership", "UC-06.md", "UI_UC-06_ActivateMembership.png", "UI_UC-06_ActivateMembership_Error.png"),
        ("3.2.3 UC-08 Check-in by QR", "UC-08.md", "UI_UC-08_QRCheckIn.png", "UI_UC-08_QRCheckIn_Error.png"),
        ("3.2.4 UC-11 Book a PT Package", "UC-11.md", "UI_UC11_BookPT.png", None),
        ("3.2.5 UC-12 Confirm/Reject PT Booking", "UC-12.md", "UI_UC12_PTBooking.png", None),
        ("3.2.6 UC-15 Record Training Session", "UC-15.md", "UI_UC-15_RecordSession.png", "UI_UC-15_RecordSession_Error.png"),
        ("3.2.7 UC-16 Register PT Account", "UC-16.md", "UI_UC-16_RegisterPT.png", None),
        ("3.2.8 UC-17 Approve/Reject PT", "UC-17.md", "UI_UC-17_ApprovePT.png", None),
    ]
    for title, md_name, ui, ui_err in uc_files:
        add_heading(doc, title, 3)
        md_path = ROOT / "docs" / "step4" / md_name
        fields = parse_md_field_table(md_path)
        # Prefer classic Field/Content pairs; if Tuấn-style multi tables, paste key sections as prose
        classic = [(k, v) for k, v in fields if k.lower() not in {"use case id", "screen name", "png file", "uc"}]
        if classic and any("Normal Flow" in k or "Main success" in k or "Description" in k for k, _ in classic):
            # keep important rows only to avoid huge duplicate headers
            keep = []
            seen = set()
            for k, v in classic:
                if k in seen:
                    continue
                if any(
                    x in k
                    for x in [
                        "UC ID",
                        "Primary",
                        "Secondary",
                        "Trigger",
                        "Description",
                        "Goal",
                        "Preconditions",
                        "Precondition",
                        "Post",
                        "Normal",
                        "Main success",
                        "Alternative",
                        "Exception",
                        "Priority",
                        "Business Rules",
                        "Related business",
                    ]
                ):
                    keep.append((k, v[:1500] + ("…" if len(v) > 1500 else "")))
                    seen.add(k)
            if keep:
                add_table(doc, ["Field", "Content"], keep)
            else:
                add_p(doc, read_text(md_path)[:3500])
        else:
            # fallback: embed markdown truncated
            body = read_text(md_path)
            if not body.strip() or "điền tên" in body or body.count("|") < 5:
                add_note(doc, f"{md_name} incomplete")
            else:
                # take first 80 lines
                lines = [ln for ln in body.splitlines() if not ln.startswith(">")]
                add_p(doc, "\n".join(lines[:90])[:4000])
        add_p(doc, "Wireframe (Step 5)", bold=True)
        try_picture(doc, IMG / ui, width=4.5)
        if ui_err:
            try_picture(doc, IMG / ui_err, width=4.2, caption="Error / exception state")
        else:
            add_note(doc, f"{md_name}: dedicated error PNG optional — validation described in docs/step5 field tables.")

    add_heading(doc, "3.3 Other use cases (brief)", 2)
    add_p(
        doc,
        "Brief descriptions for remaining catalogue UCs (UC-01…04, 07, 09–10, 13–14, 18–28) are listed in "
        "docs/02_UC_List_Detailed.md. Fully dressed elaboration beyond the eight High UCs is out of Release-1 "
        "documentation depth unless expanded later.",
    )

    add_heading(doc, "3.4 Behaviour models — Activity & State", 2)
    add_p(doc, "AD-03 Activate Membership at counter (Phước+Thiên #32)", bold=True)
    try_picture(doc, IMG / "AD_ActivateMembership.png", caption="Figure — AD-03")
    add_p(doc, "AD-02 Approve PT (Huy #31)", bold=True)
    try_picture(doc, IMG / "AD_ApprovePT.png", caption="Figure — AD-02")
    add_p(doc, "AD-01 Book PT & payment (Tuấn #30)", bold=True)
    add_note(
        doc,
        "AD-01 CHƯA CÓ — issue #30 OPEN; docs/step6/tuan_ad01.md trống; thiếu 03_Images/AD_BookPT.png. "
        "Đây là blocker bước 6 checklist #33.",
    )

    add_p(doc, "SMD-01 Membership & SMD-02 PT Booking (Thiên #34) — transition audit", bold=True)
    add_note(
        doc,
        "PNG SMD_Membership.png / SMD_PTBooking.png chưa export từ VP. Dưới đây là bảng transition từ docs/step7/thien_smd.md.",
    )
    add_p(doc, "SMD-01 key transitions (UC / Time)", italic=True)
    add_table(
        doc,
        ["ID", "Event", "Type", "Target", "UC/BR"],
        [
            ["T1", "registerMembership", "UC", "Inactive", "UC-05, BR-01"],
            ["T2", "activate", "UC", "Active", "UC-06, BR-02/03/04"],
            ["T5", "when(current_date > end_date)", "Time", "Expired", "UC-27, BR-11"],
            ["T6", "suspend", "Owner", "Suspended", "BR-04"],
            ["T10", "renew", "UC", "Active", "UC-20"],
        ],
    )
    add_p(doc, "SMD-02 key transitions (UC / Time)", italic=True)
    add_table(
        doc,
        ["ID", "Event", "Type", "Target", "UC/BR"],
        [
            ["T1", "bookPTPackage", "UC", "Pending", "UC-11, BR-06/08"],
            ["T2", "confirmBooking", "UC", "Confirmed", "UC-12"],
            ["T3", "rejectBooking", "UC", "Rejected", "UC-12, BR-09"],
            ["T4", "after(24h)", "Time", "Cancelled", "BR-08"],
            ["T6+", "recordSession", "UC", "In Progress/Completed", "UC-15, BR-10"],
        ],
    )

    add_heading(doc, "3.5 Functional Requirements (derived sample)", 2)
    add_table(
        doc,
        ["ID", "Requirement", "Trace", "Priority"],
        [
            ["FR-05-01", "System shall create Membership INACTIVE after counter registration", "UC-05, BR-01/02", "H"],
            ["FR-06-01", "System shall set ACTIVE and generate QR only when fee fully paid", "UC-06, BR-02/04", "H"],
            ["FR-08-01", "System shall validate QR and open-hours before CheckInLog", "UC-08, BR-04/05", "H"],
            ["FR-11-01", "System shall create Pending booking after successful payment", "UC-11, BR-06/08", "H"],
            ["FR-12-01", "System shall allow Confirm/Reject within 24h with refund rules", "UC-12, BR-08/09", "H"],
            ["FR-15-01", "System shall decrement remaining sessions on record", "UC-15, BR-10", "H"],
            ["FR-16-01", "System shall accept PT registration as Pending approval", "UC-16, BR-07", "H"],
            ["FR-17-01", "Owner shall Approve/Reject PT with reason on reject", "UC-17, BR-07", "H"],
            ["FR-27-01", "Scheduler shall expire memberships past EndDate", "UC-27, BR-11", "H"],
        ],
    )

    # ===== 4 =====
    add_heading(doc, "4. Data Requirements", 1)
    add_heading(doc, "4.1 Logical Data Model", 2)
    add_p(doc, "Figure 4.1 — ERD-01 Conceptual (Huy #35)", bold=True)
    try_picture(doc, IMG / "ERD_Conceptual.png", caption="Figure 4.1. ERD-01")
    add_table(
        doc,
        ["Vision name", "Huy ERD entity"],
        [
            ["Customer", "Member (+ Account)"],
            ["Gym Owner", "Gym_Owner"],
            ["Personal Trainer", "Personal_trainer"],
            ["Membership", "Customer_Membership"],
            ["MembershipPackage", "Membership_Package"],
            ["PTBooking", "Booking"],
            ["CheckInLog", "Check_In"],
            ["Payment", "Payment"],
        ],
    )
    add_note(
        doc,
        "Tuấn #36 tuan_erd_review.md trống — chưa bổ sung TrainingSession / review SMD-02 trên ERD. "
        "Booking.Status domain in ERD text may omit IN_PROGRESS/REJECTED vs SMD-02 — cần đồng bộ.",
    )

    add_heading(doc, "4.2 Data Dictionary", 2)
    add_p(doc, "Summary from docs/step7/huy_erd.md (full attribute tables live there).", italic=True)
    add_table(
        doc,
        ["Entity", "Key attributes", "Notes"],
        [
            ["Account", "accountID, UserName, Password_Hash, Status, RoleID", "NFR-SEC-01 hashing"],
            ["Role", "RoleID, RoleName", "Owner/PT/Member"],
            ["Member", "Member_ID, FullName, Phone, Mail", "Customer profile"],
            ["Membership_Package", "Package_ID, PackageName, Price, Durations_Days", "Catalog"],
            ["Customer_Membership", "EnrollmentID, Start/ExpireDate, Status", "Align SMD-01 statuses"],
            ["Personal_trainer", "PT_ID, Specialty, Experience_years, Account", "BR-07 Approved"],
            ["Booking", "Booking_ID, DateTime, Status, PT, Member", "Align SMD-02"],
            ["Check_In", "CheckIN_ID, DateTime, Method, Member", "UC-08"],
            ["Payment", "PaymentID, Amount, Method, Status", "Gateway/cash"],
            ["Equipment_inventory / Maintenance_Log", "Equipment + maintenance cost", "Extra R1 entities"],
        ],
    )

    add_heading(doc, "4.3 Reports", 2)
    add_table(
        doc,
        ["ID", "Name", "User", "Sources"],
        [
            ["RPT-01", "Revenue summary", "Gym Owner", "Payment, Customer_Membership, Booking"],
            ["RPT-02", "Check-in statistics", "Gym Owner", "Check_In, Customer_Membership"],
            ["RPT-03", "PT performance", "Gym Owner", "Booking / sessions"],
        ],
    )

    add_heading(doc, "4.4 Collection, Integrity, Retention", 2)
    add_p(
        doc,
        "Collection via UC-05/06, booking/QR, gateway callbacks, scheduler UC-27/28. "
        "Integrity: BR-02/04 and FK Account↔profiles. Retention draft: operational logs ≥ 12 months; "
        "archive Cancelled per SMD-01 T11.",
    )

    # ===== 5 =====
    add_heading(doc, "5. External Interface Requirements", 1)
    add_heading(doc, "5.1 User Interfaces", 2)
    add_p(doc, "Screen map (Step 5 wireframes)", bold=True)
    add_table(
        doc,
        ["SCR", "UC", "PNG", "Owner"],
        [
            ["SCR-05", "UC-05", "UI_UC-05_RegisterMembership.png (+Error)", "Phước"],
            ["SCR-06", "UC-06", "UI_UC-06_ActivateMembership.png (+Error)", "Phước"],
            ["SCR-08", "UC-08", "UI_UC-08_QRCheckIn.png (+Error)", "Thiên"],
            ["SCR-11", "UC-11", "UI_UC11_BookPT.png", "Tuấn"],
            ["SCR-12", "UC-12", "UI_UC12_PTBooking.png", "Tuấn"],
            ["SCR-15", "UC-15", "UI_UC-15_RecordSession.png (+Error)", "Thiên"],
            ["SCR-16", "UC-16", "UI_UC-16_RegisterPT.png", "Huy"],
            ["SCR-17", "UC-17", "UI_UC-17_ApprovePT.png", "Huy"],
        ],
    )
    add_p(
        doc,
        "Style: Vietnamese labels on UI; English IDs in SRS. Field/validation tables: docs/step5/*_ui.md. "
        "Huy NFR-USAB-01: core reception tasks < 30s for new users.",
    )

    add_heading(doc, "5.2 Software Interfaces", 2)
    add_p(
        doc,
        "Payment Gateway (REST pay/refund callbacks); SMS Service API; QR generation/validation module; "
        "relational DBMS. (Huy NFR + Vision OE-4)",
    )

    add_heading(doc, "5.3 Hardware Interfaces", 2)
    add_p(
        doc,
        "Không áp dụng thiết bị chuyên dụng — lý do: Release 1 dùng camera điện thoại/tablet tiêu chuẩn để quét QR; "
        "không tích hợp turnstile phần cứng.",
    )

    add_heading(doc, "5.4 Communications Interfaces", 2)
    add_p(doc, "HTTPS for clients/APIs; SMS provider channel; payment callbacks over TLS.")

    # ===== 6 =====
    add_heading(doc, "6. Quality Attributes", 1)
    add_p(doc, "From docs/step8/huy_nfr.md (#39).", italic=True)
    add_table(
        doc,
        ["NFR-ID", "Description", "Measurement", "Target"],
        [
            ["NFR-PERF-01", "Lookup/check-in response under load", "JMeter / Network @100 concurrent", "Avg ≤1.5s; max ≤3s"],
            ["NFR-SEC-01", "Password hashing", "Inspect Account store", "BCrypt factor ≥10; no plaintext"],
            ["NFR-SEC-02", "Session timeout", "Idle session test", "Logout after 15 minutes"],
            ["NFR-USAB-01", "Receptionist core task time", "UAT 5 new users", "100% <30s"],
            ["NFR-REL-01", "Daily backup", "Verify schedule", "Daily end-of-day full backup"],
        ],
    )
    add_note(doc, "Planguage TAG blocks (≥2) — có thể bổ sung formal TAG: từ mẫu HuongDan nếu GV yêu cầu chặt.")

    # ===== 7–8 =====
    add_heading(doc, "7. Internationalization and Localization Requirements", 1)
    add_p(doc, "End-user UI: Vietnamese. Dates dd/mm/yyyy. Currency VND. Time zone UTC+7. SRS/model names: English.")

    add_heading(doc, "8. Other Requirements", 1)
    add_p(
        doc,
        "Personal-data compliance (Decree 13/2023). Short front-desk operating guidance. "
        "No thick desktop client in R1.",
    )

    # ===== APPENDICES =====
    add_heading(doc, "Appendix A – Glossary", 1)
    add_table(
        doc,
        ["Term", "Definition"],
        [
            ["Membership", "Customer–package contract with status lifecycle (SMD-01)"],
            ["QR Membership", "Token valid only while membership ACTIVE (BR-04)"],
            ["PT Booking", "Order for PT package sessions (SMD-02)"],
            ["Training Session", "One delivered session under a booking (UC-15)"],
            ["Pending Booking", "Paid/awaiting PT confirm within 24h (BR-08)"],
            ["Gym Owner", "Highest admin role for counter, PT approval, reports"],
            ["Check-in / Check-out", "Gate event logged via QR validation"],
        ],
    )

    add_heading(doc, "Appendix B – Analysis Models", 1)
    add_table(
        doc,
        ["ID", "Name", "Image / location", "Status"],
        [
            ["CD-01", "Context Diagram", "CD_ContextDiagram.png", "OK (typo polish pending)"],
            ["UCD-01", "Overview + packages", "UCD_*.png", "OK"],
            ["AD-01", "Book PT & payment", "AD_BookPT.png", "MISSING — Tuấn #30"],
            ["AD-02", "Approve PT", "AD_ApprovePT.png", "OK (from step-6)"],
            ["AD-03", "Activate Membership", "AD_ActivateMembership.png", "OK"],
            ["SMD-01", "Membership lifecycle", "SMD_Membership.png", "MISSING PNG — tables OK"],
            ["SMD-02", "PT Booking lifecycle", "SMD_PTBooking.png", "MISSING PNG — tables OK"],
            ["ERD-01", "Conceptual ERD", "ERD_Conceptual.png", "OK"],
        ],
    )

    add_heading(doc, "Appendix C – Traceability Matrix", 1)
    add_p(
        doc,
        "Authoritative file: 04_Traceability_Matrix.xlsx (sheets Traceability + NFR). "
        "Also docs/step7/phuoc_srs_trace.md. Columns: BO | UC | FR | BR | Diagram | Screen | NFR | Test.",
    )

    add_heading(doc, "Appendix D – Open Issues / Missing from teammates", 1)
    add_table(
        doc,
        ["ID", "Gap", "Owner", "Blocks"],
        [
            ["OI-01", "AD-01 Book PT PNG + swimlane write-up", "Tuấn #30", "Step 6 checklist #33"],
            ["OI-02", "SMD_Membership.png & SMD_PTBooking.png VP export", "Thiên #34", "SRS figures / zip A.3"],
            ["OI-03", "tuan_vision.md empty (PT user class / BO-03 confirm)", "Tuấn #6", "Formal Vision freeze"],
            ["OI-04", "tuan_erd_review.md empty (TrainingSession + SMD-02 review)", "Tuấn #36", "ERD consistency"],
            ["OI-05", "tuan_peer_review.md empty", "Tuấn #41", "Step 8 checklist #43"],
            ["OI-06", "Instructor / exact class code on cover", "Phước", "Cover page"],
            ["OI-07", "CD typo fixes on VPP export", "Phước (+ Thiên review)", "Polish"],
            ["OI-08", "BR ID drift Huy step3 vs Vision", "Huy/Phước", "Traceability clarity"],
        ],
    )

    add_heading(doc, "Appendix E – Source map (docs/step*)", 1)
    add_table(
        doc,
        ["Step", "Key files consumed"],
        [
            ["1", "thien_vision, huy_vision, 01_Vision_Scope_GMS (tuan_vision empty)"],
            ["2", "phuoc_cd + UC list"],
            ["3", "UCD PNGs; huy_br_glossary (glossary); thien/tuan UCD notes"],
            ["4", "UC-05/06/08/11/12/15/16/17.md"],
            ["5", "*_ui.md + UI_*.png"],
            ["6", "AD-03 + AD-02; AD-01 missing"],
            ["7", "huy_erd, thien_smd, phuoc_srs_trace, ERD png"],
            ["8", "huy_nfr; thien_peer_review; tuan_peer empty"],
        ],
    )

    doc.save(OUT)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
