import requests

fiverules = requests.get('https://ella.uv-kooperation.de/fiverules')
fiverulesjson = fiverules.json()
elektrohandwerk = fiverulesjson["services"][0]
s143 = elektrohandwerk["services"][0]
s143_ui = s143["ui"]
import pdb; pdb.set_trace()