from web3 import Web3

w3 = Web3()
account = w3.eth.account.create()
print("address: ", account.address)
print("private: ", account.privateKey.hex())
