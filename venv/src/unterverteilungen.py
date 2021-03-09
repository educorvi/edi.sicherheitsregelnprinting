from fpdf import FPDF
from importdata import input

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("newtemplate1_seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}
input = input.get("data")

#Kopffragen

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
"""
# Verbindung zwischen ausloesestrom und art_der_freischaltung?
# data["art_der_freischaltung"] = input.get('#/properties/edi4961450e44ba4d16aeb015a919e73f0a')
# data["ausloesestrom"] = "50"
data["ort_der_freischaltung"] = input.get('#/properties/edi2e32c9143f91464392d3ea5b72c1db89')
# data["ort_nroderbezeichnung"] = "55934"
"""

data["art_der_freischaltung"] = "NH-Sicherungen"
data["ausloesestrom"] = "50"
data["ort_der_freischaltung"] = "Trafostation"

# 2
"""
data["sperrelement"] = input.get('#/properties/edi36e713d0f0544afab38414b8d139fcec')
data["betriebsraum_tuer_verschlossen"] = input.get('#/properties/edi8aeb082703364653b77ecedfb294800c')
data["schalten_verboten"] = input.get('#/properties/ediff3de7cc99c74d7a8d7fc9430714cc4d')
"""

data["sperrelement"] = "ja"
data["betriebsraum_tuer_verschlossen"] = "ja"
data["schalten_verboten"] = "ja"

# 3
"""
data["spannungspruefer"] = input.get('#/properties/edi9b0ea2910d514df791e528597a6e5f28')
data["usv"] = input.get('#/properties/edi94283112763649bda0ef6f900ddc2cbc')
"""

data["spannungspruefer"] = "3M Voltage Meter x559m"
data["usv"] = "ja"

# 4
"""
data["euk_wo_eingebaut"] = input.get('#/properties/edibba761f4767d4a3b9f1528712f8f1abe')
data["geerdet_begruendung"] = input.get('#/properties/edibba761f4767d4a3b9f1528712f8f1abe')
"""

data["euk_wo_eingebaut"] = "am richtigen Ort"
data["geerdet_begruendung"] = "Richtiger Einbau erfolgt"

# 5
"""
data["ziel_der_abdeckung"] = input.get('#/properties/edi94f9841893d04f6184e06a9b57797e59')
"""

data["ziel_der_abdeckung"] = "Personenschutz"


# Kopffragen

#to be added bei ja/nein-frage
#Stehen andere Anlagenteile weiterhin unter Spannung, so dass der Arbeitsbereich z. B. mit Ketten oder Bändern gekennzeichnet oder abgegrenzt werden muss?

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

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 230)
pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 235)
pdf.cell(0, 0, data.get("art_der_freischaltung"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 245)
pdf.cell(0, 0, 'Auslösestrom: %s A' % data.get("ausloesestrom"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 255)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 260)
pdf.cell(0, 0, data.get("ort_der_freischaltung"))

# 2 Gegen Wiedereinschalten gesichert

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 22)
pdf.cell(0, 0, 'Wurde ein Sperrelement eingesetzt, weil')

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 27)
pdf.cell(0, 0, 'der Bereich fuer Laien zugaenglich ist?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 33)
pdf.cell(0, 0, data.get("sperrelement"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 43)
pdf.cell(0, 0, 'Wurde die Tür zum elektrischen')

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 48)
pdf.cell(0, 0, 'Betriebsraum verschlossen?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 53)
pdf.cell(0, 0, data.get("betriebsraum_tuer_verschlossen"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 63)
pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten"')

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 68)
pdf.cell(0, 0, 'zusätzlich angebracht?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 73)
pdf.cell(0, 0, data.get("schalten_verboten"))

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 89)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 94)
pdf.cell(0, 0, data.get("spannungspruefer"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 104)
pdf.cell(0, 0, 'Dezentrale Einspeisung vorhanden, z.B.')

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 109)
pdf.cell(0, 0, 'USV, PV, Notstromaggregat?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 114)
pdf.cell(0, 0, data.get("usv"))

# 4 Geerdet und kurzgeschlossen

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 130)
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung')

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 135)
pdf.cell(0, 0, 'eingebaut?')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 140)
pdf.cell(0, 0, data.get("euk_wo_eingebaut"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 150)
pdf.cell(0, 0, 'Begründung:')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 155)
pdf.cell(0, 0, data.get("geerdet_begruendung"))

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 170)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 175)
pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

pdf.output("unterverteilungen.pdf", "F")
