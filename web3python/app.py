from web3 import Web3

infura_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)
balance =web3.eth.getBalance("0xa58284cc1DB7dfC4DD1035f279bc1f2C60D86372")
print(web3.fromWei(balance,'ether'))