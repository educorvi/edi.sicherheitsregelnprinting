import requests

fiverules = requests.get('https://devella.uv-kooperation.de/fiverules/s143')
s143 = fiverules.json()
s143_ui = s143["ui"]

fieldslist = []
internalfields = []

variable = 0
for k in s143_ui["elements"]:
    fieldset = dict()
    fieldset[k["type"]] = dict()
    #import pdb; pdb.set_trace()
    for i in s143_ui["elements"][variable]["elements"]:
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
    fieldset[k["type"]] = internalfields
    fieldslist.append(fieldset)
    variable = variable + 1

#import pdb; pdb.set_trace()
print(fieldslist)