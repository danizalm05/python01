//SPDX-License-Identifier: MIT
//https://github.com/Cyfrin/remix-fund-me-cu/blob/main/FundMe.sol
//https://youtu.be/umepbfKp5rI?t=15149
//https://coinsbench.com/walkthrough-using-chainlink-data-feeds-for-computation-in-cryptozombies-71ac9bb7abba 
//https://youtu.be/umepbfKp5rI?t=21093
//Start MetaMask bofore llstarting Remix
// In remix you sould chose enviroment :'Injected provider - Metamask'


// Get funds from 
// Withdraw funds
// Set a minimum  funding value in USD

pragma solidity ^0.8.18;
//import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";
import {PriceConverter} from "./PriceConverter.sol";
error NotOwner();
contract FundMe {
    using PriceConverter for uint256;
    mapping(address => uint256 amountFounded) public addressToAmountFunded;
   

    uint256 public constant MINIMUM_USD = 5 * 10e18; //5$   
    address[] public funders;
    // Could we make this constant?    no! We should make it immutable! */
    // Becase we set it not in the same line of declration.
    address public immutable i_owner;
  
   constructor() {
        i_owner = msg.sender;
    }


 //In order for a function to recive native blockchin token it must  be marked  as payable
 function fund() public  payable {  
    
    require(msg.value.getConversionRate() >= MINIMUM_USD, "You need to spend more ETH!");
    //  require(msg.value > 1e16, "You need to spend more ETH!"); 
     //require(getConversionRate(msg.value ) >= MINIMUM_USD, "You need to spend more ETH!");
     addressToAmountFunded[msg.sender] += msg.value;
     funders.push(msg.sender);  
  } 


  function withdraw() public onlyOwner {
  
     //require(msg.sender == i_owner,"Must be owner!");
     for (uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
     }
     //Reset the array length of 0
     funders = new address[](0);
    //                      Withdraw funds
    //                  =======================
    //                there are 3 ways: transfer, send, call
   //  1. transfer
     // msg.sender is of type:    address  
     // payable(msg.sender) is of type:     payable address
    // payable(msg.sender).transfer(address(this).balance);

   // 2. send
   // bool sendSuccess = payable(msg.sender).send(address(this).balance);
   // require(sendSuccess, "Send failed"); // if sendSuccess is false?
   
    // 3. call
    (bool callSuccess,  ) = payable(msg.sender).call{value: address(this).balance}("");
    require(callSuccess, "Call failed");

  } 
 
    // Explainer from: https://solidity-by-example.org/fallback/
    // Ether is sent to contract
    //      is msg.data empty?
    //          /   \
    //         yes  no
    //         /     \
    //    receive()?  fallback()
    //     /   \
    //   yes   no
    //  /        \
    //receive()  fallback()


 modifier onlyOwner() {
     
      //  require(msg.sender == i_owner,"Must be owner!");
    if (msg.sender != i_owner) revert NotOwner();
    // error without message saves gas
        _; //Execute the code inside the function that this modifer is used 
    }

     // Explainer from: https://solidity-by-example.org/fallback/
    // Ether is sent to contract
    //      is msg.data empty?
    //          /   \
    //         yes  no
    //         /     \
    //    receive()?  fallback()
    //     /   \
    //   yes   no
    //  /        \
    //receive()  fallback()

    fallback() external payable {
        fund();
    }

    receive() external payable {
        fund();
    }
}

// Concepts we didn't cover yet (will cover in later sections)
// 1. Enum
// 2. Events
// 3. Try / Catch
// 4. Function Selector
// 5. abi.encode / decode
// 6. Hash with keccak256
// 7. Yul / Assembly






}