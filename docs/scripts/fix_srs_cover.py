# -*- coding: utf-8 -*-
"""Rebuild a professional cover page for 01_SRS_GMS.docx (page 1), keep body after Revision History."""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Cm
from docx.text.paragraph import Paragraph

BLACK = RGBColor(0, 0, 0)
GRAY = RGBColor(0x55, 0x55, 0x55)
NOTE = RGBColor(0x33, 0x33, 0x33)
DOC = "01_SRS_GMS.docx"


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


class Cursor:
    def __init__(self, ref):
        self.ref = ref
        self.last = None

    def insert(self, el):
        if self.last is None:
            self.ref.addprevious(el)
        else:
            self.last.addnext(el)
        self.last = el
        return el


def main():
    doc = Document(DOC)
    rev_el = None
    for p in doc.paragraphs:
        if p.text.strip() == "Revision History" and p.style.name.startswith("Heading"):
            rev_el = p._element
            break
    if rev_el is None:
        raise SystemExit("Revision History heading not found")

    body = doc.element.body
    for child in list(body):
        if child is rev_el:
            break
        if child.tag.endswith("}sectPr"):
            continue
        body.remove(child)

    cur = Cursor(rev_el)

    def para(
        text="",
        size=13,
        bold=False,
        italic=False,
        align="center",
        before=0,
        after=6,
        color=BLACK,
    ):
        new_p = OxmlElement("w:p")
        cur.insert(new_p)
        p = Paragraph(new_p, doc._body)
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        if align == "center":
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif align == "left":
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if text:
            r = p.add_run(text)
            set_run(r, size=size, bold=bold, italic=italic, color=color)
        return p

    # --- Cover (page 1) ---
    para("FPT UNIVERSITY", size=15, bold=True, before=48, after=2)
    para("Trường Đại học FPT", size=12, italic=True, after=8)
    para("DEPARTMENT OF SOFTWARE ENGINEERING", size=11, bold=True, after=2)
    para("Course: SWR302 — Software Requirement", size=12, after=2)
    para("Semester: FALL 2026", size=12, after=18)
    para("─" * 42, size=12, before=2, after=10)

    para("SOFTWARE REQUIREMENTS SPECIFICATION", size=18, bold=True, before=6, after=4)
    para("Đặc tả yêu cầu phần mềm", size=13, italic=True, after=16)
    para("SYSTEM", size=10, bold=True, after=2)
    para("GMS — Gym Management System", size=16, bold=True, after=12)
    para("─" * 42, size=12, before=2, after=10)

    para("Document control", size=12, bold=True, align="left", before=2, after=6)
    para("Version:  1.0-draft", size=13, align="left", after=2)
    para("Group:    GroupOfFour", size=13, align="left", after=2)
    para("Class:    SWR302 (FALL 2026)", size=13, align="left", after=2)
    para("Date:     11/11/2026", size=13, align="left", after=10)

    para("Project team", size=12, bold=True, align="left", before=2, after=6)

    table = doc.add_table(rows=5, cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    data = [
        ("Role", "Full name", "Student ID"),
        ("Leader", "Văn Xuân Phước", "DE190430"),
        ("Member", "Nguyễn Anh Tuấn", "DE201152"),
        ("Member", "Nguyễn Ngô Tâm Thiên", "DE190385"),
        ("Member", "Đặng Nguyễn Huy", "DE201171"),
    ]
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            cell = table.rows[i].cells[j]
            cell.text = ""
            cp = cell.paragraphs[0]
            r = cp.add_run(val)
            set_run(r, size=12, bold=(i == 0))
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tbl = table._tbl
    body.remove(tbl)
    cur.insert(tbl)

    para("", after=6)
    para("Instructor / Giảng viên hướng dẫn", size=12, bold=True, align="left", before=10, after=4)
    para("Name: ____________________________________________", size=13, align="left", after=14)
    para(
        "FPT University  ·  SWR302  ·  GroupOfFour",
        size=10,
        italic=True,
        before=20,
        after=4,
        color=GRAY,
    )

    # Page break
    pb = OxmlElement("w:p")
    cur.insert(pb)
    run = Paragraph(pb, doc._body).add_run()
    br = OxmlElement("w:br")
    br.set(qn("w:type"), "page")
    run._element.append(br)

    para(
        "[NOTE] Chỉ nhúng sơ đồ Visual Paradigm (CD / UCD Overview / AD / ERD). "
        "Wireframe UI và PlantUML draft không đính kèm.",
        size=11,
        italic=True,
        align="left",
        before=0,
        after=10,
        color=NOTE,
    )

    sec = doc.sections[0]
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(2.0)
    sec.left_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)

    doc.save(DOC)
    print("Cover OK:", DOC)


if __name__ == "__main__":
    main()
