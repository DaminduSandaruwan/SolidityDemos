pragma solidity 0.5.1;

contract Timelock {
    
    address payable public benificiary;
    uint256 public releaseTime;
    
    constructor(
        address payable _benificiary, 
        uint256 _releaseTime
        
    ) public payable {
        require(_releaseTime > block.timestamp);
        benificiary = _benificiary;
        releaseTime = _releaseTime;
    }
    
    function release() public {
        require(block.timestamp >= releaseTime);
        address(benificiary).transfer(address(this).balance);
    }
}