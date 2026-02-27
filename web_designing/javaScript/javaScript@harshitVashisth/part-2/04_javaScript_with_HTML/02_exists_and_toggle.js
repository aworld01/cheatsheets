const para = document.querySelector(".para");
console.log(para);

/* example1 */
// console.log(para.classList.contains("big")); //to check if "para" class have "big" class or not.

/* example2 */
const toggle = para.classList.toggle("bg-dark"); //to check if class exists then remove or add
const toggle2 = para.classList.toggle("bg-dark");