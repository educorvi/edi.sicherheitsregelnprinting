from fpdf import FPDF
from importdata import input

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("newtemplate1_seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}

#Kopffragen
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

# 1
"""
# Verbindung zwischen ausloesestrom und art_der_freischaltung?
# data["art_der_freischaltung"] = input.get('#/properties/edi43ba285a6396493da82241d5ecec090d')
# data["ausloesestrom"] = "50"
data["ort_der_freischaltung"] = input.get('#/properties/edi43ba285a6396493da82241d5ecec090d')
# data["ort_nroderbezeichnung"] = "55934"
"""

data["art_der_freischaltung"] = "NH-Sicherungen"
data["ausloesestrom"] = "50"
data["ort_der_freischaltung"] = "Trafostation"
data["ort_nroderbezeichnung"] = "55934"

# 2
"""
data["vorhaengeschloss_schalter"] = input.get('#/properties/edic589597967b44e00af9e74c7c1319cb0')
data["betriebsraum_tuer_verschlossen"] = input.get('#/properties/edi64719875ff504d6eb8fd735f12fd7d17')
data["schalten_verboten"] = input.get('#/properties/edi6af7fbabb2a44046b882d580080326e1')
"""

data["vorhaengeschloss_schalter"] = "ja"
data["betriebsraum_tuer_verschlossen"] = "ja"
data["schalten_verboten"] = "ja"

# 3
"""
data["spannungspruefer"] = input.get('#/properties/edi594b8869f8884cb4b76d376d960c3b74')
"""

data["spannungspruefer"] = "3M Voltage Meter x559m"

# 4
"""
data["euk_wo_eingebaut"] = input.get('#/properties/ediec7dc4dfa3b646818f003c01c9f1709c')
data["geerdet_begruendung"] = input.get('#/properties/edibc2aa174fac14dc68fdce90b73990e62')
"""

data["euk_wo_eingebaut"] = "am richtigen Ort"
data["geerdet_begruendung"] = "Richtiger Einbau erfolgt"

# 5
"""
data["ziel_der_abdeckung"] = input.get('#/properties/edi8eb283983de7413b9b8b9530fb227543')
data["art_der_abdeckung"] = input.get('#/properties/edibe53684aba79423cb430632c3423e180')
"""

data["ziel_der_abdeckung"] = "Personenschutz"
data["art_der_abdeckung"] = "isolierende Formteile"


# Kopffragen

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(13, 107)
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

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14.3, 208.3)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_elektrischerschlag"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(72.2, 208.3)
pdf.cell(0, 0, data.get("zusaetzliche_schutzausrüstung_stoerlichtbogen"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(14.4, 231.6)
pdf.cell(0, 0, data.get("abgrenzung_arbeitsbereich_ja"))

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
pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 82.5)
pdf.cell(0, 0, data.get("vorhaengeschloss_schalter"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 89)
pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 94)
pdf.cell(0, 0, data.get("betriebsraum_tuer_verschlossen"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 100.5)
pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 105.5)
pdf.cell(0, 0, data.get("schalten_verboten"))


# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 136)
pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 141)
pdf.cell(0, 0, data.get("spannungspruefer"))

# 4 Geerdet und kurzgeschlossen

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 210)
pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung eingebaut?')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 215)
pdf.cell(0, 0, data.get("euk_wo_eingebaut"))

pdf.set_font('DGUVMeta-Bold', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 221.5)
pdf.cell(0, 0, 'Begründung:')

pdf.set_font('DGUVMeta-Normal', '', 10)
pdf.set_text_color(35,31,32)
pdf.set_xy(12.7, 226.5)
pdf.cell(0, 0, data.get("geerdet_begruendung"))
"""

# 5 Mit der Abdeckung soll erreicht werden

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 170)
pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 175)
pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

pdf.set_font('DGUVMeta-Normal', '', 14)
pdf.set_xy(104, 185)
pdf.cell(0, 0, 'Art der Abdeckung:')

pdf.set_font('DGUVMeta-Normal', 'u', 14)
pdf.set_xy(104, 190)
pdf.cell(0, 0, data.get("art_der_abdeckung"))

"""

pdf.output("elektrohandwerk-schaltanlagen.pdf", "F")