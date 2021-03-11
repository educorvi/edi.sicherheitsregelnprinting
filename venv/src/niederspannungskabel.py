from fpdf import FPDF
from importdata import niederspannungskabel as input

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

# 1A

data["art_der_freischaltung1a"] = input.get('#/properties/edia5679b847b3e4c4598e9349227d4299b')

if data["art_der_freischaltung1a"] == "NH-Sicherungen":
    data["ausloesestrom1a"] = input.get('#/properties/edid605559080d64bbb8d4850749dc12f1c')
elif data["art_der_freischaltung1a"] == "NH-Lastschaltleiste":
    data["ausloesestrom1a"] = input.get('#/properties/edi12145ea0507746278169217acf02dd81')
elif data["art_der_freischaltung1a"] == "Leistungsschalter":
    data["ausloesestrom1a"] = input.get('#/properties/edi0403a154b0554947af6b9431278d993a')
else:
    data["ausloesestrom1a"] = "/"

data["ort_der_freischaltung1a"] = input.get('#/properties/edi838ee883350146549eaf39b9699e1293')

if data["ort_der_freischaltung1a"] == "Kabelverteilerschrank":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi778ae09c2a7d4430b457f10809926977')
elif data["ort_der_freischaltung1a"] == "Trafostation":
    data["nroderbezeichnung1a"] = input.get('#/properties/edic1240cd04d36417cacc2235fc1e82284')
elif data["ort_der_freischaltung1a"] == "Niederspannungs-Hauptverteilung":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi17167f2ec33d4ea2839e56ff60131387')
elif data["ort_der_freischaltung1a"] == "Niederspannungs-Schaltstation":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi198e6b2542674ebab13c94d75af66149')

# 1B

data["art_der_freischaltung"] = input.get('#/properties/edi0df2502e80594c2d9df307d0f939562f')

if data["art_der_freischaltung"] == "NH-Sicherungen":
    data["ausloesestrom"] = input.get('#/properties/edi7b8b089113024ab69c2133a6295219a8')
elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
    data["ausloesestrom"] = input.get('#/properties/edi71229e67f15042d49d1bedbab36e5e9d')
elif data["art_der_freischaltung"] == "Leistungsschalter":
    data["ausloesestrom"] = input.get('#/properties/edid7c9a6a76c3d453ca2454be566b04301')
else:
    data["ausloesestrom"] = "/"

data["ort_der_freischaltung"] = input.get('#/properties/edicbf3dd9390984bf8813716bbe56b59ee')

if data["ort_der_freischaltung"] == "Kabelverteilerschrank":
    data["nroderbezeichnung"] = input.get('#/properties/edi022ee3cb58684aafa3cdf0fc711db5c6')
elif data["ort_der_freischaltung"] == "Trafostation":
    data["nroderbezeichnung"] = input.get('#/properties/edi62df182f4cc542b294471fd7e02e13ba')
elif data["ort_der_freischaltung"] == "Niederspannungs-Hauptverteilung":
    data["nroderbezeichnung"] = input.get('#/properties/edia32c8b9872cd482ba67cfcadbddaea90')
elif data["ort_der_freischaltung"] == "Niederspannungs-Schaltstation":
    data["nroderbezeichnung"] = input.get('#/properties/edi202c14b3bb1241dc819115fd5b8bc8f6')

# Title

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 58.5)
pdf.cell(0, 0, 'Arbeiten an Kabeln')

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 68)
pdf.cell(0, 0, 'in der Niederspannung')

pdf.set_font('DGUVMeta-Bold', '', 14)
pdf.set_text_color(0,140,142)
pdf.set_xy(12.7, 83.5)
pdf.cell(0, 0, 'Industrie S140')

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
pdf.image("newtemplate3_seite2.jpg", x=-4, y=-8, w=217, h=313)

# 1a Freigeschaltet Ausschaltstelle 1

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 29.2)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 34.2)
pdf.cell(0, 0, data.get("art_der_freischaltung1a"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 40.7)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 45.7)
pdf.cell(0, 0, data.get("ort_der_freischaltung1a"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 52.2)
pdf.cell(0, 0, 'Nr. oder Bezeichnung:')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 57.2)
pdf.cell(0, 0, data.get("nroderbezeichnung1a"))

# 1b Freigeschaltet Ausschaltstelle 2

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 78)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 83)
pdf.cell(0, 0, 'NH-Lastschaltleiste')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 93)
pdf.cell(0, 0, 'Auslösestrom: %s A' % '50')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 103)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 108)
pdf.cell(0, 0, 'Trafostation %s ' % '55934')

# 2a Gegen Wiedereinschalten gesichert Ausschaltstelle 1

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 124)
pdf.cell(0, 0, 'Wie wurde gesichert?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 129)
pdf.cell(0, 0, 'Steuersicherung entfernt')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 139)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 144)
pdf.cell(0, 0, 'zusaetzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 149)
pdf.cell(0, 0, 'magnetisch')

# 2b Gegen Wiedereinschalten gesichert Ausschaltstelle 1

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 171)
pdf.cell(0, 0, 'Wie wurde gesichert?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 176)
pdf.cell(0, 0, 'Steuersicherung entfernt')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 186)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 191)
pdf.cell(0, 0, 'zusaetzlich angebracht?')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 196)
pdf.cell(0, 0, 'magnetisch')

# 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle1

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 225)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 230)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 3b Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle2

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 265)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 270)
pdf.cell(0, 0, '3M Voltage Meter x559m')

# 4a Geerdet und kurzgeschlossen Ausschaltstelle 1

"""
Work in progress
"""

# 4b Geerdet und krzgeschlossen Ausschaltstelle 2

"""
Work in progress
"""

# 5 Mit der Abdeckung soll erreicht werden

pdf.add_page()
pdf.image("vorlage3-Seite2.jpg", x=-4, y=-8, w=217, h=313)

pdf.set_font('Arial', '', 14)
pdf.set_xy(108, 98)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('Arial', 'u', 14)
pdf.set_xy(108, 103)
pdf.cell(0, 0, 'Nichts')


pdf.output("niederspannungskabel.pdf", "F")