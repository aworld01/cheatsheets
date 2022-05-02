function inputMsg(){
    let name = document.querySelector(".name");
    let age = document.querySelector(".age");
    let n = document.getElementById("name").value;
    let a = document.getElementById("age").value;
    name.textContent = n;
    age.innerText = a;
}