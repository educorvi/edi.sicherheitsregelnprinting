from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

pdf.image("vorlage5-Seite1.jpg", x=-4, y=-8, w=217, h=313)

data = {}
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

#Adding new page

pdf.add_page()
pdf.image("vorlage5-Seite2.jpg", x=-4, y=-8, w=217, h=313)

# 2 Gegen Wiedereinschalten gesichert

"""
to be filled
"""

# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

"""
to be filled
"""

# 4 Geerdet und kurzgeschlossen

"""
to be filled
"""

# 5 Mit der Abdeckung soll erreicht werden

"""
to be filled
"""

pdf.output("unterverteilungen.pdf", "F")