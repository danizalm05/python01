# https://github.com/PatrickAlphaC/web3_py_simple_storage/blob/main/deploy.py
# you must run  pip install py-solc-x
# In the video, we forget to `install_solc`
# change 'from solcx import compile_standard' to 
from solcx import compile_standard, install_solc 



with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    #print(simple_storage_file)
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
    solc_version="0.6.0",
)    