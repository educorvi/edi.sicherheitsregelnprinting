from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

#pdf.image("5-Sicherheitsregeln-Vorlage-JPG.jpg", x=-4, y=-8, w=217, h=313)
pdf.image("vorlage-JPG.jpg", x=-4, y=-8, w=217, h=313)

# 1 Freigeschaltet

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 31)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 36)
pdf.cell(0, 0, 'NH-Sicherungen')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 46)
pdf.cell(0, 0, 'Auslösestrom NH-Sicherungen:')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 51)
pdf.cell(0, 0, '_________ A')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 61)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 66)
pdf.cell(0, 0, 'Trafostation')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 76)
pdf.cell(0, 0, 'Nr. oder Bezeichnung Umspannwerk')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 81)
pdf.cell(0, 0, '459')

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 98)
pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 103)
pdf.cell(0, 0, 'Schalter eingehängt und abgeschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 108)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 118)
pdf.cell(0, 0, 'Wurde die Tür zum elektrischen')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 123)
pdf.cell(0, 0, 'Betriebsraum verschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 128)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 138)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 143)
pdf.cell(0, 0, 'zusätzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 148)
pdf.cell(0, 0, 'ja')

pdf.output("sicherheitsregeln.pdf", "F")