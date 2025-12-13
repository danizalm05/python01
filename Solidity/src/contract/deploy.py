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
# https://developer.metamask.io/key/active-endpoints  'Linea Sepolia' 

w3 = Web3(Web3.HTTPProvider("https://linea-mainnet.infura.io/v3/5808951b3b634fabbcc238ba2be88de6")) 


# the chain id for gaunch is 1337 . the network is 5777
chain_id = 59144 #59141    # serach for 'Linea Sepolia' in  https://chainlist.org/ or https://chainid.network/
my_address =  "0xBa5Bb12E154d5bAFa48eDbd21F68F69B4bDfd57B"
private_key = "0xe7326b4b21f2bc7980fa956491873ddb595bc505291d2a704873e0c10c4f3ecd"

#The 'my_address' and  'private_key' are changing for every time we are running Ganush


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

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")

# Send it!
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
#changing from rawTransaction to raw_transaction

# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

# Working with deployed Contracts
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
#  'retrieve' is a function in the 'simple_storage.sol' file
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")

#43:14:00 
greeting_transaction = simple_storage.functions.store(15).build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.raw_transaction)
#changing from rawTransaction to raw_transaction
print("Updating stored Value...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

print(simple_storage.functions.retrieve().call())