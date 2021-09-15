const Web3 = require('web3')
const web3 = new Web3('https://mainnet.infura.io/v3/3b1967c19b6445abab489f56666744b6')
const _ = require('underscore');
// const _ = web3.utils._

//Gasprice
web3.eth.getGasPrice().then((result)=>{
    console.log(web3.utils.fromWei(result,'ether'))   
})

//Hash Value
console.log(web3.utils.sha3('Damindu Sandaruwan'))

console.log(web3.utils.randomHex(32))

//Underscore js

console.log(_)

_.each({key1:'value1', key2:'value2'},(value,key)=>{
    console.log(key)
})


