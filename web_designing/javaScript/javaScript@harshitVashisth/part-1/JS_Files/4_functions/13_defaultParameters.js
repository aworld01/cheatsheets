/* before we used */
// function addTwo(a,b){
//     if(typeof b === "undefined"){
//     b = 0;
//     }
//     return a+b;
// }
// let ans = addTwo(4);
// console.log(ans);

// let ans = addTwo(4,5);
// console.log(ans);



/* now we use */
function addTwo(a,b=0){
    return a+b;
}
// let ans = addTwo(4);
// console.log(ans);

let ans = addTwo(4,5);
console.log(ans);