const Tx = require('ethereumjs-tx').Transaction
const Web3 = require('web3')
const web3 = new Web3('https://mainnet.infura.io/v3/3b1967c19b6445abab489f56666744b6')

web3.eth.getBlockNumber().then(console.log)

//latest blocks
web3.eth.getBlock('latest').then((block) => {
    console.log({
        blockHash: block.hash,
        blockNumber: block.number
    })
})

//Latest 10 blocks
web3.eth.getBlockNumber().then((latest) => {
    for (let i = 0; i < 10; i++) {
        web3.eth.getBlock(latest - i).then((block) => {
            console.log({
                blockHash: block.hash, 
                blockNumber: block.number
            })
        }
        )
    }
})

web3.eth.getGasPrice().then((result)=>{
    console.log(web3.utils.fromWei(result, 'ether'))
})

console.log(web3.utils.sha3('Damindu Sandaruwan'))