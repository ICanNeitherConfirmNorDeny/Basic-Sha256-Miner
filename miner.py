import hashlib

NONCE_Limit = 10000000000

# any more zeros than 5 could take a while.
zeros = 5 

def mining(block_number, transactions, previous_hash):
    for nonce in range(NONCE_Limit):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_find = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_find.startswith("0" * zeros):
            print(f"Found hash with nonce: {nonce}")
            return hash_find

    return -1

block_number = 55
transactions = "948503840cs953"
previous_hash = "9459873105ty1"

mining(block_number, transactions, previous_hash)

combo_text = str(block_number) + transactions + previous_hash + str(22406)
print(hashlib.sha256(combo_text.encode()).hexdigest())


