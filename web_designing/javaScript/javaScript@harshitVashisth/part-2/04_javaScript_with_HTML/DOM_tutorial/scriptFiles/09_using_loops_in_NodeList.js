/*
arrayLikeObject == indexing, length property

You can use with HTMLCollection
1: simple forLoop
2: for of loop
3: forEach loop
*/

/* simple forLoop */
// let paragraphs = document.querySelectorAll("p"); //returns NodeList
// console.log(paragraphs);

// for(let i=0; i<paragraphs.length; i++){
//     let navItem = paragraphs[i];
//     navItem.style.backgroundColor = "yellow";
//     navItem.style.textAlign = "center";
// };



/* for of Loop */
// let paragraphs = document.querySelectorAll("p");
// for(let paragraph of paragraphs){
//     paragraph.style.backgroundColor = "yellow";
//     paragraph.style.textAlign = "center";
// };



/* forEach */
let paragraphs = document.querySelectorAll("p");
// console.log(paragraphs);

// navItems = Array.from(paragraphs); //to change into array
// console.log(navItems);

// console.log(Array.isArray(navItems)); //to check array

paragraphs.forEach((navItem)=>{
    navItem.style.backgroundColor = "yellow";
    navItem.style.textAlign = "center";
});