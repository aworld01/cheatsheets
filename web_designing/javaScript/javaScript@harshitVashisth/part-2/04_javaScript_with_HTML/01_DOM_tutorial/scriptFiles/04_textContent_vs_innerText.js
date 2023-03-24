let p = document.getElementById("hide");

let txt1 = p.textContent; //it returns hidden text also
console.log(txt1);

let txt2 = p.innerText; //it never returns hidden text
console.log(txt2);