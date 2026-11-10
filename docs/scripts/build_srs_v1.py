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


FONT = "Times New Roman"
SIZE = Pt(13)
UC_FIELDS = [
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

# Only Visual Paradigm exports may be embedded (no wireframe UI, no PlantUML drafts)
VP_ALLOWED = {
    "CD_ContextDiagram.png",
    "UCD_Overview.png",
    "UCD_Membership.png",  # allow when re-exported from VPP (current repo copy is draft — not inserted in build)
    "UCD_PT.png",
    "UCD_Report_Feedback.png",
    "AD_ActivateMembership.png",
    "AD_ApprovePT.png",
    "AD_BookPT.png",
    "SMD_Membership.png",
    "SMD_PTBooking.png",
    "ERD_Conceptual.png",
}


def _force_run_font(run, size=SIZE, bold=None, italic=None, color=None):
    run.font.name = FONT
    run.font.size = size
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii", FONT)
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi", FONT)
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}eastAsia", FONT)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    else:
        run.font.color.rgb = RGBColor(0, 0, 0)


def set_doc_defaults(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = FONT
    style.font.size = SIZE
    style.font.color.rgb = RGBColor(0, 0, 0)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii", FONT)
    rFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi", FONT)
    # Headings: black, Times New Roman (no theme blue)
    sizes = {1: Pt(16), 2: Pt(14), 3: Pt(13)}
    for level, sz in sizes.items():
        hs = doc.styles[f"Heading {level}"]
        hs.font.name = FONT
        hs.font.size = sz
        hs.font.bold = True
        hs.font.color.rgb = RGBColor(0, 0, 0)
        hrPr = hs.element.get_or_add_rPr()
        hrFonts = hrPr.get_or_add_rFonts()
        hrFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii", FONT)
        hrFonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi", FONT)
        # clear theme color if present
        color_el = hrPr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color")
        if color_el is not None:
            hrPr.remove(color_el)
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn

        c = OxmlElement("w:color")
        c.set(qn("w:val"), "000000")
        hrPr.append(c)


def add_heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        _force_run_font(run, size={1: Pt(16), 2: Pt(14), 3: Pt(13)}.get(level, SIZE), bold=True, color=RGBColor(0, 0, 0))
    return h


def add_p(doc, text="", bold=False, italic=False, size=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    sz = SIZE if size is None else (Pt(size) if isinstance(size, int) else size)
    _force_run_font(run, size=sz, bold=bold, italic=italic)
    return p


def add_note(doc, text):
    p = doc.add_paragraph()
    run = p.add_run("[MISSING / TODO] " + text)
    _force_run_font(run, size=SIZE, bold=True, color=RGBColor(0xC0, 0x39, 0x2B))
    return p


def _set_cell_font(cell):
    for p in cell.paragraphs:
        for run in p.runs:
            _force_run_font(run, size=SIZE, color=RGBColor(0, 0, 0))
        if not p.runs and p.text:
            p.text = p.text
            for run in p.runs:
                _force_run_font(run, size=SIZE, color=RGBColor(0, 0, 0))


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        _force_run_font(run, size=SIZE, bold=True, color=RGBColor(0, 0, 0))
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            cell = table.rows[r_i + 1].cells[c_i]
            cell.text = ""
            run = cell.paragraphs[0].add_run(str(val) if val is not None else "")
            _force_run_font(run, size=SIZE, color=RGBColor(0, 0, 0))
    doc.add_paragraph()
    return table


def try_picture(doc, path: Path, width=5.8, caption=None, note=None):
    """Insert VP diagram only. Reject UI wireframes / PlantUML drafts."""
    if path.name not in VP_ALLOWED:
        add_note(
            doc,
            f"Không nhúng {path.name} — chỉ đính kèm sơ đồ Visual Paradigm (không wireframe UI / nháp PlantUML). "
            + (note or ""),
        )
        return False
    if path.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))
        if caption:
            cap = doc.add_paragraph()
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = cap.add_run(caption)
            _force_run_font(r, size=SIZE, bold=True, italic=True)
        note_bits = [f"Source file: 03_Images/{path.name}", "Visual Paradigm export", "≥150 dpi (A.3)"]
        if note:
            note_bits.insert(1, note)
        n = doc.add_paragraph()
        n.alignment = WD_ALIGN_PARAGRAPH.CENTER
        nr = n.add_run(" · ".join(note_bits))
        _force_run_font(nr, size=Pt(11), italic=True, color=RGBColor(0x33, 0x33, 0x33))
        return True
    add_note(doc, f"Chưa có ảnh VP — cần file: 03_Images/{path.name}" + (f" | {note}" if note else ""))
    return False


def parse_md_field_table(path: Path) -> dict[str, str]:
    """Parse Field|Content exam table into dict keyed by canonical field name."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    data: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(parts) < 2:
            continue
        key = re.sub(r"\*+", "", parts[0]).strip()
        val = parts[1].replace("<br>", " ").replace("<br/>", " ")
        if not key or key.lower() in {"field", "item"} or set(key) <= {"-", ":"}:
            continue
        if parts[1].startswith("---"):
            continue
        data[key] = val
    return data


def uc_rows_for_srs(path: Path) -> list[list[str]]:
    """Return Field|Content rows in Phước exam order for SRS."""
    data = parse_md_field_table(path)
    # alias map
    aliases = {
        "Post conditions": ["Post conditions", "Postconditions", "Post condition"],
        "Normal Flow": ["Normal Flow", "Main success scenario"],
        "Alternative Flows": ["Alternative Flows", "Alternative flows"],
        "Exceptions": ["Exceptions", "Exception flows"],
        "Secondary Actors": ["Secondary Actors", "Secondary actors"],
        "Primary Actor": ["Primary Actor", "Primary actor"],
        "Business Rules": ["Business Rules", "Related business rules"],
    }
    rows = []
    for field in UC_FIELDS:
        val = data.get(field, "")
        if not val:
            for alt in aliases.get(field, []):
                if alt in data:
                    val = data[alt]
                    break
        rows.append([field, val or "—"])
    return rows


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def finalize_fonts(doc: Document) -> None:
    """Force black + TNR 13 on body; headings black."""
    for p in doc.paragraphs:
        style_name = p.style.name if p.style else ""
        if style_name.startswith("Heading"):
            level = int(style_name[-1]) if style_name[-1].isdigit() else 1
            sz = {1: Pt(16), 2: Pt(14), 3: Pt(13)}.get(level, SIZE)
            for run in p.runs:
                _force_run_font(run, size=sz, bold=True, color=RGBColor(0, 0, 0))
        else:
            for run in p.runs:
                # keep missing notes red
                if run.text.startswith("[MISSING"):
                    _force_run_font(run, size=SIZE, bold=True, color=RGBColor(0xC0, 0x39, 0x2B))
                elif run.font.size is None or run.font.size < Pt(13):
                    col = run.font.color.rgb if run.font.color and run.font.color.rgb else RGBColor(0, 0, 0)
                    _force_run_font(run, size=SIZE, color=col if col != RGBColor(0xC0, 0x39, 0x2B) else RGBColor(0, 0, 0))
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        _force_run_font(run, size=SIZE, color=RGBColor(0, 0, 0))


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
                "Assemble from docs/step*; UC Field|Content sync; VP-only figures; font 13 / black headings",
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
        "Font: Times New Roman **13 pt** (body); headings black (no theme color). "
        "IDs: BO-xx, BR-xx, UC-xx, FR-xx, NFR-<TYPE>-xx, SCR-xx, CD/UCD/AD/SMD/ERD-xx. "
        "Priority: High / Medium / Low. Keywords: shall / should / may. "
        "End-user UI: Vietnamese; SRS body: English. "
        "Fully dressed UC template: two-column Field | Content table (see UC-05). "
        "Diagrams embedded in this SRS: Visual Paradigm exports only (no wireframe UI, no PlantUML drafts). "
        "Canonical BR: Vision BR-01…BR-12 in §2.6.",
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
    try_picture(
        doc,
        IMG / "CD_ContextDiagram.png",
        caption="Figure 2.1 — CD-01 Context Diagram of the Gym Management System (GMS)",
        note="1 process center; ≥5 external entities; ≥12 noun-named data flows. Owner: Phước #10. Peer note (#42): fix typo labels on VPP re-export.",
    )
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
    try_picture(
        doc,
        IMG / "UCD_Overview.png",
        width=5.5,
        caption="Figure 3.1 — UCD-01 Use Case Overview of GMS",
        note="Actors + high-priority UCs; generalization User←Customer/PT/Owner. Owner: Phước #15.",
    )
    add_p(doc, "Package diagrams (Step 3) — Visual Paradigm only", bold=True)
    add_note(
        doc,
        "Figure 3.2 UCD Membership / 3.3 UCD PT / 3.4 UCD Report-Feedback: các PNG hiện có trong repo "
        "là nháp PlantUML (02_Models/*.puml) hoặc draft — KHÔNG nhúng vào SRS. "
        "Cần export lại từ GMS.vpp → 03_Images/UCD_Membership.png, UCD_PT.png, UCD_Report_Feedback.png.",
    )

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

    # Fully dressed UCs — unified Field | Content table (Phước exam template)
    add_heading(doc, "3.2 Fully Dressed Use Cases (≥8)", 2)
    add_p(
        doc,
        "Mỗi UC dưới đây dùng cùng một bảng Field | Content (đồng bộ template UC-05). "
        "Wireframe UI (Figma/Stitch/draw.io) chỉ tham chiếu đường dẫn file — không nhúng vào SRS "
        "(SRS chỉ đính kèm sơ đồ Visual Paradigm).",
        italic=True,
    )
    uc_files = [
        ("3.2.1 UC-05 Register Membership (at Counter)", "UC-05.md", "SCR-05", "03_Images/UI_UC-05_RegisterMembership.png"),
        ("3.2.2 UC-06 Activate Membership", "UC-06.md", "SCR-06", "03_Images/UI_UC-06_ActivateMembership.png"),
        ("3.2.3 UC-08 Check-in by QR", "UC-08.md", "SCR-08", "03_Images/UI_UC-08_QRCheckIn.png"),
        ("3.2.4 UC-11 Book a PT Package", "UC-11.md", "SCR-11", "03_Images/UI_UC11_BookPT.png"),
        ("3.2.5 UC-12 Confirm / Reject PT Booking", "UC-12.md", "SCR-12", "03_Images/UI_UC12_PTBooking.png"),
        ("3.2.6 UC-15 Record Training Session", "UC-15.md", "SCR-15", "03_Images/UI_UC-15_RecordSession.png"),
        ("3.2.7 UC-16 Register PT Account", "UC-16.md", "SCR-16", "03_Images/UI_UC-16_RegisterPT.png"),
        ("3.2.8 UC-17 Approve / Reject PT", "UC-17.md", "SCR-17", "03_Images/UI_UC-17_ApprovePT.png"),
    ]
    for title, md_name, scr, ui_path in uc_files:
        add_heading(doc, title, 3)
        md_path = ROOT / "docs" / "step4" / md_name
        rows = uc_rows_for_srs(md_path)
        if all(r[1] == "—" for r in rows):
            add_note(doc, f"{md_name} incomplete or wrong template")
        else:
            add_table(doc, ["Field", "Content"], rows)
        add_p(doc, f"UI reference (not embedded): {scr} → `{ui_path}` — see docs/step5 for field tables.", italic=True)

    add_heading(doc, "3.3 Other use cases (brief)", 2)
    add_p(
        doc,
        "Brief descriptions for remaining catalogue UCs (UC-01…04, 07, 09–10, 13–14, 18–28) are listed in "
        "docs/02_UC_List_Detailed.md. Fully dressed elaboration beyond the eight High UCs is out of Release-1 "
        "documentation depth unless expanded later.",
    )

    add_heading(doc, "3.4 Behaviour models — Activity & State", 2)
    add_p(doc, "AD-03 Activate Membership at counter (Phước+Thiên #32)", bold=True)
    try_picture(
        doc,
        IMG / "AD_ActivateMembership.png",
        caption="Figure 3.5 — AD-03 Activate Membership at Counter (swimlane)",
        note="≥3 lanes (Owner / GMS / Customer|SMS). Related UC-05/06. Owners: Phước+Thiên #32.",
    )
    add_p(doc, "AD-02 Approve PT (Huy #31)", bold=True)
    try_picture(
        doc,
        IMG / "AD_ApprovePT.png",
        caption="Figure 3.6 — AD-02 Register & Approve Personal Trainer (swimlane)",
        note="Lanes PT / GMS / Owner. Related UC-16/17. Owner: Huy #31.",
    )
    add_p(doc, "AD-01 Book PT & payment (Tuấn #30)", bold=True)
    try_picture(
        doc,
        IMG / "AD_BookPT.png",
        caption="Figure 3.7 — AD-01 Book PT Package & Payment (swimlane)",
        note="Expected file AD_BookPT.png · Related UC-11/12 · Owner: Tuấn #30.",
    )
    add_note(
        doc,
        "AD-01 CHƯA CÓ — issue #30 OPEN; docs/step6/tuan_ad01.md trống. Blocker checklist bước 6 #33.",
    )

    add_p(doc, "SMD-01 Membership & SMD-02 PT Booking (Thiên #34)", bold=True)
    try_picture(
        doc,
        IMG / "SMD_Membership.png",
        caption="Figure 3.8 — SMD-01 Membership Lifecycle",
        note="States Inactive/Active/Suspended/Expired/Cancelled + Time events. Owner: Thiên #34.",
    )
    try_picture(
        doc,
        IMG / "SMD_PTBooking.png",
        caption="Figure 3.9 — SMD-02 PT Booking Lifecycle",
        note="States Pending…Cancelled; Time after(24h)=BR-08. Owner: Thiên #34.",
    )
    add_note(
        doc,
        "PNG SMD chưa export từ VP — chèn bảng transition bên dưới từ docs/step7/thien_smd.md cho đến khi có hình.",
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
    try_picture(
        doc,
        IMG / "ERD_Conceptual.png",
        caption="Figure 4.1 — ERD-01 Conceptual Data Model of GMS (≥10 entities)",
        note="Converted/normalized from Entity Relationship Diagram1.jpg · Owner: Huy #35 · Dict: docs/step7/huy_erd.md",
    )
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
    add_p(
        doc,
        "Style: Vietnamese labels on UI; English IDs in SRS. Field/validation tables: docs/step5/*_ui.md. "
        "Huy NFR-USAB-01: core reception tasks < 30s for new users. "
        "Wireframe PNG are kept in 03_Images/ for the submission zip / appendix, but are NOT embedded "
        "in this SRS document (only Visual Paradigm diagrams are embedded).",
    )
    add_p(doc, "Screen map (wireframe file references — not embedded)", bold=True)
    add_table(
        doc,
        ["SCR", "UC", "PNG path", "Owner"],
        [
            ["SCR-05", "UC-05", "03_Images/UI_UC-05_RegisterMembership.png (+_Error)", "Phước"],
            ["SCR-06", "UC-06", "03_Images/UI_UC-06_ActivateMembership.png (+_Error)", "Phước"],
            ["SCR-08", "UC-08", "03_Images/UI_UC-08_QRCheckIn.png (+_Error)", "Thiên"],
            ["SCR-11", "UC-11", "03_Images/UI_UC11_BookPT.png", "Tuấn"],
            ["SCR-12", "UC-12", "03_Images/UI_UC12_PTBooking.png", "Tuấn"],
            ["SCR-15", "UC-15", "03_Images/UI_UC-15_RecordSession.png (+_Error)", "Thiên"],
            ["SCR-16", "UC-16", "03_Images/UI_UC-16_RegisterPT.png", "Huy"],
            ["SCR-17", "UC-17", "03_Images/UI_UC-17_ApprovePT.png", "Huy"],
        ],
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

    add_heading(doc, "Appendix F – Figure catalogue & image notes", 1)
    add_p(
        doc,
        "Chính sách hình trong SRS: chỉ nhúng sơ đồ xuất từ Visual Paradigm (.vpp). "
        "Không nhúng wireframe UI (Figma/Stitch/draw.io) và không nhúng nháp PlantUML. "
        "Wireframe vẫn nằm trong 03_Images/ để nộp zip A.3 riêng.",
    )
    add_table(
        doc,
        ["Figure", "File", "Type", "SRS §", "Status", "Note"],
        [
            ["2.1", "CD_ContextDiagram.png", "CD", "2.1", "Embedded (VP)", "Fix typo labels on re-export (#42)"],
            ["3.1", "UCD_Overview.png", "UCD", "3.1", "Embedded (VP)", "Overview"],
            ["3.2", "UCD_Membership.png", "UCD", "3.1", "Not embedded", "PlantUML/draft — re-export from VPP"],
            ["3.3", "UCD_PT.png", "UCD", "3.1", "Not embedded", "PlantUML/draft — re-export from VPP"],
            ["3.4", "UCD_Report_Feedback.png", "UCD", "3.1", "Not embedded", "Explicit draft from .puml (Huy)"],
            ["3.5", "AD_ActivateMembership.png", "AD", "3.4", "Embedded (VP)", "AD-03"],
            ["3.6", "AD_ApprovePT.png", "AD", "3.4", "Embedded (VP)", "AD-02"],
            ["3.7", "AD_BookPT.png", "AD", "3.4", "MISSING", "Tuấn #30"],
            ["3.8", "SMD_Membership.png", "SMD", "3.4", "MISSING", "Thiên #34 — tables in §3.4"],
            ["3.9", "SMD_PTBooking.png", "SMD", "3.4", "MISSING", "Thiên #34"],
            ["4.1", "ERD_Conceptual.png", "ERD", "4.1", "Embedded (VP)", "Huy #35"],
            ["—", "UI_UC-*", "Wireframe", "5.1 ref only", "Not embedded", "UI tools — file path only"],
        ],
    )
    add_p(doc, "Image notes", bold=True)
    add_p(
        doc,
        "Mỗi hình VP được nhúng có caption Figure + dòng Source (file, VP export, ≥150 dpi). "
        "Hình MISSING giữ số Figure để bổ sung sau.",
    )

    finalize_fonts(doc)
    doc.save(OUT)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
