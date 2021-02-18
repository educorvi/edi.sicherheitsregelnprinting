from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("elektrohandwerk-schaltanlagen-vorlage.jpg", x=-4, y=-8, w=217, h=313)

# 1 Freigeschaltet

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 31)
pdf.cell(0, 0, '')

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 98)
pdf.cell(0, 0, '')

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 168)
pdf.cell(0, 0, '')

# 4 Geerdet und kurzgeschlossen

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 208)
pdf.cell(0, 0, '')

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 251)
pdf.cell(0, 0, '')


pdf.output("elektrohandwerk-betriebsmittel.pdf", "F")