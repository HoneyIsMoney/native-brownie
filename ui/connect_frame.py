from web3 import Web3
from decouple import config

url = config('FRAME_RPC')
print(url)

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(url))
res = w3.isConnected()
print(res)
w3.provider
