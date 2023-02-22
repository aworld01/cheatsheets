const numbers = [1,2,3,4,5,10];

/* aim: sum of all the numbers in array */
// function s(accumulator, currentValue){
//     return accumulator + currentValue;
// }

// const sum = numbers.reduce(s);
// console.log(sum);

/*
accumulator,            currentValue,           return
1                       2                       3
3                       3                       6
6                       4                       10
10                      5                       15
15                      10                      25
*/







function n(totalPrice, currentProduct){
    return totalPrice + currentProduct.price;
}

const userCart = [
    {productId: 1, productName: "Mobile", price: 12000},
    {productId: 2, productName: "Laptop", price: 22000},
    {productId: 3, productName: "TV", price: 15000}
];

const totalAmount = userCart.reduce(n, 0); //0 is initialValue, you can put if you need or not.
console.log(totalAmount);

/*
totalPrice,            currentValue,           return
0                      {}                      12000
12000                  22000                   34000
34000                  15000                   49000
*/