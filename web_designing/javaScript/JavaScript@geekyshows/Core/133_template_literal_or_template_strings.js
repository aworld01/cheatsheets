/*
Template literals are string literals allowing embedded expressions. You can use multiLine strings and stringInterpolation features with them.
Template literals are enclosed by the back-tick (` `) character instead of double or single quotes.
*/

/*multipleLineString*/
// s = `Hello
// world
// How are
// You?`;

// console.log(s);



/*
stringInterpolation
Template literals can contain placeholders. These are indicated by the dollar-sign and curly-braces (${expression})
*/
// s = "You are Welcome";
// console.log(`${s} in my world!`);



// add = `${2+2}`;
// console.log(add);



// function myfun(say){
//     return "Hello "+say;
// }

// console.log(`${myfun("world")} how are you?`)



function sayName(arg){
    return `Your name is: ${arg}.`
}

console.log(sayName("Abdul Fahad"))