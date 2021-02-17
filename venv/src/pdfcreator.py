from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

#pdf.image("5-Sicherheitsregeln-Vorlage-JPG.jpg", x=-4, y=-8, w=217, h=313)
pdf.image("testvorlage-JPG.jpg", x=-4, y=-8, w=217, h=313)

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

pdf.output("sicherheitsregeln.pdf", "F")