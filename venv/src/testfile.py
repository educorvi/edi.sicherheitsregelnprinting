import requests
from fpdf import FPDF

fiverules = requests.get('https://devella.uv-kooperation.de/fiverules/s143')
s143 = fiverules.json()
s143_ui = s143["ui"]

fieldslist = []

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
import pdb; pdb.set_trace()

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

height = 20
height2 = 80
for i in fieldslist:
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(20, height)
    try:
        klaus = i["fieldsetname"]
    except:
        klaus = "Kopffragen"
    pdf.cell(0, 0, klaus)
    height = height + 10

    for f in i["fields"]:
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(20, height2)
        pdf.cell(0, 0, f["title"])
        height2 = height2 + 5

pdf.output("s143.pdf", "F")