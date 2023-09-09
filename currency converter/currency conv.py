from requests import get
from pprint import PrettyPrinter 

BASE_URL = "https://free.currconv.com/"
API_KEY = "ef7dabd5088a0dc9bc6e"

printer = PrettyPrinter()

def getcurrency():
    endpoint = f"/api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    printer.pprint(data)

getcurrency()

  








