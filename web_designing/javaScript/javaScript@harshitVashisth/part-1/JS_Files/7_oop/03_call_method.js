/* example1*/
// function hello(){
//     console.log("Hello world");
// };

// // hello(); //regular use
// hello.call(); //call method



/* example2*/
// const user1 = {
//     name: "Harshit",
//     age: 18,
//     about: function(){
//         console.log(`Name is ${this.name} and age is ${this.age}.`)
//     }
// };

// const user2 = {
//     name: "Mohit",
//     age: 18
// }

// user1.about.call();
// user1.about.call(user1);
// user1.about.call(user2);



/* call method with parameters (example1)*/
// const user1 = {
//     name: "Harshit",
//     age: 18,
//     about: function(hobby, job){
//         console.log(`My name is ${this.name} and age is ${this.age}.`);
//         console.log(`My hobby is ${hobby}, and I'm an ${job}`);
//     }
// };

// const user2 = {
//     name: "Mohit",
//     age: 18
// }

// user1.about.call(user2, "Listening to music", "Electrician");



/* call method with parameters (example2)*/
// function about(hobby, job){
//     console.log(`My name is ${this.name} and age is ${this.age}.`);
//     console.log(`My hobby is ${hobby}, and I'm an ${job}`);
// };

// const user1 = {
//     name: "Harshit",
//     age: 18
// }

// about.call(user1, "Listening to music", "Electrician");