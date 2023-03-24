/* it will work with only one button */
// const btn1 = document.querySelector(".btn");

// btn1.addEventListener("click", ()=>{
//     console.log(btn1.textContent);
// });



/* it will work with multiple buttons */
const btns = document.querySelectorAll(".btn");
function show(){
    console.log(this.textContent);
};

for(let button of btns){
    button.addEventListener("click", show)
};


/* 6:31:00 / 8:13:32 */