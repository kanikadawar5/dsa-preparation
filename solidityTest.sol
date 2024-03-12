// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "forge-std/Test.sol";
import "../src/Token.sol";  // Import the contract to be tested 

contract TokenTest is Test {
    Token public token; // Instance of the Token contract

    // Setup function to deploy contract before tests
    function setUp() public {
        token = new Token();
    }

    // Test the initial token balance of the contract deployer 
    function testInitialBalance() public {
        assertEq(token.balanceOf(address(this)), 1000000);
    }

    // Test successful token transfer
    function testTransferSuccess() public {
        uint256 initialBalance = token.balanceOf(address(this));
        vm.prank(address(0xabcd)); // Simulate a different sender
        token.transfer(address(0xabcd), 100);

        assertEq(token.balanceOf(address(this)), initialBalance - 100);
        assertEq(token.balanceOf(address(0xabcd)), 100);
    }

    // Test failed transfer due to insufficient balance (fuzz testing)
    function testFuzzTransferFail(uint256 amount) public {
        vm.assume(amount > token.balanceOf(address(this))); // Add an assumption for fuzzing
        vm.expectRevert(bytes("Not enough tokens")); 
        token.transfer(address(1), amount); 
    } 
}