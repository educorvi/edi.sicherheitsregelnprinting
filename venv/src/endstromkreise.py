# Template ohne Radiobutton bei Kopffragen

from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("newtemplate1_seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}

# Kopffragen
"""
data["arbeitsstelle"] = input.get('#/properties/arbeitsstelle-arbeitsort')
data["datum_uhrzeit"] = input.get('#/properties/datum-und-uhrzeit')
data["person_anlageverantwortlichkeit"] = input.get('#/properties/person-in-der-rolle-des-anlagenverantwortlichen)
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
"""

data["arbeitsstelle"] = "educorvi GmbH & Co. KG"
data["datum_uhrzeit"] = "01.03.2021 11:57 Uhr"
data["person_anlageverantwortlichkeit"] = "Lars Walther"
data["person_arbeitsverantwortlichkeit"] = "Lars Walther"
data["person_arbeitsausfuehrung"] = "Seppo Walther"
data["zusaetzliche_schutzausrüstung_elektrischerschlag"] = "x"
data["zusaetzliche_schutzausrüstung_stoerlichtbogen"] = "x"

# 1
"""
# data["art_der_freischaltung"] = input.get('#/properties/edi4ed9533af063465dbd40ede7ce144b34')

if data["art_der_freischaltung"] == "LS-Schalter":
    data["ausloesestrom"] = input.get('#/properties/edi595058c14f914f97913f1982c3ee63ed')
elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
    data["ausloesestrom"] = input.get('#/properties/edi866e423a5ffe4c8d8c634335fa41d500')
elif data["art_der_freischaltung"] == "Schraubsicherungen":
    data["ausloesestrom"] = input.get('#/properties/edidd592cc4a5674acfa8669da7e7056728')
else:
    data["ausloesestrom"] = "/"

data["ort_der_freischaltung"] = input.get('#/properties/edi86c60abee95a45c8886de483c2b84e91')
"""

data["art_der_freischaltung"] = "LS-Schalter"
data["ausloesestrom"] = "50"
data["ort_der_freischaltung"] = "Unterverteilung: 5303492"

# 2
"""
data["sperrelement"] = input.get('#/properties/')
data["betriebsraum_tuer_verschlossen"] = input.get('#/properties/')
data["schalten_verboten"] = input.get('#/properties/')
"""

data["sperrelement"] = "ja"
data["betriebsraum_tuer_verschlossen"] = "ja"
data["schalten_verboten"] = "ja"

# 3
"""
data["spannungspruefer"] = input.get('#/properties/')
data["usv"] = input.get('#/properties/')
"""

data["spannungspruefer"] = "3M Voltage Meter x559m"
data["usv"] = "ja"

# 4
"""
data["euk_wo_eingebaut"] = input.get('#/properties/')
data["geerdet_begruendung"] = input.get('#/properties/')
"""

data["euk_wo_eingebaut"] = "an der Sammelschiene"
data["geerdet_begruendung"] = "Richtiger Einbau erfolgt"

# 5
"""
data["ziel_der_abdeckung"] = input.get('#/properties/')
"""

data["ziel_der_abdeckung"] = "Personenschutz"

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

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 40.7)
pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(0,0,0)
pdf.set_xy(12.7, 45.7)
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

pdf.output("endstromkreise.pdf", "F")