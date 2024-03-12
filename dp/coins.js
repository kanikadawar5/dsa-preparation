// https://www.geeksforgeeks.org/coin-change-dp-7/
// recursion

// Input: sum = 4, coins[] = {1,2,3}, 
// Output: 4
// Explanation: there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}. 

var coinChange = function (sum, coins) {
    console.log(sum, coins)
    if (sum === 0) return 1;
    if (sum < 0) return 0;
    if (coins.length === 0) return 0;
    return coinChange(sum - coins[0], coins) + coinChange(sum, coins.slice(1));
}
console.log(coinChange(4, [1, 2, 3]))
