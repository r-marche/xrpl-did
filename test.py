## TESTING XRPL-PY
## This file is meant to familiarize with the usage of the library xrpl-py,
## following the guide at https://xrpl.org/docs/tutorials/python/get-started

###############################################################################
##DEFINE THE NETWORK CLIENT

from xrpl.clients import JsonRpcClient

## Connecting to the Testnet
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

###############################################################################
##CREATE AN ACCOUNT ON THE TESTNET

from xrpl.wallet import generate_faucet_wallet
from xrpl.account import get_account_root

##Creating a wallet using faucet: https://xrpl.org/xrp-testnet-faucet.html
test_wallet = generate_faucet_wallet(client, debug=True)

##Retrieve account
address = test_wallet.address
account = get_account_root(address, client)

###############################################################################
##PREPARE PAYMENT

from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops

tx_payment = Payment(
    account=account,
    amount=xrp_to_drops(22),
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
)

###############################################################################
##SIGN AND SUBMIT

from xrpl.transaction import submit_and_wait

#tx_response = submit_and_wait(tx_payment, client, test_wallet)
## Not working

###############################################################################
##DERIVE AN X-ADDRESS

from xrpl.core import addresscodec

#test_xaddress = addresscodec.classic_address_to_xaddress(
#		account,
#		tag=12345,
#		is_test_network=True
#	)
#print("\nClassic address:\n\n", account)
#print("X-address:\n\n", test_xaddress)
## Not working

###############################################################################
## LOOK UP INFO ABOUT ACCOUNT

import json
from xrpl.models.requests.account_info import AccountInfo

acct_info = AccountInfo(
    account=account,
    ledger_index="validated",
    strict=True,
)

response = client.request(acct_info)
result = response.result

print("response.status: ", response.status)
print(json.dumps(response.result, indent=4, sort_keys=True))