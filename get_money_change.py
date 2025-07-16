'''
This archive we obtain the change official of Banco de México and Update the File
'''

import os
from datetime import date
import requests
from functions.query import query

url = "https://cdn.dinero.today/api/banxico_fix.json" # We need the url from 

os.system("cls") if os.name == "nt" else os.system("clear") # clear the console
today = str(date.today())

response = requests.get(url, "USD")

if response.status_code == 200:
    data = response.json()
    mxn = str(data['rates']['MXN'])
    query(f"UPDATE dbo.DateDimension SET TipoCambio = '{mxn}' WHERE Date = '{today}';")
else:
    print(f"Error: {response.status_code}")