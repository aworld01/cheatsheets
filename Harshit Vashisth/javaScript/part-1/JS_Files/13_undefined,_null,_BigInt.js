/* undefined */
// let name;
// console.log(typeof(name));


/* null */
// let n = null;
// console.log(n);
// console.log(typeof(n)); // This is a bug.


/*
BigInt
There is a limit to store integer number in javaScript.
You can not mix BigInt with another datatype
*/

/* to check maximum safe storage */
// console.log(Number.MAX_SAFE_INTEGER);

/* to check minimum safe storage. */
// console.log(Number.MIN_SAFE_INTEGER); 

let num1 = BigInt(12); //to assign BigInt number.
let num2 = 123n; //to assign BigInt number.
console.log(num1);
console.log(typeof(num1));

console.log(num2);
console.log(typeof (num2));

let total=num1+num2;
console.log(total);