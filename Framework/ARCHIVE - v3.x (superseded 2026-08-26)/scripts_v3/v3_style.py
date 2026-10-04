# -*- coding: utf-8 -*-
"""Shared house style for the Framework v3.0 document set.
Navy/gold identity, rule cards, callouts, source tags, three-class source
labeling (LEDGER / CONVENTION / FIELD AMENDMENT), numbered pages."""
import glob
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

# ---------- palette ----------
NAVY = colors.HexColor("#17365D")
NAVY_DARK = colors.HexColor("#0F2440")
GOLD = colors.HexColor("#BF9B30")
GOLD_PALE = colors.HexColor("#F7F0DC")
INK = colors.HexColor("#1A1A1A")
GRAY = colors.HexColor("#5A5A5A")
PALE = colors.HexColor("#F4F4F0")
RULE_BG = colors.HexColor("#EDF0F5")

# ---------- fonts ----------
def _register_dejavu():
    try:
        import matplotlib
        p = os.path.join(os.path.dirname(matplotlib.__file__),
                         "mpl-data", "fonts", "ttf")
        pdfmetrics.registerFont(TTFont("DejaVuSans", os.path.join(p, "DejaVuSans.ttf")))
        pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", os.path.join(p, "DejaVuSans-Bold.ttf")))
        return True
    except Exception:
        return False

HAS_DEJAVU = _register_dejavu()
CHECK = '<font name="DejaVuSans">☐</font>' if HAS_DEJAVU else "[ ]"

# ---------- paragraph styles ----------
def styles():
    s = {}
    s["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24,
                                leading=29, textColor=NAVY, alignment=1)
    s["subtitle"] = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=12,
                                   leading=16, textColor=GRAY, alignment=1)
    s["edition"] = ParagraphStyle("edition", fontName="Helvetica-Bold", fontSize=11,
                                  leading=14, textColor=GOLD, alignment=1)
    s["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16,
                             leading=20, textColor=NAVY, spaceBefore=14, spaceAfter=8)
    s["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5,
                             leading=16, textColor=NAVY, spaceBefore=10, spaceAfter=5)
    s["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5,
                             leading=13.5, textColor=NAVY_DARK, spaceBefore=8, spaceAfter=3)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5,
                               leading=13.2, textColor=INK, spaceAfter=6)
    s["bullet"] = ParagraphStyle("bullet", parent=s["body"], leftIndent=14,
                                 bulletIndent=4, spaceAfter=3.5)
    s["quote"] = ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=9.5,
                                leading=13.4, textColor=NAVY_DARK, leftIndent=16,
                                rightIndent=10, spaceBefore=3, spaceAfter=2)
    s["source"] = ParagraphStyle("source", fontName="Helvetica", fontSize=7.6,
                                 leading=10, textColor=GRAY, leftIndent=16, spaceAfter=7)
    s["cardtitle"] = ParagraphStyle("cardtitle", fontName="Helvetica-Bold", fontSize=10,
                                    leading=13, textColor=colors.white)
    s["cardbody"] = ParagraphStyle("cardbody", parent=s["body"], spaceAfter=3)
    s["tag"] = ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=7.6,
                              leading=10, textColor=GOLD)
    s["small"] = ParagraphStyle("small", fontName="Helvetica", fontSize=8.2,
                                leading=11, textColor=GRAY, spaceAfter=4)
    s["epigraph"] = ParagraphStyle("epigraph", fontName="Helvetica-Oblique", fontSize=10.5,
                                   leading=15, textColor=NAVY_DARK, alignment=1,
                                   leftIndent=40, rightIndent=40, spaceBefore=10, spaceAfter=4)
    s["epigraphsrc"] = ParagraphStyle("epigraphsrc", parent=s["source"], alignment=1,
                                      leftIndent=0)
    s["formlabel"] = ParagraphStyle("formlabel", fontName="Helvetica-Bold", fontSize=9,
                                    leading=12, textColor=INK, spaceAfter=2)
    s["formline"] = ParagraphStyle("formline", fontName="Helvetica", fontSize=9,
                                   leading=17, textColor=INK, spaceAfter=2)
    return s

S = styles()

# ---------- building blocks ----------
def rule_card(title, flowables, width=6.7 * inch, bar=NAVY):
    """Navy title bar + bordered body: the house 'rule card'."""
    head = Table([[Paragraph(title, S["cardtitle"])]], colWidths=[width])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    body = Table([[flowables]], colWidths=[width])
    body.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, bar),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    wrap = Table([[head], [body]], colWidths=[width])
    wrap.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return wrap

def callout(flowables, width=6.7 * inch, color=GOLD, bg=GOLD_PALE):
    """Gold left-rule callout."""
    t = Table([["", flowables]], colWidths=[4, width - 4])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), color),
        ("BACKGROUND", (1, 0), (1, -1), bg),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("RIGHTPADDING", (1, 0), (1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0),
    ]))
    return t

def source_class_box(kind, flowables, width=6.7 * inch):
    """Three-class source labels: LEDGER handled inline; this box is for
    CONVENTION and FIELD AMENDMENT material."""
    labels = {
        "convention": ("FRAMEWORK CONVENTION — not attributable to Buffett/Munger", GRAY, PALE),
        "amendment": ("FIELD AMENDMENT — JULY 2026 (tested experience)", GOLD, GOLD_PALE),
    }
    text, color, bg = labels[kind]
    head = Paragraph(f'<font color="#{color.hexval()[2:]}"><b>{text}</b></font>',
                     ParagraphStyle("sc", fontName="Helvetica-Bold", fontSize=7.6,
                                    leading=10, textColor=color))
    t = Table([[head], [flowables]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.7, color),
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

def q(text, src):
    """Quote + source-tag pair."""
    return [Paragraph(f'“{text}”', S["quote"]),
            Paragraph(src, S["source"])]

# ---------- page furniture ----------
class NumberedDoc(BaseDocTemplate):
    def __init__(self, path, doc_title, **kw):
        super().__init__(path, pagesize=LETTER, leftMargin=0.9 * inch,
                         rightMargin=0.9 * inch, topMargin=0.8 * inch,
                         bottomMargin=0.75 * inch, title=doc_title, **kw)
        self.doc_title = doc_title
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      id="main")
        self.addPageTemplates([PageTemplate(id="page", frames=[frame],
                                            onPage=self._decorate)])

    def _decorate(self, canv: Canvas, doc):
        canv.saveState()
        canv.setStrokeColor(GOLD)
        canv.setLineWidth(1.2)
        canv.line(doc.leftMargin, LETTER[1] - 0.55 * inch,
                  LETTER[0] - doc.rightMargin, LETTER[1] - 0.55 * inch)
        canv.setFont("Helvetica", 7)
        canv.setFillColor(GRAY)
        canv.drawString(doc.leftMargin, LETTER[1] - 0.48 * inch, self.doc_title)
        canv.drawRightString(LETTER[0] - doc.rightMargin, LETTER[1] - 0.48 * inch,
                             "v3.0 — July 2026")
        canv.setFillColor(NAVY)
        canv.drawCentredString(LETTER[0] / 2, 0.45 * inch, f"Page {doc.page}")
        canv.restoreState()

MOTTO = ("The goal is not to win. It is to see how wrong you can be and still be "
         "right. Margin of safety, moat assessment, conservative DCF modeling, and "
         "position sizing are each sequential admissions of fallibility.")
