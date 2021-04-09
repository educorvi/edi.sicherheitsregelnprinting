import requests

import time
from reportlab.lib.enums import TA_JUSTIFY
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

fieldslist = []

Story = []
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

variable = 0
for k in s143_ui["elements"]:
    #import pdb; pdb.set_trace()
    fieldset = dict()
    fieldset["fieldsettype"] = k["type"]
    try:
        fieldset["fieldsetname"] = k["label"]
    except:
        pass
    fieldset["fields"] = dict()
    #import pdb; pdb.set_trace()
    internalfields = []
    for i in k["elements"]:
        #import pdb; pdb.set_trace()
        field = i["scope"]
        fieldid = field
        field = dict()

        fieldid = fieldid.split("/")
        fieldid = fieldid[2]

        field["id"] = fieldid
        field["title"] = s143["form"]["properties"][fieldid]["title"]
        field["type"] = s143["form"]["properties"][fieldid]["type"]

        if fieldid in s143["form"]["required"]:
            field["required"] = True
        else:
            field["required"] = False

        internalfields.append(field)
        #import pdb; pdb.set_trace()
        #variable = variable + 1
    fieldset["fields"] = internalfields
    fieldslist.append(fieldset)

print(fieldslist)
#import pdb; pdb.set_trace()

for i in fieldslist:
    try:
        klaus = i["fieldsetname"]
    except:
        klaus = "Kopffragen"
    Story.append(Paragraph(klaus, styles["Heading2"]))
    Story.append(Spacer(1, 12))

    for f in i["fields"]:
        Story.append(Paragraph(f["title"], styles["Normal"]))
        Story.append(Spacer(1, 12))

doc.build(Story)