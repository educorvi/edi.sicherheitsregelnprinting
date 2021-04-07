from fpdf import FPDF

def create_pdf(input):

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.add_font('DGUVMeta-Normal', '', 'DGUVMeta-Normal.ttf', uni=True)
    pdf.add_font('DGUVMeta-Bold', '', 'DGUVMeta-Bold.ttf', uni=True)
    pdf.add_font('DGUVMeta-NormalItalic', '', 'DGUVMeta-NormalItalic.ttf', uni=True)

    pdf.image("newtemplate2_seite1.jpg", x=-4, y=-8, w=217, h=313)

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

    # 1

    data["art_der_freischaltung"] = input.get('#/properties/edi913c7b7064874fe788ced88ff0566392')

    if data["art_der_freischaltung"] == "NH-Sicherungen":
        data["ausloesestrom"] = input.get('#/properties/ediac93b1a15dc34f6faa18c203f9a00049')
    elif data["art_der_freischaltung"] == "Schraubsicherungen":
        data["ausloesestrom"] = input.get('#/properties/edic96044edb86143c6855f5b0a89d33577')
    elif data["art_der_freischaltung"] == "SLS-Schalter":
        data["ausloesestrom"] = input.get('#/properties/edi32d649c1c4fb422f8c868e47f905f7d0')
    elif data["art_der_freischaltung"] == "Trenner geöffnet":
        data["ausloesestrom"] = input.get('#/properties/edi898bfa6b08564c569e22437b853b6632')
    else:
        data["ausloesestrom"] = "/"

    data["ort_der_freischaltung"] = input.get('#/properties/edid693e96632ce48548a14e9215ba73a34')

    # 2

    data["schalten_verboten"] = input.get('#/properties/edi5e1db87b6ba84b9480d006df28e6150c')

    # 3

    data["spannungspruefer"] = input.get('#/properties/edica7f37a7fd3546b1bbe137efc4e0c920')
    data["rueckspannung"] = input.get('#/properties/edi8c6b921bfaad450d968cf330bc85f998')
    data["usv"] = input.get('#/properties/edie2a09ff90b8d420b8ccad52756e2e9aa')

    # 4

    data["euk"] = input.get('#/properties/edieb6c9063a1914cd1adcee7d46b81ed49')
    if data["euk"] == "nicht geerdet und kurzgeschlossen":
        data["geerdet_begruendung"] = input.get('#/properties/edida248b77b1f6458dab42a69b0485ced4')
    else:
        data["geerdet_begruendung"] = ""

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edi5609a18d6bbc4fc69bcd7c4d7fdac251')

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edifba255e4d77d4062913dd6a403987972'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edi6f273b360fee47849dac4e4cec88356e'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edi954994e18e77435aa5a3486363e24bc4')
        if data.get("art_der_abdeckung") == "die Entfernung beträgt ca.:":
            data["entfernung"] = input.get('#/properties/edid6c093eee3be4405b84296381c045ed8')
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 63.25)
    pdf.cell(0, 0, 'Arbeiten an Zähleranlagen')

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

    #Adding new page

    pdf.add_page()
    pdf.image("newtemplate6_seite2.jpg", x=-4, y=-8, w=217, h=313)

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

    # 2 Gegen Wiedereinschalten gesichert

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 77.5)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 82.5)
    pdf.cell(0, 0, data.get("schalten_verboten"))

    # 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 110)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 115)
    pdf.cell(0, 0, data.get("spannungspruefer"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 121.5)
    pdf.cell(0, 0, 'Rückspannung von benachbarten Zählerfeldern möglich?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 126.5)
    pdf.cell(0, 0, data.get("rueckspannung"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 133)
    pdf.cell(0, 0, 'Dezentrale Einspeisung vorhanden, z. B. USV, PV, Notstromaggregat?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 138)
    pdf.cell(0, 0, data.get("usv"))

    # 4 Geerdet und kurzgeschlossen

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 189)
    pdf.cell(0, 0, 'Wurde eine EuK-Vorrichtung eingebaut, z. B. im HAK?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 194)
    pdf.cell(0, 0, data.get("euk"))

    if data["euk"] == "nicht geerdet und kurzgeschlossen":
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

    pdf.output("s136.pdf", "F")

if __name__ == "__main__":
    from importdata import zaehleranlagen as input
    create_pdf(input)