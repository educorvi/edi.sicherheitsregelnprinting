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

# 1

data["art_der_freischaltung"] = input.get('#/properties/edi28afa3ee4d234949ad8d234d9aea29f9')

if data["art_der_freischaltung"] == "NH-Sicherungen":
    data["ausloesestrom"] = input.get('#/properties/edi935e850a261444598644af53f08dcd32')
elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
    data["ausloesestrom"] = input.get('#/properties/edi5d28dd3c9465429497162dd0518e05c0')
elif data["art_der_freischaltung"] == "Leistungsschalter":
    data["ausloesestrom"] = input.get('#/properties/edi53635db3c89e44aa81ef36372b2ac188')
elif data["art_der_freischaltung"] == "Trenner geöffnet":
    data["ausloesestrom"] = input.get('#/properties/edi898bfa6b08564c569e22437b853b6632')
else:
    data["ausloesestrom"] = "/"

data["ort_der_freischaltung"] = input.get('#/properties/edi2ec234bab6ab4651b9e024e421a6556e')

if data["ort_der_freischaltung"] == "Trafostation":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edi7b6be3fa231b47d193febc77614abf20')
elif data["ort_der_freischaltung"] == "Station Niederspannung":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edieda69f8934a840f5b6986f953e16fec4')
elif data["ort_der_freischaltung"] == "Schaltfeld Niederspannung":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edi43801a9ac06c471bb571823dbf676dd5')
elif data["ort_der_freischaltung"] == "Unterverteilung/Stromkreis":
    data["ort_nroderbezeichnung"] = input.get('#/properties/edibfbdfdc9a9a643bbb5e6de5689a22d74')
else:
    data["ort_nroderbezeichnung"] = "/"

# 2

data["sicherungsart"] = input.get('#/properties/edi24a2debaffea4b28a214b41c730e75ce')
data["schalten_verboten"] = input.get('#/properties/edifa1a1d574a4149c48b2d1bedcf0ccd29')

# 3a

data["spannungspruefer3a"] = input.get('#/properties/edi9eff5b18dc154de8895dbba3cc192249')

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

# 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 136)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 141)
pdf.cell(0, 0, data.get("spannungspruefer3a"))

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