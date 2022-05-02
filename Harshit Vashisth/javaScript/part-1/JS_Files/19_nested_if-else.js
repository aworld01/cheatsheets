/*
let winningNumber = 19;
[19] your guess is right
[17] too low
[20] too high
*/

let winningNumber = 19;
// let usrInput = prompt("Guess a number"); //it takes input in string
// console.log(typeof usrInput, usrInput);

// let usrInput = +prompt("Guess a number"); //put "+" to conver into number
// console.log(typeof usrInput, usrInput);

// let usrInput = +prompt("Guess a number");
// if(usrInput === winningNumber){
//     console.log("Your number is right....")
// }else{
//     console.log("Your guess is wrong...")
// }

let usrInput = +prompt("Guess a number");
if(usrInput === winningNumber){
    console.log("Your number is right....")
}else{
    if(usrInput < winningNumber){
        console.log("Too low...")
    }else{
        console.log("Too high...")
    }
}