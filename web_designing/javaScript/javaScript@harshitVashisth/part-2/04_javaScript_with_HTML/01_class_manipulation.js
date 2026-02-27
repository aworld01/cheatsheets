let para = document.querySelector(".para");
// console.log(para);
// console.log(para.classList); //to change into DOMTokenList

function added(){
    para.classList.add("bg", "fg", "align"); //to add classList
}

function removed(){
    para.classList.remove("bg", "fg"); //to remove classList
}

function cleared(){
    para.classList.remove("bg", "fg", "align");
}