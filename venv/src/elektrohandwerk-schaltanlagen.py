from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("vorlage5-Seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}
data["art_der_freischaltung"] = "NH-Sicherungen"

# Kopffragen

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(3, 74)
pdf.cell(0, 0, 'educorvi GmbH & Co. KG')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(3, 92)
pdf.cell(0, 0, '01.03.2021')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(3, 110)
pdf.cell(0, 0, 'Lars Walther')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(3, 128.5)
pdf.cell(0, 0, 'Lars Walther')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(3, 146.5)
pdf.cell(0, 0, 'Seppo Walther')

pdf.set_font('Arial', '', 14)
pdf.set_xy(4.4, 173.6)
pdf.cell(0, 0, 'x')

pdf.set_font('Arial', '', 14)
pdf.set_xy(78.7, 173.6)
pdf.cell(0, 0, 'x')

pdf.set_font('Arial', '', 14)
pdf.set_xy(4.3, 199.9)
pdf.cell(0, 0, 'x')

pdf.set_font('Arial', '', 14)
pdf.set_xy(27.5, 199.9)
pdf.cell(0, 0, 'x')

# 1 Freigeschaltet

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 230)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 235)
pdf.cell(0, 0, data.get("art_der_freischaltung"))

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 245)
pdf.cell(0, 0, 'Auslösestrom: %s A' % '50')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 255)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 260)
pdf.cell(0, 0, 'Trafostation')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 270)
pdf.cell(0, 0, 'Nr. oder Bezeichnung: %s' % '55934')

#Adding new page

pdf.add_page()
pdf.image("vorlage5-Seite2.jpg", x=-4, y=-8, w=217, h=313)

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 22)
pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 27)
pdf.cell(0, 0, 'Schalter eingehängt und abgeschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 33)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 43)
pdf.cell(0, 0, 'Wurde die Tür zum elektrischen')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 48)
pdf.cell(0, 0, 'Betriebsraum verschlossen?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 53)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 63)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 68)
pdf.cell(0, 0, 'zusätzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 73)
pdf.cell(0, 0, 'ja')

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 89)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 99)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 4 Geerdet und kurzgeschlossen

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 130)
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 135)
pdf.cell(0, 0, 'eingebaut?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 140)
pdf.cell(0, 0, 'zu Hause')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 150)
pdf.cell(0, 0, 'Begründung:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 155)
pdf.cell(0, 0, 'Weil ichs kann')

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 170)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 175)
pdf.cell(0, 0, 'Nichts')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 185)
pdf.cell(0, 0, 'Art der Abdeckung:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 190)
pdf.cell(0, 0, 'isolierende Formteile')


pdf.output("elektrohandwerk-schaltanlagen.pdf", "F")