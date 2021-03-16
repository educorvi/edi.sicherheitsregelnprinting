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

    data["art_der_freischaltung1a"] = input.get('#/properties/edi6a8f77755207467090eddf15f6a21e87')

    if data["art_der_freischaltung1a"] == "NH-Sicherungen":
        data["ausloesestrom1a"] = input.get('#/properties/edibedde3faf5304b9bb0101e9b23f5d284')
    elif data["art_der_freischaltung1a"] == "NH-Lastschaltleiste":
        data["ausloesestrom1a"] = input.get('#/properties/edi78c896ef894445108dc67298d8b3318c')
    elif data["art_der_freischaltung1a"] == "Leistungsschalter":
        data["ausloesestrom1a"] = input.get('#/properties/edi58255093bbca48999e2aaae5462f3c82')
    else:
        data["ausloesestrom1a"] = "/"

    data["ort_der_freischaltung1a"] = input.get('#/properties/edi1c959df02d0e4f65ac31465aed4ed8c6')

    if data["ort_der_freischaltung1a"] == "Kabelverteilerschrank":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi424a0be1228145318070ee2f83c7b639')
    elif data["ort_der_freischaltung1a"] == "Trafostation":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi5a9acfa863614586845b7fd9918cafc8')
    elif data["ort_der_freischaltung1a"] == "Kompaktstation":
        data["nroderbezeichnung1a"] = input.get('#/properties/edi1af11b6f7ca74a85a9f8c1888071215f')

    data["zusaetzlichfreigeschaltet1a"] = input.get('#/properties/edi39026745e38e4279b3113e51c8d76d50')

    if data["zusaetzlichfreigeschaltet1a"] == ['im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)']:
        data["zusaetzlichfreigeschaltet1a"] = 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)'
    else:
        data["zusaetzlichfreigeschaltet1a"] = ''

    # 1B

    data["art_der_freischaltung1b"] = input.get('#/properties/ediaa9552464dcf4b7f96903f645ed53b63')

    if data["art_der_freischaltung1b"] == "NH-Sicherungen":
        data["ausloesestrom1b"] = input.get('#/properties/edi1cb1f54ea8e041ff85d4b19d46b54f2d')
    elif data["art_der_freischaltung1b"] == "NH-Lastschaltleiste":
        data["ausloesestrom1b"] = input.get('#/properties/edi378aec1700974f628e5a08c2b2f63d6c')
    elif data["art_der_freischaltung1b"] == "Leistungsschalter":
        data["ausloesestrom1b"] = input.get('#/properties/edi004df17a3e1e4d299e0bd5123f0f18d0')
    else:
        data["ausloesestrom1b"] = "/"

    data["ort_der_freischaltung1b"] = input.get('#/properties/edicda586dcbda14b88863b1e780bdcf787')

    if data["ort_der_freischaltung1b"] == "Kabelverteilerschrank":
        data["nroderbezeichnung1b"] = input.get('#/properties/edif856292285394eb7920585f54d02644a')
    elif data["ort_der_freischaltung1b"] == "Trafostation":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi099d5d84e51e4e638fe8c175a2542e9f')
    elif data["ort_der_freischaltung1b"] == "Kompaktstation":
        data["nroderbezeichnung1b"] = input.get('#/properties/edi017c5fa9e6cc48f284d71bf87d3e9d7f')

    data["zusaetzlichfreigeschaltet1b"] = input.get('#/properties/edid0995ee6abad4deeb59519bfb7440c32')

    if data["zusaetzlichfreigeschaltet1b"] == ['im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)']:
        data["zusaetzlichfreigeschaltet1b"] = 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)'
    else:
        data["zusaetzlichfreigeschaltet1b"] = ''

    # 2A

    data["schloss2a"] = input.get('#/properties/edi6b58b8a2d67a43b69428560b9814730b')
    data["schalten_verboten2a"] = input.get('#/properties/edie1a1691433504d06ada6e73dbe580d80')

    # 2B

    data["schloss2b"] = input.get('#/properties/edibd10b6f4f90a4786b3753ed927e45f44')
    data["schalten_verboten2b"] = input.get('#/properties/edie9bfd532c7724f989e9841c8dc9b8425')

    # 3A

    data["spannungspruefer3a"] = input.get('#/properties/edi2ab6fcfb494f483bbc0d3bc735e7d8cd')

    # 3B

    data["spannungspruefer3b"] = input.get('#/properties/edi8c4fababb3cd4426894252045c83d088')

    # 3C

    data["pruefungsart3c"] = input.get('#/properties/edib201ffc9d8154fd5ba5982f8c1e9ad7a')

    if data["pruefungsart3c"] == "Andere Methode":
        data["erlauterung3c"] = input.get('#/properties/edi8b65c32610b7485aa4475e7aea8921b5')
    else:
        data["erlauterung3c"] = ""

    # 4

    data["euk_wo"] = input.get('#/properties/edice9c36613f404d818c5f11a72028d86e')

    if data["euk_wo"] == "Nicht geerdet und kurzentschlossen":
        data["euk_begruendung"] = input.get('#/properties/edi32732bbb05eb4ad6a23ad8ca3a6ce6af')

    # 5

    data["ziel_der_abdeckung"] = input.get('#/properties/edi083dd47e5405445d9d452b34d5bfd82c')

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edic7f067d9bb594c618d6d8c5d96b1d9fc'))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        data["art_der_abdeckung"] = ', '.join(input.get('#/properties/edi18d247e0ad8f4e90b205425be8b4f259'))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        data["art_der_abdeckung"] = input.get('#/properties/edifa3e5b24ed8a433ea4f2b63fa2c9407f')
        if data.get("art_der_abdeckung") == "die Entfernung beträgt ca.:":
            data["entfernung"] = input.get('#/properties/edi448aa2c4d1dc4141bbe961fa1456cab2')
    else:
        data["art_der_abdeckung"] = ""

    # Title

    pdf.set_font('DGUVMeta-Bold', '', 20)
    pdf.set_text_color(0,73,148)
    pdf.set_xy(12.7, 63.25)
    pdf.cell(0, 0, 'Arbeiten an Kabeln in der Niederspannung')

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
    pdf.image("newtemplate7_seite2.jpg", x=-4, y=-8, w=217, h=313)

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

    if data["zusaetzlichfreigeschaltet1a"] == 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)':
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 63.7)
        pdf.cell(0, 0, 'Zusätzlich freigeschaltet:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 68.7)
        pdf.cell(0, 0, data.get("zusaetzlichfreigeschaltet1a"))
    else:
        data["zusaetzlichfreigeschaltet1a"] = ''

    # 1b Freigeschaltet Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 89)
    pdf.cell(0, 0, 'Wie erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, data.get("art_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 100.5)
    pdf.cell(0, 0, 'Wo erfolgte die Freischaltung?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 105.5)
    pdf.cell(0, 0, data.get("ort_der_freischaltung1b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 112)
    pdf.cell(0, 0, 'Nr. oder Bezeichnung:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 117)
    pdf.cell(0, 0, data.get("nroderbezeichnung1b"))

    if data["zusaetzlichfreigeschaltet1b"] == 'im Hausanschlusskasten (wegen dezentraler Einspeisung, z. B. PV-Anlage, BHKW)':
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 123.5)
        pdf.cell(0, 0, 'Zusätzlich freigeschaltet:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 128.5)
        pdf.cell(0, 0, data.get("zusaetzlichfreigeschaltet1b"))
    else:
        data["zusaetzlichfreigeschaltet1b"] = ''

    # 2a Gegen Wiedereinschalten gesichert Ausschaltstelle 1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 147.5)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am (Leistungs-) Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 152.5)
    pdf.cell(0, 0, data.get("schloss2a"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 159)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 164)
    pdf.cell(0, 0, data.get("schalten_verboten2a"))

    # 2b Gegen Wiedereinschalten gesichert Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 196)
    pdf.cell(0, 0, 'Wurde ein Vorhängeschloss am (Leistungs-) Schalter eingehängt und abgeschlossen?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 201)
    pdf.cell(0, 0, data.get("schloss2b"))

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 207.5)
    pdf.cell(0, 0, 'Wurde ein Schild "Schalten verboten" zusätzlich angebracht?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 212.5)
    pdf.cell(0, 0, data.get("schalten_verboten2b"))

    # 3a Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle1

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 256)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 261)
    pdf.cell(0, 0, data.get("spannungspruefer3a"))

    # Adding new page

    pdf.add_page()
    pdf.image("newtemplate7_seite3.jpg", x=-4, y=-8, w=217, h=313)

    # 3b Spannungsfreiheit allpolig festgestellt an der Ausschaltstelle 2

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 22)
    pdf.cell(0, 0, 'Zweipoliger Spannungsprüfer:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 27)
    pdf.cell(0, 0, data.get("spannungspruefer3b"))

    # 3c Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 50)
    pdf.cell(0, 0, 'Wie wurde geprüft?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 55)
    pdf.cell(0, 0, data.get("pruefungsart3c"))

    if data["pruefungsart3c"] == "Andere Methode":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 61.5)
        pdf.cell(0, 0, 'Erläuterung der Methode')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 66.5)
        pdf.cell(0, 0, data.get("erlauterung3c"))

    # 4 Geerdet und kurzgeschlossen an den Ausschaltstellen

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 94)
    pdf.cell(0, 0, 'Wo wurde die EuK-Vorrichtung in die NH-Sicherungsunterteile eingebaut?')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 99)
    pdf.cell(0, 0, data.get("euk_wo"))

    if data["euk_wo"] == "Nicht geerdet und kurzentschlossen":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 105.5)
        pdf.cell(0, 0, 'Begründung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 110.5)
        pdf.cell(0, 0, data.get("euk_begruendung"))

    # 5 Mit der Abdeckung soll erreicht werden

    pdf.set_font('DGUVMeta-Bold', '', 10)
    pdf.set_text_color(35,31,32)
    pdf.set_xy(12.7, 139)
    pdf.cell(0, 0, 'Mit der Abdeckung soll erreicht werden:')

    pdf.set_font('DGUVMeta-Normal', '', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(12.7, 144)
    pdf.cell(0, 0, data.get("ziel_der_abdeckung"))

    if data["ziel_der_abdeckung"] == "teilweiser Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 150.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 155.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "vollständiger Berührungsschutz":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 150.5)
        pdf.cell(0, 0, 'Art der Abdeckung:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 155.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))
    elif data["ziel_der_abdeckung"] == "Abdeckung nicht notwendig":
        pdf.set_font('DGUVMeta-Bold', '', 10)
        pdf.set_text_color(35, 31, 32)
        pdf.set_xy(12.7, 150.5)
        pdf.cell(0, 0, 'Keine Abdeckung angebracht, weil:')

        pdf.set_font('DGUVMeta-Normal', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(12.7, 155.5)
        pdf.cell(0, 0, data.get("art_der_abdeckung"))

        if data.get("art_der_abdeckung") == "die Entfernung beträgt ca.:":
            pdf.set_font('DGUVMeta-Normal', '', 10)
            pdf.set_text_color(35, 31, 32)
            pdf.set_xy(12.7, 160.5)
            pdf.cell(0, 0, str(data.get("entfernung") + " Meter"))

    pdf.output("s138.pdf", "F")

if __name__ == "__main__":
    from importdata import evu_niederspannungskabel as input
    create_pdf(input)