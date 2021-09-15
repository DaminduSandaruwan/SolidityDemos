const Web3 = require('web3')
const web3 = new Web3('https://mainnet.infura.io/v3/3b1967c19b6445abab489f56666744b6')

web3.eth.getGasPrice().then((result)=>{
    console.log(web3.utils.fromWei(result,'ether'))   
})