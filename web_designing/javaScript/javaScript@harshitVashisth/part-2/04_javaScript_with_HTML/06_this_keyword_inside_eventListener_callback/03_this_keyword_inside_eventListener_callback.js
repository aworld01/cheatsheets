const btn = document.querySelector(".btn");

/* example1 with normalFunction (this will return btn itself) */
// function show(){
//     console.log("you clicked me....");
//     console.log("Value of this:", this);
// };
// btn.addEventListener("click", show);



/* example2 with auroFunction (this will return window) */
function show(){
}
btn.addEventListener("click", ()=>{
    console.log("you clicked me....");
    console.log("Value of this:", this);
});