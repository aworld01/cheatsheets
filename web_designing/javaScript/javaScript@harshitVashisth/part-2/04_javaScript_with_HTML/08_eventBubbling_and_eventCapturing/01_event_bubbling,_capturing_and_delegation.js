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
// child.addEventListener("click", ()=>{
//     console.log("You clicked on Child");
// });

// parent.addEventListener("click", () => {
//     console.log("You clicked on parent")
// });

// grandParent.addEventListener("click", ()=>{
//     console.log("You clicked on grandParent");
// });


/* event capturing */
// child.addEventListener("click", ()=>{
//     console.log("Capture !!!! document.child");
// }, true);

// parent.addEventListener("click", () => {
//     console.log("Capture !!!! document.parent")
// }, true);

// grandParent.addEventListener("click", ()=>{
//     console.log("Capture !!!! document.grandParent");
// }, true);


/* event delegation */
/* example1 */
// grandParent.addEventListener("click", ()=>{
//     console.log("You clicked on something");
// });


/* example2 */
grandParent.addEventListener("click", (e)=>{
    console.log(e.target);
});

/* 7:49:00 / 8:13:32 */