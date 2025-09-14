import os
import requests
from dotenv import load_dotenv
import os
import re


def verifica_cnpj (cnpj):
    cnpj = str(cnpj)
    if re.search(r'^[0-9]{14}$|^[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$',cnpj):
        print("formatacao correta")
    else:
        print("formatacao incorreta ")

def conect_api(cnpj):
    verifica_cnpj(cnpj)
    r = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
    if r.status_code == 200:
      # for values  in r.json():
      #     print(f"{values}")
      response_dict = r.json()
      print(len(response_dict.values()))
      print(f"cep: {response_dict['cep']}")

def main():
    
    load_dotenv()  # take variables from .env.
    db_url = os.getenv("TELEGRAM_KEY")
    print(db_url)
    conect_api(19131243000197)


main()
