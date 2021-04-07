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

    # 1

    data["art_der_freischaltung"] = input.get('#/properties/edi151f290f01614c52ba070de4f768e1f9')

    if data["art_der_freischaltung"] == "LS-Schalter":
        data["ausloesestrom"] = input.get('#/properties/edi6a3941bb2cb141c4a16da7f789e8b592')
    elif data["art_der_freischaltung"] == "NH-Lastschaltleiste":
        data["ausloesestrom"] = input.get('#/properties/edi42d201e511d244929df7a7a4f87c01a0')
    elif data["art_der_freischaltung"] == "Schraubsicherungen":
        data["ausloesestrom"] = input.get('#/properties/edi3ad9b1c2693846999813e01fb7b491fa')
    else:
        data["ausloesestrom"] = "/"

    data["ort_der_freischaltung"] = input.get('#/properties/edi17b019e086414ea48e6be09cb1fd27a1')

    # 2

    data["sperrelement"] = input.get('#/properties/edi776a057f1ac34a029366024d194d1f78')
    data["schaltsperre"] = input.get('#/properties/edi70573b75d5564f3c8f8fdbc18587f789')
    data["reparaturschalter"] = input.get('#/properties/edi6d1af6f810f640d981df099510d1ce34')
    data["schalten_verboten"] = input.get('#/properties/edi028811b628af49e880cffa21a1fc62bb')

    # 3

    data["spannungspruefer"] = input.get('#/properties/edi5176dc0fe64f4fa1a2b31ce19e29403f')

    # 4

    data["euk_wo_eingebaut"] = input.get('#/properties/edi4deef32aa18848f68fa0ab082a88f141')
    if data["euk_wo_eingebaut"] == "Nicht geerdet und kurzgeschlossen":
        data["geerdet_begruendung"] = input.get('#/properties/edi5e66ed0080b74d80af012ad33cde01f6')
    else:
        data["geerdet_begruendung"] = ""

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edicb98d6e5aadb415b8a13ba97621832ef')

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edidf6523c6c376412b8502d346715aa3ee'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edi48105f3d939e4d6c9d7a483ab1e38675'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edi498bef640c6a45008d44d5992a3a21ac')
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 58.5)
    pdf.cell(0, 0, 'Arbeiten an elektrischen Betriebsmitteln,')

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 68)
    pdf.cell(0, 0, 'z. B. Werkzeugmaschinen')

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
    pdf.cell(0, 0, 'Wurde eine Schaltsperre eingesetzt, weil der Bereich für Laien zugänglich ist?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("schaltsperre"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wurde ein Reparaturschalter mit einem Vorhängeschloss versehen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("reparaturschalter"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 112)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 117)
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


    pdf.output("s146.pdf", "F")

if __name__ == "__main__":
    from importdata import elektrische_betriebsmittel as input
    create_pdf(input)