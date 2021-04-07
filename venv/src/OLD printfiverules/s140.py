#4 Tippfehler?

from fpdf import FPDF

def create_pdf(input):

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

    data["art_der_freischaltung1b"] = input.get('#/properties/edi0df2502e80594c2d9df307d0f939562f')

    if data["art_der_freischaltung1b"] == "NH-Sicherungen":
        data["ausloesestrom1b"] = input.get('#/properties/edi7b8b089113024ab69c2133a6295219a8')
    elif data["art_der_freischaltung1b"] == "NH-Lastschaltleiste":
        data["ausloesestrom1b"] = input.get('#/properties/edi71229e67f15042d49d1bedbab36e5e9d')
    elif data["art_der_freischaltung1b"] == "Leistungsschalter":
        data["ausloesestrom1b"] = input.get('#/properties/edid7c9a6a76c3d453ca2454be566b04301')
    else:
        data["ausloesestrom1b"] = "/"

    data["ort_der_freischaltung1b"] = input.get('#/properties/edicbf3dd9390984bf8813716bbe56b59ee')

    if data["ort_der_freischaltung1b"] == "Kabelverteilerschrank":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi022ee3cb58684aafa3cdf0fc711db5c6')
    elif data["ort_der_freischaltung1b"] == "Trafostation":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi62df182f4cc542b294471fd7e02e13ba')
    elif data["ort_der_freischaltung1b"] == "Niederspannungs-Hauptverteilung":
        data["nroderbezeichnung1b"] = input.get('#/properties/edia32c8b9872cd482ba67cfcadbddaea90')
    elif data["ort_der_freischaltung1b"] == "Niederspannungs-Schaltstation":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi202c14b3bb1241dc819115fd5b8bc8f6')

    # 2A

    data["sicherungsart2a"] = input.get('#/properties/edi768f4be54bbd4240b2dd16399e55f066')
    data["schloss2a"] = input.get('#/properties/edica45a1857afe4978b343dbd395cde252')
    data["schalten_verboten2a"] = input.get('#/properties/edi1326f85283674efab4f65b147f6ccc3a')

    # 2B

    data["sicherungsart2b"] = input.get('#/properties/edi8d73b9ab15f745a2ba818fbff946d9d5')
    data["schloss2b"] = input.get('#/properties/edia339c41b72c74c01a6e0165eec4b0b10')
    data["schalten_verboten2b"] = input.get('#/properties/edi6f75580051fe46818f92df966464667e')

    # 3A

    data["spannungspruefer3a"] = input.get('#/properties/edi571f6a3a096845bcafca86ab6739ddcd')

    # 3B

    data["spannungspruefer3b"] = input.get('#/properties/edief48d58a0dd6465996714a0b51a39937')

    # 3C

    data["pruefungsart3c"] = input.get('#/properties/edifc55d559eeb0405bba483ccb9193197d')

    if data["pruefungsart3c"] == "Andere Methode":
        data["erlauterung3c"] = input.get('#/properties/edi3f2fdb49ce7a4357925e3f3abf998f94')
    else:
        data["erlauterung3c"] = ""

    # 4

    data["euk_wo"] = input.get('#/properties/edi6b1886d59d804474b114fae396943ef7')

    if data["euk_wo"] == "Nicht geerdet und kurzentschlossen":
        data["euk_begruendung"] = input.get('#/properties/edid49863db8c2c40a3a824f3302bfcb217')

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edibbe242b53c1e4c20ac98cf1fccf1b44e')

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edicc76c15eb6f547a798da96afdaa62ebf'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edibcbcfe207cfb4ac3b55c1e65f6509f2c'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edidb001b83c10742d89663636aa256f689')

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 58.5)
    pdf.cell(0, 0, 'Arbeiten an Kabeln')

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 68)
    pdf.cell(0, 0, 'in der Niederspannung')

    """
    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 63.25)
    pdf.cell(0, 0, 'Arbeiten an Kabeln in der Niederspannung')
    """

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

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 78)
    pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 83)
    pdf.cell(0, 0, data.get("art_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 89.5)
    pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94.5)
    pdf.cell(0, 0, data.get("ort_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 101)
    pdf.cell(0, 0, 'Nr. oder Bezeichnung:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 106)
    pdf.cell(0, 0, data.get("nroderbezeichnung1b"))

    # 2a Gegen Wiedereinschalten gesichert Ausschaltstelle 1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 130)
    pdf.cell(0, 0, 'Wie wurde gesichert?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 135)
    pdf.cell(0, 0, data.get("sicherungsart2a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 141.5)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am (Leistungs-) Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 146.5)
    pdf.cell(0, 0, data.get("schloss2a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 153)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 158)
    pdf.cell(0, 0, data.get("schalten_verboten2a"))

    # 2b Gegen Wiedereinschalten gesichert Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 179)
    pdf.cell(0, 0, 'Wie wurde gesichert?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 184)
    pdf.cell(0, 0, data.get("sicherungsart2b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 190.5)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am (Leistungs-) Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 195.5)
    pdf.cell(0, 0, data.get("schloss2b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 202)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 207)
    pdf.cell(0, 0, data.get("schalten_verboten2b"))

    # 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 238)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 243)
    pdf.cell(0, 0, data.get("spannungspruefer3a"))

    # 3b Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 266)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 271)
    pdf.cell(0, 0, data.get("spannungspruefer3b"))

    # Adding new page

    pdf.add_page()
    pdf.image("newtemplate3_seite3.jpg", x=-4, y=-8, w=217, h=313)

    # 3c Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 28)
    pdf.cell(0, 0, 'Wie wurde geprüft?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 33)
    pdf.cell(0, 0, data.get("pruefungsart3c"))

    if data["pruefungsart3c"] == "Andere Methode":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 39.5)
        pdf.cell(0, 0, 'Erläuterung der Methode')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 44.5)
        pdf.cell(0, 0, data.get("erlauterung3c"))

    # 4 Geerdet und kurzgeschlossen an den Ausschaltstellen

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 70)
    pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung in die NH-Sicherungsunterteile eingebaut?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 75)
    pdf.cell(0, 0, data.get("euk_wo"))

    if data["euk_wo"] == "Nicht geerdet und kurzentschlossen":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 81.5)
        pdf.cell(0, 0, 'Begründung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 86.5)
        pdf.cell(0, 0, data.get("euk_begruendung"))

    # 5 Mit der Abdeckung soll erreicht werden

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 113)
    pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 118)
    pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 124.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 129.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 124.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 129.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 124.5)
        pdf.cell(0, 0, 'Begründung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 129.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))

    pdf.output("s140.pdf", "F")

if __name__ == "__main__":
    from importdata import niederspannungskabel as input
    create_pdf(input)