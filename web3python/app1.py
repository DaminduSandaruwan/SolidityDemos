from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

account_1="0xe11d37d48b637B078f2B1e4A27A1BEeB1544Ad1c"
account_2="0x3B7304E52Aa468D2a71cDDbf3eC8213480Ed162f"
private_key="012d18838f8cbb466604fc0d782c87288b44dc211411a7442ab560b621205e90"

#get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build Transaction
tx= {
    'nonce': nonce,
    'to': account_2,
    'value' : web3.toWei(1,'ether'),
    'gas' : 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign Transaction
signed_tx = web3.eth.account.signTransaction(tx,private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get transaction hash
print(tx_hash)
print(web3.toHex(tx_hash))