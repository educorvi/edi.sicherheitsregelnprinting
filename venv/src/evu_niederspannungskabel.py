from fpdf import FPDF
from importdata import evu_niederspannungskabel as input

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

data["art_der_freischaltung1a"] = input.get('#/properties/edi6a8f77755207467090eddf15f6a21e87')

if data["art_der_freischaltung1a"] == "NH-Sicherungen":
    data["ausloesestrom1a"] = input.get('#/properties/edibedde3faf5304b9bb0101e9b23f5d284')
elif data["art_der_freischaltung1a"] == "NH-Lastschaltleiste":
    data["ausloesestrom1a"] = input.get('#/properties/edi78c896ef894445108dc67298d8b3318c')
elif data["art_der_freischaltung1a"] == "Leistungsschalter":
    data["ausloesestrom1a"] = input.get('#/properties/edi58255093bbca48999e2aaae5462f3c82')
else:
    data["ausloesestrom1a"] = "/"

data["ort_der_freischaltung1a"] = input.get('#/properties/edi1c959df02d0e4f65ac31465aed4ed8c6')

if data["ort_der_freischaltung1a"] == "Kabelverteilerschrank":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi424a0be1228145318070ee2f83c7b639')
elif data["ort_der_freischaltung1a"] == "Trafostation":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi5a9acfa863614586845b7fd9918cafc8')
elif data["ort_der_freischaltung1a"] == "Kompaktstation":
    data["nroderbezeichnung1a"] = input.get('#/properties/edi1af11b6f7ca74a85a9f8c1888071215f')

data["zusaetzlichfreigeschaltet1a"] = input.get('#/properties/edi39026745e38e4279b3113e51c8d76d50')

if data["zusaetzlichfreigeschaltet1a"] == ['im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)']:
    data["zusaetzlichfreigeschaltet1a"] = 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)'
else:
    data["zusaetzlichfreigeschaltet1a"] = ''

# Title

pdf.set_font('DGUVMeta-Bold', '', 20)
pdf.set_text_color(0,73,148)
pdf.set_xy(12.7, 63.25)
pdf.cell(0, 0, 'Arbeiten an Kabeln in der Niederspannung')

pdf.set_font('DGUVMeta-Bold', '', 14)
pdf.set_text_color(0,140,142)
pdf.set_xy(12.7, 83.5)
pdf.cell(0, 0, 'EVU')

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
pdf.image("newtemplate7_seite2.jpg", x=-4, y=-8, w=217, h=313)

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

if data["zusaetzlichfreigeschaltet1a"] == 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)':
    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35, 31, 32)
    pdf.set_xy(12.7, 63.7)
    pdf.cell(0, 0, 'Zusätzlich freigeschaltet:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(12.7, 68.7)
    pdf.cell(0, 0, data.get("zusaetzlichfreigeschaltet1a"))
else:
    data["zusaetzlichfreigeschaltet1a"] = ''

pdf.output("evu_niederspannungskabel.pdf", "F")