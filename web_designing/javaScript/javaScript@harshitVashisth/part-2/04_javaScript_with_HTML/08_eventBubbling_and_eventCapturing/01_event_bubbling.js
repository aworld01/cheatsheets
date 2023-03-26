/*
event bubbling / event propogation
event capturing
event delegation

HTML
.grandparent>.parent>.child
box
*/

const grandParent = document.querySelector(".grandParent");
const parent = document.querySelector(".parent");
const child = document.querySelector(".child");


/* event bubbling / event propogation */
child.addEventListener("click", ()=>{
    console.log("You click on Child");
});

parent.addEventListener("click", () => {
    console.log("You click on parent")
});

grandParent.addEventListener("click", ()=>{
    console.log("You click on grandParent");
});

/* 7:34:00 / 8:13:32 */