# https://github.com/PatrickAlphaC/web3_py_simple_storage/blob/main/deploy.py
# https://www.youtube.com/watch?v=M576WGiDBdQ&t=44s   03:30:00


# you must run  pip install py-solc-x
# In the video, we forget to `install_solc`
# change 'from solcx import compile_standard' to
from solcx import compile_standard, install_solc
import json


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
print(abi)
#         ============   Deploy the contract ================== 03:50:00