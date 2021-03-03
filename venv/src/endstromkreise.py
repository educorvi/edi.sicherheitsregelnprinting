from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("vorlage7-Seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}

# Kopffragen
"""
data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
data["datum_uhrzeit"] = input.get('#/properties/datum-und-uhrzeit')
data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen)
data["person_arbeitsverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-arbeitsverantwortlichen')
data["person_arbeitsausfuehrung"] = input.get('#/properties/arbeitsausfuhrende-person')
# Multiple-Choice-Felder (?):
# data["zusaetzliche_schutzausrüstung"] = input.get('#/properties/zusatzliche-personliche-schutzausrustung')
# data["abgrenzung_arbeitsbereich"] = input.get('#/properties/wurde-der-arbeitsbereich-z-b-mit-ketten-oder')
"""

data["arbeitsstelle"] = "educorvi GmbH & Co. KG"
data["datum_uhrzeit"] = "01.03.2021 11:57 Uhr"
data["person_anlageverantwortlichkeit"] = "Lars Walther"
data["person_arbeitsverantwortlichkeit"] = "Lars Walther"
data["person_arbeitsausfuehrung"] = "Seppo Walther"
data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = "x"
data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = "x"
data["abgrenzung_arbeitsbereich_ja"] = "x"
data["abgrenzung_arbeitsbereich_nein"] = "x"

# Kopffragen

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(12, 76)
pdf.cell(0, 0, data.get("arbeitsstelle"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(12, 94)
pdf.cell(0, 0, data.get("datum_uhrzeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(12, 112.5)
pdf.cell(0, 0, data.get("person_anlageverantwortlichkeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(12, 131)
pdf.cell(0, 0, data.get("person_arbeitsverantwortlichkeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(12, 149.5)
pdf.cell(0, 0, data.get("person_arbeitsausfuehrung"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14.1, 175.6)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_elektrischerschlag"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(88.4, 175.6)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_stoerlichtbogen"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14, 200.8)
pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_ja"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(37.2, 200.8)
pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_nein"))

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
pdf.cell(0, 0, 'Unterverteilung %s ' % '55934')

#Adding new page

pdf.add_page()
pdf.image("vorlage7-Seite2.jpg", x=-4, y=-8, w=217, h=313)

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 100)
pdf.cell(0, 0, 'Wurde ein Sperrelement eingesetzt, weil')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 105)
pdf.cell(0, 0, 'der Bereich fuer Laien zugaenglich ist?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 110)
pdf.cell(0, 0, 'ja')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 120)
pdf.cell(0, 0, 'Wurde eine Schaltsperre eingesetzt, weil')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 125)
pdf.cell(0, 0, 'der Bereich fuer Laien zugaenglich ist?')

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
pdf.cell(0, 0, 'ja')

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
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 213)
pdf.cell(0, 0, 'eingebaut?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 218)
pdf.cell(0, 0, 'zu Hause')

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

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 266)
pdf.cell(0, 0, 'Art der Abdeckung:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 271)
pdf.cell(0, 0, 'isolierende Formteile')


pdf.output("endstromkreise.pdf", "F")