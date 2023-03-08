/*
arrayLikeObject == indexing, length property

You can use with HTMLCollection
1: simple forLoop
2: for of loop
3: forEach loop //can't directly use with HTMLCollection

navItems = Array.from(navItems); //to change into array
*/

/* simple forLoop */
// const navItems = document.getElementsByClassName("nav-item"); //returns HTMLCollection
// for(let i=0; i<navItems.length; i++){
//     let navItem = navItems[i];
//     navItem.style.backgroundColor = "yellow";
//     navItem.style.textAlign = "center";
// }



/* for of Loop */
// const navItems = document.getElementsByClassName("nav-item"); //returns HTMLCollection
// for(let navItem of navItems){
//     navItem.style.backgroundColor = "yellow";
//     navItem.style.textAlign = "center";
// }



/* forEach */
let navItems = document.getElementsByClassName("nav-item"); //returns HTMLCollection
navItems = Array.from(navItems); //to change into array
navItems.forEach((navItem)=>{
    navItem.style.backgroundColor = "gray";
    navItem.style.textAlign = "center";
});





/* 4:29:21 / 8:13:32 */