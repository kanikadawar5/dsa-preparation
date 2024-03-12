// // recursion

// var fibo = function (n) {
//   if (n <= 1) {
//     return n;
//   } else {
//     return fibo(n - 1) + fibo(n - 2);
//   }
// };

// console.log(fibo(10)); // 55
// console.log(fibo(20)); // 6765

// DP
var fibo = function (n) {
    let f = []
    f[0] = 0
    f[1] = 1
    for (let i = 2; i <= n; i++) {
        f[i] = f[i - 1] + f[i - 2]
    }
    return f[n]
}

console.log(fibo(10)); // 55
