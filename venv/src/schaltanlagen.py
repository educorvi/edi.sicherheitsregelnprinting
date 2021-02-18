from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("vorlage1.jpg", x=-4, y=-8, w=217, h=313)

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
pdf.set_xy(108, 100)
pdf.cell(0, 0, 'Wurde ein Vorhaengeschloss am')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 105)
pdf.cell(0, 0, 'Schalter eingehaengt und abgeschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 110)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 120)
pdf.cell(0, 0, 'Wurde die Tuer zum elektrischen')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 125)
pdf.cell(0, 0, 'Betriebsraum verschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 130)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 140)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 145)
pdf.cell(0, 0, 'zusätzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 150)
pdf.cell(0, 0, 'magnetisch')

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 168)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 173)
pdf.cell(0, 0, '3M Voltage Meter x559m')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 183)
pdf.cell(0, 0, 'Dezentrale Einspeisung vorhanden,')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 188)
pdf.cell(0, 0, 'z.B. USV, PV, Notstromaggregat?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 193)
pdf.cell(0, 0, 'ja')

# 4 Geerdet und kurzgeschlossen

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 208)
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 213)
pdf.cell(0, 0, 'eingebaut?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 218)
pdf.cell(0, 0, 'in die NH-Sicherungsunterteile')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 228)
pdf.cell(0, 0, 'Begründung:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 233)
pdf.cell(0, 0, 'Weil ichs kann')

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 251)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 256)
pdf.cell(0, 0, 'Nichts')

pdf.output("schaltanlagen.pdf", "F")