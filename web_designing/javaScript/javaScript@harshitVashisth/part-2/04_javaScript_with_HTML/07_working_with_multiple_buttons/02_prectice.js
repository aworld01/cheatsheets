const btns = document.querySelectorAll(".wrapper button");

for(let button of btns){
    button.addEventListener("click", (e) =>{
        const btn = e.currentTarget;
        btn.style.background = "yellow";
        btn.style.color = "blue";
    })
}

/* 7:06:50 / 8:13:32 */