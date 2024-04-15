## Importing everything. MUST BE MODIFIED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions import DIDSet
from xrpl.transaction import *


## REMARK. For Mainnet implementation, DID amendament is required:
## https://xrpl.org/resources/known-amendments/#did

def createDID(address):
	'''
	Submits a DIDSet transation creating the DID associated to a given address.
	'''
	
	# Creating transation
	did_set = Transaction.from_dict(
			{
				"Account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh",
				"Fee": "10",
				"Sequence": 391,
				"URI": "697066733A2F2F62616679626569676479727A74357366703775646D37687537367568377932366E6634646675796C71616266336F636C67747179353566627A6469",
				"Data": "",
				"SigningPubKey":"0330E7FC9D56BB25D6893BA3F317AE5BCF33B3291BD63DB32654A313222F7FD020"
			}
		)

	#did_set = Transaction(

		#) 

	#setDID = DIDSet(
			#account=address,
			#data='',
			#did_document='',
			#uri='',
		#)

def updateDID(address):
	'''
	Submits a DIDSet transation updating the DID associated to a given address.
	'''

	pass



###############################################################################
#################################### TEST #####################################
###############################################################################

from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.account import get_account_root

## Connecting to the Testnet
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

##Creating a wallet using faucet: https://xrpl.org/xrp-testnet-faucet.html
test_wallet = generate_faucet_wallet(client, debug=True)

##Retrieve account
address = test_wallet.address
#account = get_account_root(address, client)

createDID(address)