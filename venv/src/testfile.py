import requests

fiverules = requests.get('https://devella.uv-kooperation.de/fiverules/s143')
s143 = fiverules.json()
s143_ui = s143["ui"]

for i in s143_ui["elements"]:
    field = i["scope"]
    fieldid = field
    field = dict()

    fieldid = fieldid.split("/")
    fieldid = fieldid[2]

    field["title"] = s143["form"]["properties"][fieldid]["title"]
    field["type"] = s143["form"]["properties"][fieldid]["type"]

    if fieldid in s143["form"]["required"]:
        field["required"] = True
    else:
        field["required"] = False

    import pdb; pdb.set_trace()