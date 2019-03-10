import requests
import json

api_token = 'ZTM4RQVJU9BKA248X4BQRVMKSTVUCFFD2I'


# Get Contract Source Code for Verified Contract Source Codes
def get_source_code(address):
    url_get_source_code = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + address + '&apikey=' + api_token
    r_source_code = requests.get(url_get_source_code)
    r_source_code_j = json.loads(r_source_code.content)
    return r_source_code_j


# Get Contract ABI for Verified Contract Source Codes
def get_ABI(address):
    url_get_ABI = 'https://api.etherscan.io/api?module=contract&action=getabi&address=' + address + '&apikey=' + api_token
    r_ABI = requests.get(url_get_ABI)
    r_ABI_j = json.loads(r_ABI.content)
    return r_ABI_j


# Get Ether Balance for a single Address
# def get_balance(address):
#    url_get_balance = 'https://api.etherscan.io/api?module=account&action=balance&address=' + address + '&tag=latest&apikey=' + api_token
#    r_balance = requests.get(url_get_balance)
#    return r_balance

