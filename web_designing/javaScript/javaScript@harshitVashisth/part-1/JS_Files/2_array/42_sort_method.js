// const numbers = [5,9,1200,400,3000];
// numbers.sort(); //it's mutate the original value (sort by aicky character)
// console.log(numbers);


// const userNames = ["Harshit", "ABC", "Mohit", "Nitish"]; //sort in caseSensetive
// userNames.sort();
// console.log(userNames);




/* finalTrick (sort in asendingOrder) */
// const numbers = [5,9,1200,400,3000];
// function sor(a,b){
//     return a-b;
// }
// numbers.sort(sor); //it's mutate the original value (sort by aicky character)
// console.log(numbers);


/* finalTrick (sort in desendingOrder) */
// const numbers = [5,9,1200,400,3000];
// function sor(a,b){
//     return b-a;
// }
// numbers.sort(sor); //it's mutate the original value (sort by aicky character)
// console.log(numbers);




/* sort with arrowFunction */
// const numbers = [5,9,1200,400,3000];
// numbers.sort((a,b)=>a-b); //it's mutate the original value (sort by aicky character)
// console.log(numbers);




/* exercise1 */
const products = [
    {productId: 1, productName: "p1", price: 300},
    {productId: 2, productName: "p2", price: 3000},
    {productId: 3, productName: "p3", price: 200},
    {productId: 4, productName: "p4", price: 8000},
    {productId: 5, productName: "p5", price: 500}
];
/* lowToHigh */
products.sort((a,b)=>{
    return a.price-b.price
});
console.log(products);
console.log();


/* highToLow */
products.sort((a,b)=>{
    return b.price-a.price
});
console.log(products);