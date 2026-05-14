from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


Q2a_txout_scriptPubKey = [
    OP_2DUP,
    OP_ADD,
    1234,
    OP_EQUALVERIFY,
    OP_SUB,
    5678,
    OP_EQUALVERIFY
]

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0013
    txid_to_spend = (
    '1a8f8889d282e55cca156ebdc47b4508c3145b33e0df33dea9503ca5524d4887')
    utxo_index = 0
######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
