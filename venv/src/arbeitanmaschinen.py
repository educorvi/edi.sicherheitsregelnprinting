from fpdf import FPDF
from importdata import arbeitanmaschinen as input

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("newtemplate1_seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}
input = input.get("data")

# Kopffragen

data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
data["datum_uhrzeit"] = input.get('#/properties/datum-und-uhrzeit')
data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen')
data["person_arbeitsverantwortlichkeit"] = input.get('#/properties/persone-in-der-rolle-des-arbeitsverantwortlichen')
data["person_arbeitsausfuehrung"] = input.get('#/properties/arbeitsausfuhrende-person')

if 'gegen elektrischen Schlag' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
    data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = "x"
else:
    data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = ""

if 'gegen Störlichtbogen' in input.get('#/properties/zusatzliche-personliche-schutzausrustung-bei-der-1'):
    data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = "x"
else:
    data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = ""

if input.get('#/properties/stehen-andere-anlagenteile-weiterhin-unter') == "ja":
    data["abgrenzung_arbeitsbereich_ja"] = "x"
else:
    data["abgrenzung_arbeitsbereich_ja"] = ""

if input.get('#/properties/stehen-andere-anlagenteile-weiterhin-unter') == "nein":
    data["abgrenzung_arbeitsbereich_nein"] = "x"
else:
    data["abgrenzung_arbeitsbereich_nein"] = ""

# Title

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 58.5)
pdf.cell(0, 0, 'Arbeiten an Maschinen, Fertigungsanlagen')

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 68)
pdf.cell(0, 0, 'oder anderen Verbrauchern')

pdf.set_font('DGUVMeta-Bold', '', 14)
pdf.set_text_color(0,140,142)
pdf.set_xy(12.7, 83.5)
pdf.cell(0, 0, 'Industrie')

# Kopffragen

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 107)
pdf.set_text_color(0,0,0)
pdf.cell(0, 0, data.get("arbeitsstelle"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 126)
pdf.cell(0, 0, data.get("datum_uhrzeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 145)
pdf.cell(0, 0, data.get("person_anlageverantwortlichkeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 164)
pdf.cell(0, 0, data.get("person_arbeitsverantwortlichkeit"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 183)
pdf.cell(0, 0, data.get("person_arbeitsausfuehrung"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_xy(20, 208.5)
pdf.cell(0, 0, "gegen elektrischen Schlag")

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14.3, 208.3)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_elektrischerschlag"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_xy(78, 208.5)
pdf.cell(0, 0, "gegen Störlichbogen")

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(72.2, 208.3)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_stoerlichtbogen"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_xy(20, 232)
pdf.cell(0, 0, "ja")

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14.4, 231.6)
pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_ja"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_xy(78, 232)
pdf.cell(0, 0, "nein")

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(72.2, 231.6)
pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_nein"))

#Adding new page

pdf.add_page()
pdf.image("newtemplate1_seite2.jpg", x=-4, y=-8, w=217, h=313)


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