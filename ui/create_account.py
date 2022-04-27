from web3 import Web3


def new():
    w3 = Web3()
    account = w3.eth.account.create()

    pub = account.address
    prv = account.privateKey.hex()
    return {
        "public": pub,
        "private": prv
    }
