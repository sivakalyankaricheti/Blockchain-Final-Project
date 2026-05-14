from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cUr3VapxCedgrVtvSntC63vM7taLm5SnrMhR46jpyGtD1cC34fAp')
cust1_public_key = cust1_private_key.pub

cust2_private_key = CBitcoinSecret(
    'cT5mL8o7YfYJmR9Xx8qW6aB2cD3eF4gH5iJ6kL7mN8pQ9rS1tU2')
cust2_public_key = cust2_private_key.pub

cust3_private_key = CBitcoinSecret(
    'cV9xY7zA6bC5dE4fG3hJ2kL1mN0pQ8rS7tU6vW5xY4zA3bC2dE')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    OP_ADD,
    1234,
    OP_EQUAL
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0013

    txid_to_spend = (
        '1a8f8889d282e55cca156ebdc47b4508c3145b33e0df33dea9503ca5524d4887')

    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
