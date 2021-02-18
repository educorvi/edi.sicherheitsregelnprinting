from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("vorlage4.jpg", x=-4, y=-8, w=217, h=313)

# 1 Freigeschaltet

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 31)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 36)
pdf.cell(0, 0, 'NH-Lastschaltleiste')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 46)
pdf.cell(0, 0, 'Auslösestrom: %s A' % '50')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 56)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 61)
pdf.cell(0, 0, 'Trafostation %s ' % '55934')

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 75)
pdf.cell(0, 0, 'Wie erfolgte die Sicherung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 80)
pdf.cell(0, 0, 'Steuersicherung entfernt')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 90)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 95)
pdf.cell(0, 0, 'zusätzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 100)
pdf.cell(0, 0, 'magnetisch')

# 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 122)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 127)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 3b Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 157)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 163)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 4 Geerdet und kurzgeschlossen

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 187)
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 193)
pdf.cell(0, 0, 'eingebaut?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 198)
pdf.cell(0, 0, 'in die NH-Sicherungsunterteile')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 208)
pdf.cell(0, 0, 'Begründung:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 213)
pdf.cell(0, 0, 'Weil ichs kann')

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 245)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 250)
pdf.cell(0, 0, 'Nichts')

pdf.output("arbeitanmaschinen.pdf", "F")