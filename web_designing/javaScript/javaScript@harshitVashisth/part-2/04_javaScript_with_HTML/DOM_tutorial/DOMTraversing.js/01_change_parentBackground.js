const h1 = document.querySelector("h1");
// console.log(h1);

/* change parent background */
const parent = h1.parentNode;
parent.style.background = "green";

/* change parentParent background */
const parentParent = h1.parentNode.parentNode;
parentParent.style.background = "gray";