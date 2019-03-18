import os, requests, json
import test_dict

def get_source(address):
    api_token = 'ZTM4RQVJU9BKA248X4BQRVMKSTVUCFFD2I'
    url_get_source_code = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + address + '&apikey=' + api_token
    r_source_code = requests.get(url_get_source_code)
    r_source_code_j = json.loads(r_source_code.content)
    return r_source_code_j

# {
#   'status':
#   'message':
#   'result':{
#               [SourceCode
#               ABI
#               ContractName
#               CompilerVersion
#               OptimizationUsed
#               Runs
#               ConstructorArguments
#               Library
#               SwarmSource]
#               }
# }

# CryptoKitties: 0x06012c8cf97BEaD5deAe237070F9587f8E7A266d

# api_token = input('Ehterscan Api Token: ')
contract_address = input('Smart Contract Address: ')
webapp_url = input('Dapp Website Url: ')


# address_list = contract_address.split()
# for address in address_list:

source = get_source(contract_address)
source_code = source['result'][0]['SourceCode']
with open('solc_code/'+source['result'][0]['ContractName']+'.sol', 'w') as f:
    f.write(source_code)

print(source['result'][0]['ContractName']+' compiler version is '+source['result'][0]['CompilerVersion'])