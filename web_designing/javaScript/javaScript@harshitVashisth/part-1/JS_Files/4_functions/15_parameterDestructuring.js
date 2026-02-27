/* example1 */
// const person = {
//     firstName: "harshit",
//     gender: "male"
// }

// function printDetails(obj){
//     console.log(obj.firstName);
//     console.log(obj.gender);
// }

// printDetails(person);



const person = {
    firstName: "harshit",
    gender: "male"
}

function printDetails({firstName, gender}){
    console.log(firstName);
    console.log(gender);
}

printDetails(person);