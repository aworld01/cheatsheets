// function myFunc(a,b,...c){
//     console.log("A is:", a);
//     console.log("B is:", b);
//     console.log("C is:", c);
// }
// myFunc(2,3,5,6,7,8,9,10);

function addAll(...numbers){
    let total = 0;
    for(let number of numbers){
        total += number;
    }
    return total
}
let result = addAll(3,4,5,8);
console.log(result);