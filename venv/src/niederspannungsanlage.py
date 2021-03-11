from fpdf import FPDF
from importdata import niederspannungsanlage as input

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("newtemplate3_seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}
input = input.get("data")

# Kopffragen

data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
data["datum_uhrzeit"] = input.get('#/properties/datum-und-uhrzeit')
data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen')
data["person_arbeitsverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-arbeitsverantwortlichen')
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

# 1

data["art_der_freischaltung"] = input.get('#/properties/edia35d5a284cfd441c8e85d75491d7b2b0')

if data["art_der_freischaltung"] == "NH-Sicherungen":
    data["ausloesestrom"] = input.get('#/properties/edi6ac532fc3bb3466bb37bf9fa0fe69723')
elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
    data["ausloesestrom"] = input.get('#/properties/edi91a3dd70963646b1a1b97d61c7e4a82a')
elif data["art_der_freischaltung"] == "Leistungsschalter":
    data["ausloesestrom"] = input.get('#/properties/edia0d7558f2b2742cc93296ecbdaafb6ea')
elif data["art_der_freischaltung"] == "Trenner geöffnet":
    data["ausloesestrom"] = input.get('#/properties/edi58b116e71fed42d08e9d13d7ccdcd1d7')
else:
    data["ausloesestrom"] = "/"

data["ort_der_freischaltung"] = input.get('#/properties/edi5a7f273428f74de489972b6913c66075')

if data["ort_der_freischaltung"] == "Trafostation":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edi3d04e27bf3ea4b699896ebb282d85cfa')
elif data["ort_der_freischaltung"] == "Umspannwerk/-anlage":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edicd578854837541c8b00db113e7f28a67')
elif data["ort_der_freischaltung"] == "Station Niederspannung":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edi51afae6421aa4aa593e6280ae0e87f01')
elif data["ort_der_freischaltung"] == "Schaltfeld Niederspannung":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edi3859034e0e724ceabb64955eb53fc3d4')
else:
    data["ort_nroderbezeichnung"] = "/"

# 2

data["sicherungsart"] = input.get('#/properties/edicc623be9685e4de8b5963d52533abae5')
data["schalten_verboten"] = input.get('#/properties/edibc8dd2af0a9446eca50e69cf66ea27c5')

# 3

data["spannungspruefer"] = input.get('#/properties/edid0e606c47a8942f3b34084387a472765')

# Title

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 58.5)
pdf.cell(0, 0, 'Arbeiten an Schaltanlagen')

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 68)
pdf.cell(0, 0, 'der Niederspannung')

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

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 29.2)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 34.2)
pdf.cell(0, 0, data.get("art_der_freischaltung"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 39.2)
pdf.cell(0, 0, 'Auslösestrom: %s A' % data.get("ausloesestrom"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 50)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 55)
pdf.cell(0, 0, data.get("ort_der_freischaltung"))

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 60)
pdf.cell(0, 0, 'Nr. oder Bezeichnung: %s' % data.get("ort_nroderbezeichnung"))

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 77.5)
pdf.cell(0, 0, 'Wie wurde gesichert?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 82.5)
pdf.cell(0, 0, data.get("sicherungsart"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 89)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 94)
pdf.cell(0, 0, data.get("schalten_verboten"))

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 136)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 141)
pdf.cell(0, 0, data.get("spannungspruefer"))

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

pdf.output("niederspannungsanlage.pdf", "F")