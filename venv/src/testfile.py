import requests

rudi = requests.get('https://devella.uv-kooperation.de/fiverules')
klaus = rudi.json()
import pdb; pdb.set_trace()