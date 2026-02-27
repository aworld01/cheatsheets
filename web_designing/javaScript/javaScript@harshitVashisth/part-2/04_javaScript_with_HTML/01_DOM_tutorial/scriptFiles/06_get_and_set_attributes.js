/* example1 */
// const link = document.querySelector("a");
// console.log(link);

// const at = link.getAttribute("href"); //to select attribute
// console.log(at);



/* example2 */
// const link = document.querySelector("input");
// console.log(link);

// const txt = link.getAttribute("name");
// console.log(txt);




const link = document.querySelector("a");
console.log(link);

g = link.getAttribute("href");
console.log(g);

link.setAttribute("href", "https://www.amazon.in");
console.log(link);