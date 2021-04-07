import requests

rudi = requests.get('https://ella.uv-kooperation.de/fiverules')
klaus = rudi.json()
elektrohandwerk = klaus["services"][0]
s143 = elektrohandwerk["services"][0]
import pdb; pdb.set_trace()