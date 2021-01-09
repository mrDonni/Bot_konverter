import requests
import json
import lxml.html
from lxml import etree
from config import currency

r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}')




print(r.content)

