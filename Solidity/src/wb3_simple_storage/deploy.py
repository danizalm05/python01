# https://github.com/PatrickAlphaC/web3_py_simple_storage/blob/main/deploy.py
# https://www.youtube.com/watch?v=M576WGiDBdQ&t=44s   03:30:00
#  

from web3 import Web3
import json


# First you must run: 
#       pip install py-solc-x   
#       pip install web3

from solcx import compile_standard, install_solc


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)
# We add these two lines that we forgot from the video!
print("Installing...")
install_solc("0.8.7")
# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.7",  # "0.6.0",
)
# print(compiled_sol)
# 03:46:30

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]
#print(abi)


#         ============   Deploy the contract ================== 03:53:00
# For connecting to ganache
# The next values  are taken from Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# the chain id for gaunch is 1337 . the network is 5777
chain_id = 1337     
my_address =  "0x9464257eB4a5904A5D9D7d687f12C0fdFf0E237c"
private_key = "0x588b57422ace77ce5255cfa40f0a4df3520d5b6bca1bce0e2a6cdad45d8301bc"

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the latest transaction
nonce = w3.eth.get_transaction_count(my_address)
print ("nonce = ",nonce) # number of transaction

# Submit the transaction that deploys the contract
transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
print ("transaction \n= ",transaction)
#043:01:00 