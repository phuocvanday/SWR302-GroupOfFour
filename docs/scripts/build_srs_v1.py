# -*- coding: utf-8 -*-
"""Assemble 01_SRS_GMS.docx from docs/step* — VP diagrams only; UC Field|Content tables; font 13; black headings."""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "03_Images"
OUT = ROOT / "01_SRS_GMS.docx"
BLACK = RGBColor(0, 0, 0)

# Only Visual Paradigm exports (no wireframe / PlantUML draft / Stitch)
VP_ALLOWED = {
    "CD_ContextDiagram.png",
    "UCD_Overview.png",  # official VP export path in step3 notes
    "AD_ActivateMembership.png",
    "AD_ApprovePT.png",
    "ERD_Conceptual.png",
}

UC_FIELD_ORDER = [
    "UC ID and Name",
    "Created By",
    "Date Created",
    "Primary Actor",
    "Secondary Actors",
    "Trigger",
    "Description",
    "Preconditions",
    "Post conditions",
    "Normal Flow",
    "Alternative Flows",
    "Exceptions",
    "Priority",
    "Frequency of Use",
    "Business Rules",
    "Other Information",
    "Assumptions",
]


def set_run(run, size=13, bold=False, italic=False, color=BLACK):
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.name = "Times New Roman"
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")
    rFonts.set(qn("w:eastAsia"), "Times New Roman")


def force_black_headings(doc: Document) -> None:
    for style_name in ["Heading 1", "Heading 2", "Heading 3", "Title", "Normal"]:
        try:
            style = doc.styles[style_name]
        except KeyError:
            continue
        style.font.name = "Times New Roman"
        style.font.color.rgb = BLACK
        if style_name == "Normal":
            style.font.size = Pt(13)
        elif style_name == "Heading 1":
            style.font.size = Pt(16)
            style.font.bold = True
        elif style_name == "Heading 2":
            style.font.size = Pt(14)
            style.font.bold = True
        elif style_name == "Heading 3":
            style.font.size = Pt(13)
            style.font.bold = True


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        set_run(run, size={1: 16, 2: 14, 3: 13}.get(level, 13), bold=True, color=BLACK)
    # also clear theme color on paragraph
    for run in h.runs:
        run.font.color.rgb = BLACK
    return h


def add_p(doc, text="", bold=False, italic=False, size=13):
    p = doc.add_paragraph()
    run = p.add_run(text)
    set_run(run, size=size, bold=bold, italic=italic)
    return p


def add_note(doc, text):
    p = doc.add_paragraph()
    run = p.add_run("[NOTE] " + text)
    set_run(run, size=12, bold=True, color=RGBColor(0x33, 0x33, 0x33))
    return p


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        r = cell.paragraphs[0].add_run(h)
        set_run(r, size=13, bold=True)
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            cell = table.rows[r_i + 1].cells[c_i]
            cell.text = ""
            # strip HTML <br> from Huy UCs
            text = str(val) if val is not None else ""
            text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
            r = cell.paragraphs[0].add_run(text)
            set_run(r, size=13)
    doc.add_paragraph()
    return table


def try_vp_picture(doc, filename: str, width=5.6, caption=None, note=None):
    """Embed only if file is in VP_ALLOWED allow-list."""
    if filename not in VP_ALLOWED:
        add_note(
            doc,
            f"Không nhúng {filename} — không phải sơ đồ Visual Paradigm chính thức (wireframe/PlantUML/nháp).",
        )
        return False
    path = IMG / filename
    if not path.exists():
        add_note(doc, f"Thiếu file VP: 03_Images/{filename}" + (f" | {note}" if note else ""))
        return False
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path), width=Inches(width))
    if caption:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cap.add_run(caption)
        set_run(r, size=12, bold=True, italic=True)
    note_bits = [f"Source: 03_Images/{filename} (Visual Paradigm export)"]
    if note:
        note_bits.append(note)
    note_bits.append("PNG ≥ 150 dpi (A.3).")
    n = doc.add_paragraph()
    n.alignment = WD_ALIGN_PARAGRAPH.CENTER
    nr = n.add_run(" · ".join(note_bits))
    set_run(nr, size=11, italic=True, color=RGBColor(0x44, 0x44, 0x44))
    return True


def parse_uc_field_table(path: Path) -> list[tuple[str, str]]:
    """Parse first Field|Content markdown table into ordered pairs."""
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    raw: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(parts) < 2:
            continue
        key = re.sub(r"\*+", "", parts[0]).strip()
        val = parts[1].strip()
        if not key or key.lower() in {"field", "item"} or set(key) <= {"-", ":"}:
            continue
        if key.startswith("---") or val.startswith("---"):
            continue
        # skip non Field/Content header rows from other tables
        if key.lower() in {"uc", "screen name", "png file", "screen", "uc-id"}:
            continue
        if key not in raw:
            raw[key] = val.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")

    # normalize Post conditions naming
    if "Post conditions" not in raw:
        for k in list(raw):
            if k.lower().startswith("post"):
                raw["Post conditions"] = raw.pop(k)
                break

    ordered = []
    used = set()
    for want in UC_FIELD_ORDER:
        # fuzzy match
        match = None
        for k in raw:
            if k.lower() == want.lower() or want.lower() in k.lower() or k.lower() in want.lower():
                match = k
                break
        if match and match not in used:
            ordered.append((want if want in UC_FIELD_ORDER else match, raw[match]))
            used.add(match)
    # append remaining Field-like keys
    for k, v in raw.items():
        if k not in used and any(
            x in k
            for x in [
                "UC ID",
                "Actor",
                "Trigger",
                "Description",
                "Precondition",
                "Post",
                "Normal",
                "Alternative",
                "Exception",
                "Priority",
                "Frequency",
                "Business",
                "Other",
                "Assumption",
                "Created",
                "Date",
            ]
        ):
            ordered.append((k, v))
    return ordered


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def build():
    doc = Document()
    force_black_headings(doc)

    for line in [
        "SOFTWARE REQUIREMENTS SPECIFICATION",
        "(Đặc tả yêu cầu phần mềm)",
        "System: GMS — Gym Management System",
        "Version: 1.0-draft (11/11/2026)",
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
        "Chỉ nhúng sơ đồ Visual Paradigm (CD/UCD Overview/AD/ERD). Wireframe UI và PlantUML draft KHÔNG đính kèm. "
        "UC fully dressed dùng bảng Field|Content đồng bộ template UC-05.",
    )

    add_heading(doc, "Revision History", 1)
    add_table(
        doc,
        ["Version", "Date", "Author", "Description"],
        [
            ["0.1", "10/11/2026", "Phuoc", "Draft cover + §1–2"],
            ["0.9", "10–11/11/2026", "Team", "Merge step drafts"],
            [
                "1.0-draft",
                "11/11/2026",
                "Phuoc",
                "UC Field|Content sync; black headings; font 13; VP images only",
            ],
            ["1.0", "", "Team", "Official freeze after AD-01 + SMD VP PNG"],
        ],
    )

    # ---- 1 ----
    add_heading(doc, "1. Introduction", 1)
    add_heading(doc, "1.1 Purpose", 2)
    add_p(
        doc,
        "This SRS specifies requirements for GMS version 1.0 — membership with QR check-in/out, "
        "PT services, payments, notifications, complaints, and operational reports. "
        "Readers: Gym Owner, SWR302 analysts, developers/testers, instructor.",
    )
    add_heading(doc, "1.2 Document Conventions", 2)
    add_p(
        doc,
        "Font: Times New Roman 13; headings black. IDs: BO-xx, BR-xx, UC-xx, FR-xx, NFR-<TYPE>-xx, SCR-xx. "
        "Priority: High/Medium/Low. shall / should / may. UI language Vietnamese; SRS body English. "
        "Fully dressed UC template: two-column Field | Content table (same as docs/step4/UC-05.md).",
    )
    add_heading(doc, "1.3 Project Scope", 2)
    add_p(
        doc,
        "GMS centralizes gym operations: accounts, membership packages, counter registration & activation, "
        "QR gate events, PT booking lifecycle, payments, SMS/in-app notifications, complaints, Excel reports.",
    )
    add_p(doc, "Business objectives", bold=True)
    add_table(
        doc,
        ["ID", "Business objective", "Success metric"],
        [
            ["BO-01", "Reduce register→activate time at counter", "≤ 5 min / customer for ≥ 90% paid cases (1 month)"],
            ["BO-02", "Valid check-in compliance", "≥ 95% logged; 100% non-ACTIVE QR denied ≤ 2s"],
            ["BO-03", "PT revenue; reduce hanging bookings", "≥ 80% Pending leave Pending in 24h; no-show ≤ 15%"],
            ["BO-04", "Owner decisions from data", "≥ 90% Excel exports ≤ 60s; reports ≥ weekly"],
        ],
    )
    add_p(doc, "In scope / Out of scope (Release 1)", bold=True)
    add_table(
        doc,
        ["In scope (Release 1)", "Out of scope / Later"],
        [
            ["Register/login/profile; membership + QR check-in/out", "Native apps; hardware turnstile"],
            ["PT approve/book/confirm/record session", "External PT marketplace"],
            ["Payment gateway + cash; SMS; complaints; Excel reports", "Full ERP; multi-branch"],
        ],
    )
    add_heading(doc, "1.4 References", 2)
    add_table(
        doc,
        ["#", "Reference"],
        [
            ["1", "HuongDan_Assignment.md — SWR302"],
            ["2", "Nghị định 13/2023/NĐ-CP"],
            ["3", "Wiegers & Beatty, Software Requirements, 3rd ed."],
            ["4", "IEEE Std 830-1998"],
            ["5", "Visual Paradigm Community"],
            ["6", "Repo: docs/step1–8, docs/01_Vision_Scope_GMS.md"],
        ],
    )

    # ---- 2 ----
    add_heading(doc, "2. Overall Description", 1)
    add_heading(doc, "2.1 Product Perspective", 2)
    add_p(
        doc,
        "GMS is a new standalone product replacing paper/Excel. Integrates Payment Gateway, SMS Service, QR Service; "
        "scheduler jobs via Time/Scheduler.",
    )
    try_vp_picture(
        doc,
        "CD_ContextDiagram.png",
        caption="Figure 2.1 — CD-01 Context Diagram of GMS",
        note="1 process; ≥5 entities; ≥12 data flows. Owner: Phước #10.",
    )
    add_p(doc, "Sample data flows (≥12) — docs/step2/phuoc_cd.md", italic=True)
    add_table(
        doc,
        ["#", "Data flow", "From", "To"],
        [
            ["1", "Account registration info", "Customer", "GMS"],
            ["2", "Login / session", "Customer/PT/Owner", "GMS"],
            ["3", "Membership register & activate", "Gym Owner", "GMS"],
            ["4", "Membership profile / QR", "GMS", "Customer/Owner"],
            ["5", "Check-in/out event & result", "Customer", "GMS"],
            ["6", "Payment request", "GMS", "Payment Gateway"],
            ["7", "Payment result", "Payment Gateway", "GMS"],
            ["8", "PT booking request & response", "Customer/PT", "GMS"],
            ["9", "SMS content", "GMS", "SMS Service"],
            ["10", "QR request / validation", "GMS", "QR Service"],
            ["11", "PT approval decision", "Gym Owner", "GMS"],
            ["12", "Operational report", "GMS", "Gym Owner"],
            ["13", "Time event", "Time/Scheduler", "GMS"],
            ["14", "Complaint & handling result", "Customer", "GMS"],
        ],
    )

    add_heading(doc, "2.2 User Classes and Characteristics", 2)
    add_table(
        doc,
        ["User class", "Description", "Frequency", "Skill", "Main rights", "Favored?"],
        [
            ["Customer", "Gym member", "High", "Basic", "QR, book PT, feedback", "Yes"],
            ["Personal Trainer", "Coach", "High", "Basic–medium", "Confirm booking, record session", "Yes"],
            ["Gym Owner", "Owner/manager", "Med–High", "Browser+Excel", "UC-05/06/17/21/22", "Yes"],
        ],
    )
    add_heading(doc, "2.3 Operating Environment", 2)
    add_p(
        doc,
        "Web on Chrome/Edge responsive; desk PC/tablet + gate camera; Linux cloud HTTPS; relational DB; "
        "REST Payment, SMS API, QR module.",
    )
    add_heading(doc, "2.4 Design and Implementation Constraints", 2)
    add_p(
        doc,
        "Decree 13/2023; UI Vietnamese; VND; UTC+7; dd/mm/yyyy; UML/DFD/ERD in Visual Paradigm (.vpp); "
        "wireframes may use Figma/Stitch/draw.io but are NOT embedded in this SRS; no card PAN storage; single site R1.",
    )
    add_heading(doc, "2.5 Assumptions and Dependencies", 2)
    add_table(
        doc,
        ["ID", "Assumption / Dependency", "Impact if false"],
        [
            ["AS-01", "Staff at counter in open hours", "Counter membership blocked"],
            ["AS-02", "One QR per ACTIVE membership", "Wrong-person check-in"],
            ["AS-03", "ACTIVE membership required to book PT", "Need walk-in exception"],
            ["DE-01", "Payment Gateway sandbox", "Cannot E2E pay tests"],
            ["DE-02", "SMS provider available", "In-app fallback only"],
            ["DE-03", "QR camera usable else ManualEntry", "Higher retry rate"],
        ],
    )
    add_heading(doc, "2.6 Business Rules", 2)
    add_table(
        doc,
        ["ID", "Business rule", "Type"],
        [
            ["BR-01", "Only logged-in Gym Owner registers/activates membership at counter", "Constraint"],
            ["BR-02", "ACTIVE only after full fee recorded", "Constraint"],
            ["BR-03", "EndDate = activation + DurationMonths (UTC+7)", "Computation"],
            ["BR-04", "One QR while ACTIVE; invalidate otherwise", "Constraint"],
            ["BR-05", "Check-in only in open hours + ACTIVE", "Constraint"],
            ["BR-06", "Book PT only with ACTIVE membership ≥ 1 day", "Constraint"],
            ["BR-07", "PT operates bookings only when Approved", "Constraint"],
            ["BR-08", "PT responds Pending within 24h else Cancel+refund", "Action enabler"],
            ["BR-09", "Reject requires reason; paid → refund", "Action enabler"],
            ["BR-10", "Record session only Confirmed + remaining > 0", "Constraint"],
            ["BR-11", "Scheduler expires membership past EndDate", "Action enabler"],
            ["BR-12", "Complaint within 7 days of event", "Constraint"],
        ],
    )

    # ---- 3 ----
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
            ["User (abstract)", "Generalization", "Login shared"],
        ],
    )
    try_vp_picture(
        doc,
        "UCD_Overview.png",
        width=5.4,
        caption="Figure 3.1 — UCD-01 Use Case Overview of GMS",
        note="Official VP export. Owner: Phước #15.",
    )
    add_note(
        doc,
        "UCD package diagrams (Membership / PT / Report) — chỉ chấp nhận export từ GMS.vpp. "
        "Các PNG PlantUML/nháp (UCD_Membership.png, UCD_PT.png, UCD_Report_Feedback.png) KHÔNG đính kèm. "
        "Thiên/Tuấn/Huy redraw trong VP rồi export lại.",
    )
    add_p(doc, "High-priority use cases (fully dressed below)", bold=True)
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
        ],
    )

    add_heading(doc, "3.2 Fully Dressed Use Cases (≥8)", 2)
    add_p(
        doc,
        "Each use case uses the synchronized Field | Content table template (same columns as Phước UC-05). "
        "Wireframe SCR references are listed in Other Information / §5.1 as file paths only — images not embedded.",
        italic=True,
    )
    uc_list = [
        ("3.2.1 UC-05 — Register Membership (at Counter)", "UC-05.md"),
        ("3.2.2 UC-06 — Activate Membership", "UC-06.md"),
        ("3.2.3 UC-08 — Check-in by QR", "UC-08.md"),
        ("3.2.4 UC-11 — Book a PT Package", "UC-11.md"),
        ("3.2.5 UC-12 — Confirm / Reject PT Booking", "UC-12.md"),
        ("3.2.6 UC-15 — Record Training Session", "UC-15.md"),
        ("3.2.7 UC-16 — Register PT Account", "UC-16.md"),
        ("3.2.8 UC-17 — Approve / Reject PT", "UC-17.md"),
    ]
    for title, md_name in uc_list:
        add_heading(doc, title, 3)
        rows = parse_uc_field_table(ROOT / "docs" / "step4" / md_name)
        if not rows:
            add_note(doc, f"Cannot parse Field|Content table from docs/step4/{md_name}")
            continue
        # strip UI image emphasis from Other Information for clarity
        cleaned = []
        for k, v in rows:
            if k == "Other Information":
                v = re.sub(r"03_Images/UI_[^\s|]+", "(wireframe path in docs/step5 — not embedded)", v)
            cleaned.append((k, v))
        add_table(doc, ["Field", "Content"], cleaned)

    add_heading(doc, "3.3 Other use cases (brief)", 2)
    add_p(
        doc,
        "Remaining catalogue UCs: docs/02_UC_List_Detailed.md (brief only unless later fully dressed).",
    )

    add_heading(doc, "3.4 Behaviour models — Activity & State", 2)
    try_vp_picture(
        doc,
        "AD_ActivateMembership.png",
        caption="Figure 3.5 — AD-03 Activate Membership at Counter",
        note="VP swimlane. UC-05/06. Owners: Phước+Thiên #32.",
    )
    try_vp_picture(
        doc,
        "AD_ApprovePT.png",
        caption="Figure 3.6 — AD-02 Register & Approve PT",
        note="VP swimlane. UC-16/17. Owner: Huy #31.",
    )
    add_note(
        doc,
        "Figure 3.7 AD-01 Book PT (AD_BookPT.png) — MISSING. Tuấn #30 must draw in Visual Paradigm and export PNG.",
    )
    add_note(
        doc,
        "Figure 3.8–3.9 SMD-01/SMD-02 — MISSING VP PNG (SMD_Membership.png, SMD_PTBooking.png). "
        "Thiên #34: export from GMS.vpp. Transition tables: docs/step7/thien_smd.md.",
    )
    add_p(doc, "SMD-01 key transitions (until PNG available)", italic=True)
    add_table(
        doc,
        ["ID", "Event", "Type", "Target", "UC/BR"],
        [
            ["T1", "registerMembership", "UC", "Inactive", "UC-05"],
            ["T2", "activate", "UC", "Active", "UC-06"],
            ["T5", "when(current_date > end_date)", "Time", "Expired", "UC-27, BR-11"],
            ["T6", "suspend", "Owner", "Suspended", "BR-04"],
        ],
    )
    add_p(doc, "SMD-02 key transitions (until PNG available)", italic=True)
    add_table(
        doc,
        ["ID", "Event", "Type", "Target", "UC/BR"],
        [
            ["T1", "bookPTPackage", "UC", "Pending", "UC-11"],
            ["T2", "confirmBooking", "UC", "Confirmed", "UC-12"],
            ["T4", "after(24h)", "Time", "Cancelled", "BR-08"],
            ["T6+", "recordSession", "UC", "In Progress/Completed", "UC-15"],
        ],
    )

    add_heading(doc, "3.5 Functional Requirements (sample)", 2)
    add_table(
        doc,
        ["ID", "Requirement", "Trace", "Priority"],
        [
            ["FR-05-01", "System shall create Membership INACTIVE after counter registration", "UC-05", "H"],
            ["FR-06-01", "System shall set ACTIVE and generate QR when fee fully paid", "UC-06", "H"],
            ["FR-08-01", "System shall validate QR and open-hours before CheckInLog", "UC-08", "H"],
            ["FR-11-01", "System shall create Pending booking after successful payment", "UC-11", "H"],
            ["FR-12-01", "System shall allow Confirm/Reject within 24h with refund rules", "UC-12", "H"],
            ["FR-15-01", "System shall decrement remaining sessions on record", "UC-15", "H"],
            ["FR-16-01", "System shall accept PT registration as Pending approval", "UC-16", "H"],
            ["FR-17-01", "Owner shall Approve/Reject PT with reason on reject", "UC-17", "H"],
        ],
    )

    # ---- 4 ----
    add_heading(doc, "4. Data Requirements", 1)
    add_heading(doc, "4.1 Logical Data Model", 2)
    try_vp_picture(
        doc,
        "ERD_Conceptual.png",
        caption="Figure 4.1 — ERD-01 Conceptual Data Model of GMS",
        note="VP conceptual ERD. Owner: Huy #35. Dictionary: docs/step7/huy_erd.md",
    )
    add_table(
        doc,
        ["Vision name", "Huy ERD entity"],
        [
            ["Customer", "Member (+ Account)"],
            ["Gym Owner", "Gym_Owner"],
            ["Personal Trainer", "Personal_trainer"],
            ["Membership", "Customer_Membership"],
            ["PTBooking", "Booking"],
            ["CheckInLog", "Check_In"],
        ],
    )
    add_heading(doc, "4.2 Data Dictionary", 2)
    add_p(doc, "Full attribute tables: docs/step7/huy_erd.md §2.", italic=True)
    add_table(
        doc,
        ["Entity", "Key attributes", "Notes"],
        [
            ["Account", "accountID, UserName, Password_Hash, Status, RoleID", "NFR-SEC-01"],
            ["Customer_Membership", "EnrollmentID, Start/ExpireDate, Status", "SMD-01"],
            ["Booking", "Booking_ID, DateTime, Status, PT, Member", "SMD-02"],
            ["Check_In", "CheckIN_ID, DateTime, Method, Member", "UC-08"],
            ["Payment", "PaymentID, Amount, Method, Status", "Gateway/cash"],
        ],
    )
    add_heading(doc, "4.3 Reports", 2)
    add_table(
        doc,
        ["ID", "Name", "User", "Sources"],
        [
            ["RPT-01", "Revenue summary", "Gym Owner", "Payment, Membership, Booking"],
            ["RPT-02", "Check-in statistics", "Gym Owner", "Check_In"],
            ["RPT-03", "PT performance", "Gym Owner", "Booking"],
        ],
    )
    add_heading(doc, "4.4 Collection, Integrity, Retention", 2)
    add_p(
        doc,
        "Collection: UC-05/06, booking/QR, gateway callbacks, scheduler. Integrity: BR-02/04. "
        "Retention draft: logs ≥ 12 months.",
    )

    # ---- 5 ----
    add_heading(doc, "5. External Interface Requirements", 1)
    add_heading(doc, "5.1 User Interfaces", 2)
    add_p(
        doc,
        "Wireframes are produced with Figma/Stitch/draw.io (not Visual Paradigm). Per team rule for this SRS revision, "
        "UI PNG files are NOT attached. Screen IDs and paths for reference:",
    )
    add_table(
        doc,
        ["SCR", "UC", "Reference path (not embedded)", "Owner"],
        [
            ["SCR-05", "UC-05", "docs/step5 + 03_Images/UI_UC-05_*", "Phước"],
            ["SCR-06", "UC-06", "03_Images/UI_UC-06_*", "Phước"],
            ["SCR-08", "UC-08", "03_Images/UI_UC-08_*", "Thiên"],
            ["SCR-11", "UC-11", "03_Images/UI_UC11_BookPT.png", "Tuấn"],
            ["SCR-12", "UC-12", "03_Images/UI_UC12_PTBooking.png", "Tuấn"],
            ["SCR-15", "UC-15", "03_Images/UI_UC-15_*", "Thiên"],
            ["SCR-16", "UC-16", "03_Images/UI_UC-16_RegisterPT.png", "Huy"],
            ["SCR-17", "UC-17", "03_Images/UI_UC-17_ApprovePT.png", "Huy"],
        ],
    )
    add_heading(doc, "5.2 Software Interfaces", 2)
    add_p(doc, "Payment Gateway REST; SMS API; QR module; relational DBMS.")
    add_heading(doc, "5.3 Hardware Interfaces", 2)
    add_p(
        doc,
        "Không áp dụng thiết bị chuyên dụng — Release 1 dùng camera điện thoại/tablet tiêu chuẩn để quét QR.",
    )
    add_heading(doc, "5.4 Communications Interfaces", 2)
    add_p(doc, "HTTPS; SMS provider; payment callbacks over TLS.")

    # ---- 6-8 ----
    add_heading(doc, "6. Quality Attributes", 1)
    add_table(
        doc,
        ["NFR-ID", "Description", "Measurement", "Target"],
        [
            ["NFR-PERF-01", "Lookup/check-in under load", "JMeter @100 concurrent", "Avg ≤1.5s; max ≤3s"],
            ["NFR-SEC-01", "Password hashing", "Inspect Account store", "BCrypt ≥10; no plaintext"],
            ["NFR-SEC-02", "Session timeout", "Idle test", "Logout @15 min"],
            ["NFR-USAB-01", "Receptionist core task", "UAT 5 users", "100% <30s"],
            ["NFR-REL-01", "Daily backup", "Verify schedule", "Daily full backup"],
        ],
    )
    add_heading(doc, "7. Internationalization and Localization Requirements", 1)
    add_p(doc, "UI Vietnamese; dates dd/mm/yyyy; VND; UTC+7; SRS/model names English.")
    add_heading(doc, "8. Other Requirements", 1)
    add_p(doc, "Decree 13/2023 compliance; short front-desk guidance; no thick desktop client in R1.")

    # ---- Appendices ----
    add_heading(doc, "Appendix A – Glossary", 1)
    add_table(
        doc,
        ["Term", "Definition"],
        [
            ["Membership", "Customer–package contract (SMD-01)"],
            ["QR Membership", "Token valid while ACTIVE (BR-04)"],
            ["PT Booking", "PT package order (SMD-02)"],
            ["Pending Booking", "Awaiting PT confirm ≤24h (BR-08)"],
            ["Check-in", "Gate event via QR validation"],
        ],
    )
    add_heading(doc, "Appendix B – Analysis Models (VP only in SRS)", 1)
    add_table(
        doc,
        ["ID", "Name", "File", "In SRS?", "Status"],
        [
            ["CD-01", "Context", "CD_ContextDiagram.png", "Yes", "VP"],
            ["UCD-01", "Overview", "UCD_Overview.png", "Yes", "VP"],
            ["UCD-pkg", "Membership/PT/Report", "UCD_*.png drafts", "No", "Redraw in VP"],
            ["AD-01", "Book PT", "AD_BookPT.png", "No", "MISSING Tuấn"],
            ["AD-02", "Approve PT", "AD_ApprovePT.png", "Yes", "VP"],
            ["AD-03", "Activate Membership", "AD_ActivateMembership.png", "Yes", "VP"],
            ["SMD-01/02", "Lifecycles", "SMD_*.png", "No", "MISSING Thiên"],
            ["ERD-01", "Conceptual", "ERD_Conceptual.png", "Yes", "VP"],
            ["UI", "Wireframes", "UI_*.png", "No", "Not VP — path only"],
        ],
    )
    add_heading(doc, "Appendix C – Traceability Matrix", 1)
    add_p(doc, "File: 04_Traceability_Matrix.xlsx (Traceability + NFR). Also docs/step7/phuoc_srs_trace.md.")
    add_heading(doc, "Appendix D – Open Issues", 1)
    add_table(
        doc,
        ["ID", "Gap", "Owner"],
        [
            ["OI-01", "AD-01 VP PNG", "Tuấn #30"],
            ["OI-02", "SMD-01/02 VP PNG", "Thiên #34"],
            ["OI-03", "Package UCD redraw in VP (replace PlantUML drafts)", "Thiên/Tuấn/Huy"],
            ["OI-04", "Instructor / class code on cover", "Phước"],
        ],
    )
    add_heading(doc, "Appendix F – Figure catalogue (embedded = VP only)", 1)
    add_table(
        doc,
        ["Figure", "File", "Embedded", "Note"],
        [
            ["2.1", "CD_ContextDiagram.png", "Yes", "VP"],
            ["3.1", "UCD_Overview.png", "Yes", "VP"],
            ["3.5", "AD_ActivateMembership.png", "Yes", "VP AD-03"],
            ["3.6", "AD_ApprovePT.png", "Yes", "VP AD-02"],
            ["3.7", "AD_BookPT.png", "No", "Wait Tuấn"],
            ["3.8–3.9", "SMD_*.png", "No", "Wait Thiên"],
            ["4.1", "ERD_Conceptual.png", "Yes", "VP"],
            ["—", "UI_*.png / UCD package drafts", "No", "Not VP / PlantUML"],
        ],
    )

    # Final pass: force all runs to black/size where possible
    for p in doc.paragraphs:
        if p.style and p.style.name.startswith("Heading"):
            for run in p.runs:
                run.font.color.rgb = BLACK
                run.font.name = "Times New Roman"

    doc.save(OUT)
    print("Wrote", OUT, "VP images only; UC Field|Content; font 13; black headings")


if __name__ == "__main__":
    build()
