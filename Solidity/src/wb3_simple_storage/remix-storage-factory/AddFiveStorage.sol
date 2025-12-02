// SPDX-License-Identifier: MIT
//https://github.com/Cyfrin/remix-storage-factory-cu/blob/main/AddFiveStorage.sol
pragma solidity 0.8.19;

import {SimpleStorage} from "./SimpleStorage.sol";

contract AddFiveStorage is SimpleStorage {
    function store(uint256 _favoriteNumber) public override {
        myFavoriteNumber = _favoriteNumber + 5;
    }
}