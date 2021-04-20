import requests

import time
from reportlab.lib import colors
from reportlab.lib.colors import Color, black, blue, red
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("reportlabtest.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

fiverules = requests.get('https://devella.uv-kooperation.de/fiverules/s143')
s143 = fiverules.json()
s143_ui = s143["ui"]

result = {"data":{"#/properties/arbeitsstelle-arbeitsort":"educorvi GmbH","#/properties/datum-und-uhrzeit":"2020-09-30T16:00","#/properties/person-in-der-rolle-des-anlagenverantwortlichen":"Lars","#/properties/person-in-der-rolle-des-arbeitsverantwortlichen":"Lars Walther","#/properties/arbeitsausfuhrende-person":"Seppo Walther","#/properties/zusatzliche-personliche-schutzausrustung":["gegen elektrischen Schlag","gegen Störlichtbogen"],"#/properties/wurde-der-arbeitsbereich-z-b-mit-ketten-oder":"ja","#/properties/edi43ba285a6396493da82241d5ecec090d":"NH-Sicherungen","#/properties/edi812abac1f12d44d18d4415cb1ddb1984":"16","#/properties/edib290d1801a964d8ab3e277a056cd793c":"25","#/properties/edi2b6d1b411a05466e8e3ce4def7b3879c":"19","#/properties/edi7bd23a69de5141aaa4379b4ba2b979ba":"Umspannwerk/-anlage","#/properties/edi3dc9a71b7dc547d6a55d036bd2417578":"Rudi","#/properties/edi69d788c9284e4a20b54819018aa0f5c4":"Klausi","#/properties/edidca06063234648e1b3b54c803a5b99ea":"Tiberius","#/properties/edic589597967b44e00af9e74c7c1319cb0":"nein","#/properties/edi64719875ff504d6eb8fd735f12fd7d17":"ja","#/properties/edi6af7fbabb2a44046b882d580080326e1":"magnetisch","#/properties/edi594b8869f8884cb4b76d376d960c3b74":"3M Voltsarecool","#/properties/ediec7dc4dfa3b646818f003c01c9f1709c":"an der Sammelschiene","#/properties/edibc2aa174fac14dc68fdce90b73990e62":"Weil halt","#/properties/edi8eb283983de7413b9b8b9530fb227543":"vollständiger Berührungsschutz","#/properties/edibe53684aba79423cb430632c3423e180":["isolierende Tücher"],"#/properties/edi30fb04c107ff4509bdddd00f9ab97add":"die Entfernung beträgt ca.:","#/properties/edi5a400e3cf88f490eac52f010595976ef":"17"},"name":"s143"}
result = result["data"]

fieldslist = []

Story = []
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

variable = 0
for k in s143_ui["elements"]:
    fieldset = dict()
    fieldset["fieldsettype"] = k["type"]
    try:
        fieldset["fieldsetname"] = k["label"]
    except:
        pass
    fieldset["fields"] = dict()
    internalfields = []
    for i in k["elements"]:
        field = i["scope"]
        fieldid = field
        field = dict()

        fieldid2 = fieldid.split("/")
        fieldid2 = fieldid2[2]

        field["id"] = fieldid2
        field["title"] = s143["form"]["properties"][fieldid2]["title"]
        field["type"] = s143["form"]["properties"][fieldid2]["type"]
        try:
            field["result"] = result[fieldid]
        except:
            pass

        if fieldid2 in s143["form"]["required"]:
            field["required"] = True
        else:
            field["required"] = False

        internalfields.append(field)
    fieldset["fields"] = internalfields
    fieldslist.append(fieldset)

print(fieldslist)

def fieldhandling(f):
    Story.append(Paragraph(f["title"], styles["Normal"]))
    try:
        if isinstance(f["result"], list):
            Story.append(Paragraph(', '.join(f["result"]), styles["Normal"]))
        else:
            Story.append(Paragraph(str(f["result"]), styles["Normal"]))
    except:
        pass
    Story.append(Spacer(1, 8))

def separator():
    separator = ((".") * 164)
    Story.append(Paragraph(separator, styles["Normal"]))
    Story.append(Paragraph(klaus, styles["Heading2"]))
    Story.append(Spacer(1, 12))

def logo():
    logo = "logo.png"
    im = Image(logo, 100, 50)
    Story.append(im)

Story = []

logo()

for i in fieldslist:

    # Fieldset
    try:
        klaus = i["fieldsetname"]
    except:
        klaus = "Kopffragen"

    separator()

    for f in i["fields"]:
        fieldhandling(f)

doc.build(Story)