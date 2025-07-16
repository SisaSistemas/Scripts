'''
This archive we obtain the change official of Banco de México and Update the File
'''

import os
from datetime import date
import requests
from functions.query import query
from functions.download import download

url = "https://cdn.dinero.today/api/banxico_fix.json" # We need the url from 
os.system("cls") if os.name == "nt" else os.system("clear") # clear the console
download()
today = str(date.today()) # We obtain the date today

response = requests.get(url, "USD") # We obtain on the url the parameter on dollar USD

if response.status_code == 200:
    data = response.json()
    mxn = str(data['rates']['MXN']) # Obtain the data on Dollaar on 
    query(f"UPDATE dbo.DateDimension SET TipoCambio = '{mxn}' WHERE Date = '{today}';")
    query(f"SELECT Date, TipoCambio FROM dbo.DateDimension WHERE date = '{today}'")
else:
    print(f"Error: {response.status_code}")