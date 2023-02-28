/* example1 */
// const person = {
//     name: "Mohit",
//     age: 8,
//     about: function(){

//     }
// };
// console.log(person);



/* exmple2 */
// const person = {
//     name: "Mohit",
//     age: 8,
//     about: function(){
//         console.log(person);
//     }
// };
// person.about();



/* example3 */
// const person = {
//     name: "Mohit",
//     age: 8,
//     about: function(){
//         console.log(this);
//     }
// };
// person.about()



/* example4 */
// const person = {
//     name: "Mohit",
//     age: 8,
//     about: function(){
//         console.log(`Person name is ${person.name}, and person age is ${person.age}.`);
//     }
// };
// person.about();



// /* example5 */
const person = {
    name: "Mohit",
    age: 8,
    about: function(){
        console.log(`Person name is ${this.name}, and person age is ${this.age}.`);
    }
};
person.about();