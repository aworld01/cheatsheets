// const numbers = [2,4,8,10];

// function isEven(number){
//     return number % 2 === 0;
// }
// /* all the numbers should be true */
// const result = numbers.every(isEven);
// console.log(result);



/* example2 */
const userCart = [
    {productId: 1, productName: "Mobile", price: 12000},
    {productId: 2, productName: "Laptop", price: 22000},
    {productId: 3, productName: "TV", price: 15000}
];

const result = userCart.every((cartItem)=>cartItem.price < 30000);
console.log(result);