from web3 import Web3


def new(searchString):
    w3 = Web3()
    searchTo = len(searchString)
    looking = True

    while looking:
        account = w3.eth.account.create()
        pattern = account.address[2:2+searchTo]
        print({
            pattern: pattern,
            searchString: searchString
        })
        if pattern == searchString:
            return {
                "public": account.address,
                "private": account.privateKey.hex()
            }
