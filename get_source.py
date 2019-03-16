import requests
import json

api_token = 'ZTM4RQVJU9BKA248X4BQRVMKSTVUCFFD2I'


def get_source_code(address):
    url_get_source_code = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + address + '&apikey=' + api_token
    r_source_code = requests.get(url_get_source_code)
    r_source_code_j = json.loads(r_source_code.content)
    return r_source_code_j

# {
#   'status':
#   'message':
#   'result':{
#               SourceCode
#               ABI
#               ContractName
#               CompilerVersion
#               OptimizationUsed
#               Runs
#               ConstructorArguments
#               Library
#               SwarmSource
#               }
# }
