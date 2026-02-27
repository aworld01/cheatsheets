// const numbers = [3,5,8,9];

// /* kya ek v number even hai */
// const result = numbers.some((number)=>number%2 === 0);
// console.log(result);




/* example2 */
const userCart = [
    {productId: 1, productName: "Mobile", price: 12000},
    {productId: 2, productName: "Laptop", price: 22000},
    {productId: 3, productName: "TV", price: 15000},
    {productId: 4, productName: "Macbook", price: 250000}
];

const result = userCart.some((cartItem)=>cartItem.price > 200000);
console.log(result);