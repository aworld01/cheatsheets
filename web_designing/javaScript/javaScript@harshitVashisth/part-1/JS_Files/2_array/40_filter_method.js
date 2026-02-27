const numbers = [1,3,2,6,4,8];

/* get evenNumbers */
// const isEven = function(number){
//     return number % 2 === 0;
// }

// const evenNumbers = numbers.filter(isEven);
// console.log(evenNumbers);



/* get oddNumbers */
// const isOdd = function(number){
//     return number % 2 !== 0;
// }

// const oddNumbers = numbers.filter(isOdd);
// console.log(oddNumbers);



/* example2 */
const isOdd = function(number){
    return number % 2 !== 0;
}

const oddNumbers = numbers.filter((number)=>{
    return number % 2 === 0;
});
console.log(oddNumbers);