from fpdf import FPDF

def create_pdf(input):

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

    data["art_der_freischaltung"] = input.get('#/properties/edidd3eb380f631414b905fb8e056a0918b')

    if data["art_der_freischaltung"] == "NH-Sicherungen":
        data["ausloesestrom"] = input.get('#/properties/edif626707d3b324fe1ab85fd1bc86cc8e9')
    elif data["art_der_freischaltung"] == "NH-Lastschaltleister":
        data["ausloesestrom"] = input.get('#/properties/edib889a8d4a3b14e3d9d382d7c1508636b')
    elif data["art_der_freischaltung"] == "Leistungsschalter":
        data["ausloesestrom"] = input.get('#/properties/edi4efaaefb3fc54ad8b0185b34a5fa7b71')
    else:
        data["ausloesestrom"] = "/"

    data["ort_der_freischaltung"] = input.get('#/properties/edi7f46d0a548664790a147b33f9bd869ce')

    if data["ort_der_freischaltung"] == "Trafostation":
        data["ort_nroderbezeichnung"] = input.get('#/properties/edid17835b08e254f06a1977660b2890a49')
    elif data["ort_der_freischaltung"] == "Umspannwerk/-anlage":
        data["ort_nroderbezeichnung"] = input.get('#/properties/edi1ceb77541181414f9ceff5f32a69edb7')
    elif data["ort_der_freischaltung"] == "Kabelverteilerschrank":
        data["ort_nroderbezeichnung"] = input.get('#/properties/edie90ea64ade3844f2aab5ee5427a88927')
    else:
        data["ort_nroderbezeichnung"] = "/"

    # 2

    data["vorhaengeschloss"] = input.get('#/properties/edib4ab8160289f41819e6d2e55931a7c77')
    data["schalten_verboten"] = input.get('#/properties/edif621189f94544eb39bbf3ce37f9eb679')
    data["entzogene_nhsicherungen"] = input.get('#/properties/edi551233029165465ea737bcf4699b274e')

    # 3

    data["spannungspruefer"] = input.get('#/properties/edifa5cf2794b5b4e0c92096e2ce203fe06')

    # 4

    data["euk_wo_eingebaut"] = input.get('#/properties/edi3878f261fc78423abdd4d1c757dd41be')
    if data["euk_wo_eingebaut"] == "Nicht geerdet und kurzgeschlossen":
        data["geerdet_begruendung"] = input.get('#/properties/edi85ef572ed38942de9bae6cb1d39a4adb')
    else:
        data["geerdet_begruendung"] = ""

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edic4983627bca3448dab434de87ba9778b')

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edi12517bfa3f0644479bf39931b29e6d45'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edic067c6dc4a72401bb697b8aef743229b'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edicfeb2bd66f854a7e9041a54994386181')
        if data.get("art_der_abdeckung") == "die Entfernung beträgt ca.:":
            data["entfernung"] = input.get('#/properties/ediea229e19846b4aedaabc8564a212b4ff')
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 58.5)
    pdf.cell(0, 0, 'Arbeiten an Schaltanlagen der Niederspannung,')

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 68)
    pdf.cell(0, 0, 'z. B. KVS, Trafostation')

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
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 82.5)
    pdf.cell(0, 0, data.get("vorhaengeschloss"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 89)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("schalten_verboten"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wurden ausgebaute NH-Sicherungen unbefugtem Zugriff entzogen, z. B. mitgenommen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("entzogene_nhsicherungen"))

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

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 189)
    pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung eingebaut?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 194)
    pdf.cell(0, 0, data.get("euk_wo_eingebaut"))

    if data["euk_wo_eingebaut"] == "Nicht geerdet und kurzgeschlossen":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35,31,32)
        pdf.set_xy(12.7, 200.5)
        pdf.cell(0, 0, 'Begründung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 205.5)
        pdf.cell(0, 0, data.get("geerdet_begruendung"))

    # 5 Mit der Abdeckung soll erreicht werden

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 235)
    pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 240)
    pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 246.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 251.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 246.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 251.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 246.5)
        pdf.cell(0, 0, 'Keine Abdeckung angebracht, weil:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 251.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))

        if data.get("art_der_abdeckung") == "die Entfernung beträgt ca.:":
            pdf.set_font('DGUVMeta-Normal', '', 10)
            pdf.set_text_color(35, 31, 32)
            pdf.set_xy(12.7, 256.5)
            pdf.cell(0, 0, str(data.get("entfernung") + " Meter"))

    pdf.output("s137.pdf", "F")

if __name__ == "__main__":
    from importdata import evu_niederspannungsschaltanlagen as input
    create_pdf(input)
