import re
import requests

def verifica_cnpj(cnpj):
    if re.search(r'^[0-9]{14}$|^[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$' , cnpj):
        print("formatacao do cnjp correta")
        return cnpj
    else:
        print("formatacao do cnjp incorreta")
        

def conect_api(cnpj):
    r =  requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")

    print(r.status_code)

    response_dict = r.json()
    print(len(response_dict.values()))
    print(f"cep: {response_dict['cep']}")    
    return response_dict['cep']
