// SPDX-License-Identifier: MIT
//SimpleStorage.sol
//https://github.com/Cyfrin/remix-simple-storage-cu/blob/main/SimpleStorage.sol
//https://www.youtube.com/watch?v=umepbfKp5rI&t=7842s

//https://youtu.be/umepbfKp5rI?t=8758
//https://youtu.be/umepbfKp5rI?t=10268     arrays
pragma solidity 0.8.34;

// pragma solidity ^0.8.0;
// pragma solidity >=0.8.0 <0.9.0;

contract SimpleStorage {

   uint256 myFavoriteNumber;

    struct Person {
        uint256 favoriteNumber;
        string name;
    }

       // uint256[] public anArray;
    Person[] public listOfPeople;

    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        myFavoriteNumber = _favoriteNumber +1 ;
    }

    function retrieve() public view returns (uint256) {
        return myFavoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        listOfPeople.push(Person(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}