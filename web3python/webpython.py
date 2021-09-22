>>> from web3 import Web3

>>> infura_url = "https://mainnet.infura.io/v3/3b1967c19b6445abab489f56666744b6"
>>> web3 = Web3(Web3.HTTPProvider(infura_url))
>>> web3.isConnected()
True
>>> web3.eth.blockNumber
13277251
>>> web3.eth.blockNumber
13277251
>>> web3.eth.getBalance("0xa58284cc1DB7dfC4DD1035f279bc1f2C60D86372")
0
>>> infura_url = "HTTP://127.0.0.1:7545"
>>> web3 = Web3(Web3.HTTPProvider(infura_url))
>>> web3.eth.getBalance("0xa58284cc1DB7dfC4DD1035f279bc1f2C60D86372")
100000000000000000000
>>> 
>>> balance =web3.eth.getBalance("0xa58284cc1DB7dfC4DD1035f279bc1f2C60D86372")
>>> web3.fromWei(balance,'ether')
Decimal('100')