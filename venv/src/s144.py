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

    data["art_der_freischaltung"] = input.get('#/properties/edi4961450e44ba4d16aeb015a919e73f0a')

    if data["art_der_freischaltung"] == "NH-Sicherungen":
        data["ausloesestrom"] = input.get('#/properties/edibe2aabe1258d47b585d178a186601fc3')
    elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
        data["ausloesestrom"] = input.get('#/properties/edib93efcc9a763409c9d3e8357a8774554')
    elif data["art_der_freischaltung"] == "Schraubsicherungen":
        data["ausloesestrom"] = input.get('#/properties/edic980387b0bd741e2ac4a15e7e4b6cc2e')
    else:
        data["ausloesestrom"] = "/"

    data["ort_der_freischaltung"] = input.get('#/properties/edi2e32c9143f91464392d3ea5b72c1db89')

    if data["ort_der_freischaltung"] == "Hauptverteilung":
        data["ort_nroderbezeichnung"] = input.get('#/properties/edi32c21570304b4f0d911d02b8a8046d0c')
    elif data["ort_der_freischaltung"] == "Unterverteilung":
        data["ort_nroderbezeichnung"] = input.get('#/properties/edi6ba4422c3dad4ea2a5ed921a02764123')
    else:
        data["ort_nroderbezeichnung"] = "/"

    # 2

    data["sperrelement"] = input.get('#/properties/edi36e713d0f0544afab38414b8d139fcec')
    data["betriebsraum_tuer_verschlossen"] = input.get('#/properties/edi8aeb082703364653b77ecedfb294800c')
    data["schalten_verboten"] = input.get('#/properties/ediff3de7cc99c74d7a8d7fc9430714cc4d')

    # 3

    data["spannungspruefer"] = input.get('#/properties/edi9b0ea2910d514df791e528597a6e5f28')
    data["usv"] = input.get('#/properties/edi94283112763649bda0ef6f900ddc2cbc')

    # 4

    data["euk_wo_eingebaut"] = input.get('#/properties/edibba761f4767d4a3b9f1528712f8f1abe')
    if data["euk_wo_eingebaut"] == "Nicht geerdet und kurzgeschlossen":
        data["geerdet_begruendung"] = input.get('#/properties/edi1941312f7bf04fa5996ec5eb018f4c78')
    else:
        data["geerdet_begruendung"] = ""

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edi94f9841893d04f6184e06a9b57797e59')

    if data["ziel_der_abdeckung"] == "ausreichender Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edib6c44b7e15b043ec9dff1538ffc40229'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edifc9c22900aa44e15b334d724a0c3eed6'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edi66bace84743b4078b2aa9941828b96d6')
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 58.5)
    pdf.cell(0, 0, 'Arbeiten an Unterverteilungen')

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 68)
    pdf.cell(0, 0, 'in der Niederspannung')

    pdf.set_font('DGUVMeta-Bold', '', 14)
    pdf.set_text_color(0,140,142)
    pdf.set_xy(12.7, 83.5)
    pdf.cell(0, 0, 'Elektrohandwerk')

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
    pdf.cell(0, 0, 'Wurde ein Sperrelement eingesetzt, weil der Bereich für Laien zugänglich ist?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 82.5)
    pdf.cell(0, 0, data.get("sperrelement"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 89)
    pdf.cell(0, 0, 'Wurde die Tür zum elektrischen Betriebsraum verschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("betriebsraum_tuer_verschlossen"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("schalten_verboten"))

    # 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 136)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 141)
    pdf.cell(0, 0, data.get("spannungspruefer"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 147.5)
    pdf.cell(0, 0, 'Dezentrale Einspeisung vorhanden, z. B. USV, PV, Notstromaggregat?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 152.5)
    pdf.cell(0, 0, data.get("usv"))

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
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 205.5)
    pdf.cell(0, 0, data.get("geerdet_begruendung"))

    # 5 Mit der Abdeckung soll erreicht werden

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 236.6)
    pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 241.6)
    pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 248.1)
    if data["ziel_der_abdeckung"] != "Abdeckung nicht notwendig":
        pdf.cell(0, 0, 'Art der Abdeckung:')
    else:
        pdf.cell(0, 0, 'keine Abdeckung angebracht, weil:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 253.1)
    pdf.cell(0, 0, data.get("art_der_abdeckung"))

    pdf.output("s144.pdf", "F")

if __name__ == "__main__":
    from importdata import unterverteilung as input
    create_pdf(input)