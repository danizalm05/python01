#!/usr/bin/env python3
# Bitcoin mining with 15 lines of python code
# https://www.youtube.com/watch?v=ZhnJ1bkIWWk
# https://github.com/codebasics/cool_python_apps/blob/main/2_bitcoin_mining/
from hashlib import sha256
MAX_NONCE = 1000000

def SHA256(text):
    return (sha256(text.encode("ascii")).hexdigest())#  print 64 bit hex


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")



if __name__=='__main__':
    transactions = '''
        Dhaval->Bhavin->20,
        Mando->Cara->45
        '''
    previous_hash = '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'
    block_number = 5
    difficulty = 4  # Number of priffix zeros that we want
    import time

    start = time.time()

    print("start mining")

    new_hash = mine(block_number, transactions, previous_hash, difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)