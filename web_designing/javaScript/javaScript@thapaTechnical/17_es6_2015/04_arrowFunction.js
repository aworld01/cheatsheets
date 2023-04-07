/* normalFunction */
// function sum(){
//     let a = 5; b = 6;
//     let add = a+b;
//     return `The sum of the two numbers is ${add}.`;
// }
// let plus = sum(4,5);
// console.log(plus);



/* arrowFunction */
// const sum = ()=>{
//     let a = 5; b = 6;
//     return `The sum of the two numbers is ${a*b}.`;
// }
    
// console.log(sum());



/* arrowFunction with parameters */
// const sum = (x, y)=>{
//     let a = x; b = y;
//     return `The sum of the two numbers is ${a*b}.`;
// }
    
// console.log(sum(9,3));



/* arrowFunction_in_oneline */
// const sum = () => `The sum of the two numbers is ${(x=5)+(y=7)}.`;
const sum = (x=5, y=6) => `The sum of the two numbers is ${x+y}.`;

console.log(sum())
// console.log(sum(9,3));