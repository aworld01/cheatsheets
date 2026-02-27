let name = document.querySelector(".name");
let age = document.querySelector(".age");
let bt = document.querySelector(".btn");

bt.addEventListener('click', inputMsg);

function inputMsg(){
    let n = prompt("Enter your name please");
    let a = prompt("Enter your age:")
    name.textContent = n;
    age.innerText = a;
}