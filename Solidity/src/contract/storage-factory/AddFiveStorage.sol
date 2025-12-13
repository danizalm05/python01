 // SPDX-License-Identifier: MIT
//https://github.com/Cyfrin/remix-storage-factory-cu/blob/main/AddFiveStorage.sol
//https://youtu.be/umepbfKp5rI?t=14484


pragma solidity ^0.8.19;

import {SimpleStorage} from "./SimpleStorage.sol";

contract AddFiveStorage is SimpleStorage {  // The 'is' key word is used for inheritance 
    function store(uint256 _favoriteNumber) public override { // we are overriding the original store function
      
	  myFavoriteNumber = _favoriteNumber + 5;
    }
}