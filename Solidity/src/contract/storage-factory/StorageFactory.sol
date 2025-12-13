/ SPDX-License-Identifier: MIT
//https://github.com/Cyfrin/remix-storage-factory-cu/blob/main/StorageFactory.sol
// 
// https://youtu.be/umepbfKp5rI?t=14461

pragma solidity ^0.8.19;

//  push buttons order 
//   1. crearwSimpleStorage  
//   2.ListSimpleStorage  (index)
//   3. sfStoe  input    (index, number )
//   4. stGet  (index) and you sould see the number.

//import {SimpleStorage, SimpleStorage2} from "./SimpleStorage.sol";//Import only this  two contract
import {SimpleStorage} from "./SimpleStorage.sol";
  
contract StorageFactory {
 
  
  SimpleStorage[] public listOfSimpleStorageContracts;

  function createSimpleStorageContract() public {
        SimpleStorage simpleStorageContractVariable = new SimpleStorage();
        // SimpleStorage simpleStorage = new SimpleStorage();
        listOfSimpleStorageContracts.push(simpleStorageContractVariable);
    }

 function sfStore(uint256 _index,  uint256 _simpleStorageNumber)  public  { 

        listOfSimpleStorageContracts[_index].store(  _simpleStorageNumber  );
  }
 
  function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        
        return listOfSimpleStorageContracts[_simpleStorageIndex].retrieve();
    }


}