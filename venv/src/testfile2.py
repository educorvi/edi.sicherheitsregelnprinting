import os.path
import tempfile
from datetime import date
from time import localtime, gmtime, strftime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import grey, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.frames import Frame
from reportlab.platypus import Table
from reportlab.platypus.flowables import Flowable, Spacer, Image, PageBreak, BalancedColumns
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT as _r
from reportlab.lib.enums import TA_CENTER as _c
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from apply import apply

dguvnormal = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DGUVMeta-Normal.ttf')
dguvbold = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DGUVMeta-Bold.ttf')

pdfmetrics.registerFont(TTFont('DGUVNormal', dguvnormal))
pdfmetrics.registerFont(TTFont('DGUVBold', dguvbold))

class PdfBaseTemplate(BaseDocTemplate):
    """Basistemplate for PDF-Prints"""

    def __init__(self, filename, **kw):
        frame1 = Frame(1 * cm, 1 * cm, 18.5 * cm, 27 * cm, id='F1', showBoundary=False)
        self.allowSplitting = 0
        apply(BaseDocTemplate.__init__, (self, filename), kw)
        self.addPageTemplates(PageTemplate('normal', [frame1]))

class NumberedCanvas(canvas.Canvas):
    """Add Page number to generated PDF"""

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("DGUVBold", 7.5)
        if self._pageNumber < page_count:
            self.drawRightString(19.3 * cm, 1 * cm, "Seite %d von %d" % (self._pageNumber, page_count))
        if self._pageNumber == page_count:
            self.drawRightString(19.3 * cm, 2 * cm, "Seite %d von %d" % (self._pageNumber, page_count))
            self.drawString(9.25 * cm, 2 * cm, "www.bgetem.de")
            self.drawString(1.2 * cm, 2 * cm, "Berufsgenossenschaft")
            self.drawString(1.2 * cm, 1.6 * cm, "Energie Textil Elektro")
            self.drawString(1.2 * cm, 1.2 * cm, "Medienerzeugnisse")

def createpdf(filehandle, content):
    """Funktion zum Schreiben der PDF-Datei"""

    story = []  # Alle Elemente des PDFs werden der Story hinzugefuegt

    # Styles fuer normale Paragraphen, gelesen aus dem SampleStyleSheet
    stylesheet = getSampleStyleSheet()

    h1 = stylesheet['Heading1']
    h1.fontname = 'DGUVBold'

    h2 = stylesheet['Heading2']
    h2.fontName = 'DGUVBold'

    h3 = stylesheet['Heading3']
    h3.fontname = 'DGUVBold'

    code = stylesheet['Code']

    bodytext = stylesheet['BodyText']
    bodytext.fontName = 'DGUVNormal'

    bodybold = stylesheet['BodyText']
    bodybold.fontName = 'DGUVBold'

    # Weitere Styles fuer Paragraphen
    stylesheet.add(ParagraphStyle(name='smallbody', fontName='DGUVNormal', fontSize=9, spaceAfter=5))
    stylesheet.add(ParagraphStyle(name='normal', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='free', fontName='DGUVNormal', fontSize=7.5, borderPadding=0))
    stylesheet.add(ParagraphStyle(name='right', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_r))
    stylesheet.add(ParagraphStyle(name='center', fontName='DGUVNormal', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_c))
    stylesheet.add(ParagraphStyle(name='bold', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='boldnew', fontName='DGUVBold', fontSize=9, borderPadding=(5, 3, 3, 5)))
    stylesheet.add(ParagraphStyle(name='boldright', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_r))
    stylesheet.add(ParagraphStyle(name='boldcenter', fontName='DGUVBold', fontSize=7.5, borderPadding=(5, 3, 3, 5), alignment=_c))

    smallbody = stylesheet['smallbody']
    bullet = stylesheet['Bullet']
    bullet.fontSize=9
    bullet.fontName='DGUVNormal'
    entry_normal = stylesheet['normal']
    entry_free = stylesheet['free']
    entry_right = stylesheet['right']
    entry_center = stylesheet['center']
    entry_bold = stylesheet['bold']
    entry_boldnew = stylesheet['boldnew']
    entry_boldright = stylesheet['boldright']
    entry_boldcenter = stylesheet['boldcenter']

    coronastyles = {}
    coronastyles['h1'] = h1
    coronastyles['h2'] = h2
    coronastyles['h3'] = h3
    coronastyles['code'] = code
    coronastyles['bodytext'] = bodytext
    coronastyles['bodybold'] = bodybold
    coronastyles['smallbody'] = smallbody
    coronastyles['bullet'] = bullet
    coronastyles['entry_normal'] = entry_normal
    coronastyles['entry_free'] = entry_free
    coronastyles['entry_right'] = entry_right
    coronastyles['entry_center'] = entry_center
    coronastyles['entry_bold'] = entry_bold
    coronastyles['entry_boldnew'] = entry_boldnew
    coronastyles['entry_boldright'] = entry_boldright
    coronastyles['entry_boldcenter'] = entry_boldcenter

    im = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/logo_etem.jpg')
    logo = Image(im)
    logo.drawHeight = 6 * cm * logo.drawHeight / logo.drawWidth
    logo.drawWidth = 6 * cm
    logo.hAlign = 'RIGHT'

    # Datum
    datum = u"Datum: %s" % (strftime("%d.%m.%Y"))
    zeit = u"Zeit: %s" % (strftime("%H:%M:%S", localtime()))

    colWidths = [9.5*cm, 2.75*cm, 6.25*cm]
    formtitle = content.get('title')
    testheadline = u'<font color="#008c8e"><b>%s</b></font>' % formtitle
    toptable = [[Paragraph(testheadline, h2), Paragraph(u" ", bodytext), logo]]
    table = Table(toptable, colWidths=colWidths, style=[('VALIGN', (0, 0), (-1, -1), 'TOP')])
    table.hAlign = 'CENTER'
    story.append(table)
    story.append(Spacer(0 * cm, 0.5 * cm))

    textbox_name = InteractiveTextField('Name', 250)
    textbox_datum = InteractiveTextField('Datum', 250)
    textbox_unternehmer = InteractiveTextField('Unternehmer/Unternehmerin', 250)

    story.append(Paragraph(u"Firma", entry_free))
    story.append(textbox_name)
    story.append(Spacer(0 * cm, 0.1 * cm))
    story.append(Paragraph(u"Datum", entry_free))
    story.append(textbox_datum)
    story.append(Spacer(0 * cm, 0.1 * cm))
    story.append(Paragraph(u"Unternehmer/Unternehmerin", entry_free))
    story.append(textbox_unternehmer)

    story.append(Spacer(0 * cm, 0.5 * cm))

    for i in content.get('content'):
        if i.portal_type == 'Textblock':
            blockkey = 'textblock_%s' % i.UID()
            textblock = content.get(blockkey)
            if i.spalten == 2:
                story = create_columnblock(textblock, coronastyles, story)
            else:
                story = create_textblock(textblock, coronastyles, story)
            story.append(Spacer(0 * cm, 1 * cm))
        elif i.portal_type == 'Tabelle':
            story.append(create_tabelle(i, coronastyles, 'nva'+i.UID()))
            story.append(Spacer(0 * cm, 1 * cm))
        elif i.portal_type == 'Ueberschrift':
            story.append(Paragraph(i.title, coronastyles[i.format]))

    story.append(PageBreak())
    story.append(Spacer(0 * cm, 1 * cm))
    story.append(Paragraph(u"Weitere Maßnahmen (z. B. Notfall- oder Pandemieplan):", smallbody))
    story.append(Spacer(0 * cm, 0.5 * cm))
    story.append(InteractiveTextField('massnahme1', 500))
    story.append(InteractiveTextField('massnahme2', 500))
    story.append(InteractiveTextField('massnahme3', 500))
    story.append(InteractiveTextField('massnahme4', 500))
    story.append(InteractiveTextField('massnahme5', 500))
    story.append(InteractiveTextField('massnahme6', 500))
    story.append(InteractiveTextField('massnahme7', 500))
    story.append(InteractiveTextField('massnahme8', 500))

    story.append(Spacer(0 * cm, 14 * cm))
    schlusstext = u"""Diese Gefährdungsbeurteilung ergänzt die betriebliche Gefährdungsbeurteilung. Sie wurde
                      vor Beginn der Arbeiten erstellt, die Maßnahmen wurden umgesetzt und auf Wirksamkeit überprüft.
                      Die Mitarbeiter sind unterwiesen."""
    schlussline = u'<font color="#008c8e"><b>%s</b></font>' % schlusstext
    story.append(Paragraph(schlussline, bodybold))

    story.append(Spacer(0 * cm, 0.5 * cm))

    textbox_name = InteractiveTextField('name_verantwortlich', 250)
    textbox_unterschrift = InteractiveTextField('datum_unterschrift', 250)
    colWidths = [9.25*cm, 9.25*cm]
    signtable = [[textbox_name, textbox_unterschrift],
                 [Paragraph(u"Name des Arbeitsverantwortlichen", entry_free),
                  Paragraph(u"Datum, Unterschrift", entry_free)]
                ]
    table = Table(signtable, colWidths=colWidths)
    table.hAlign = 'CENTER'
    story.append(table)

    story.append(Spacer(0 * cm, 1 * cm))

    colWidths = [8*cm, 4.5*cm, 6*cm]
    datum_version = "%s, Version %s" % (content.get('stand'), content.get('version'))
    bestellnummer = "Bestell-Nr. %s" % content.get('bestellnr')
    datatable = [[Paragraph(u" "), Paragraph(datum_version, entry_free), Paragraph(bestellnummer, entry_boldright)]]
    table = Table(datatable, colWidths=colWidths)
    story.append(table)

    doc = PdfBaseTemplate(filehandle, pagesize=A4)
    doc.build(story, canvasmaker=NumberedCanvas)
