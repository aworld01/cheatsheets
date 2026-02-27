/* it will work with only one button */
// const btn1 = document.querySelector(".wrapper button");

// btn1.addEventListener("click", ()=>{
//     console.log(btn1.textContent);
// });



/* it will work with multiple buttons */
// const btns = document.querySelectorAll(".wrapper button");
// function show(){
//     console.log(this.textContent);
// };

// for(let button of btns){
//     button.addEventListener("click", show)
// };



/* example2 */
const btns = document.querySelectorAll(".wrapper button");

for(let button of btns){
    button.addEventListener("click", (e) =>{
        console.log(e.currentTarget.textContent);
    })
}