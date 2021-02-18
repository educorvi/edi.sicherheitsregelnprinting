from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("elektrische-betriebsmittel-vorlage.jpg", x=-4, y=-8, w=217, h=313)

# 1 Freigeschaltet

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 31)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 36)
pdf.cell(0, 0, 'LS-Schalter')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 46)
pdf.cell(0, 0, 'Ausloesestrom: %s A' % '50')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 56)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 61)
pdf.cell(0, 0, 'Trafostation')

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 83)
pdf.cell(0, 0, 'Wurde ein Sperrlement eingesetzt, weil')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 88)
pdf.cell(0, 0, 'der Bereich fuer Laien zugaenglich ist?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 93)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 103)
pdf.cell(0, 0, 'Wurde eine Schaltsperre eingesetzt, weil')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 108)
pdf.cell(0, 0, 'der Bereich fuer Laien zugaenglich ist?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 113)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 123)
pdf.cell(0, 0, 'Wurde ein Reparaturschalter mit einem')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 128)
pdf.cell(0, 0, 'Vorhaengeschloss versehen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 133)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 143)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 148)
pdf.cell(0, 0, 'zusaetzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 153)
pdf.cell(0, 0, 'magnetisch')


# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 168)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 173)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 4 Geerdet und kurzgeschlossen

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 208)
pdf.cell(0, 0, '')

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 251)
pdf.cell(0, 0, '')


pdf.output("elektrische-betriebsmittel.pdf", "F")