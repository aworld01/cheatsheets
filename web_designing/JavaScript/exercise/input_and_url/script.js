let name = document.querySelector(".name");
let age = document.querySelector(".age")

let bt = document.querySelector(".btn");

bt.addEventListener('click', inputMsg);

function inputMsg(){
    let search = document.getElementById("search").value;

    let url = "https://www.google.com/search?client=firefox-b-e&q=";

    data = url+search;
}