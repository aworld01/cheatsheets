/*
// const random = Math.random(); //to generate random number <1

// const rand10 = Math.random() * 10; //to generate random number <10

const randFloor = Math.floor(Math.random() * 10); //to generate a random number in string form
console.log(randFloor);
*/

const btn = document.querySelector("button"); //to select button
const body = document.body; //to select body
const colorCode = document.querySelector(".currentColor");
console.log(colorCode.textContent);

function randomColorGenerator(){
    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);
    const randomColor = `rgb(${red}, ${green}, ${blue})`;
    return randomColor;
}

btn.addEventListener("click", ()=>{
    const randomColor = randomColorGenerator();
    body.style.background = randomColor;
    colorCode.textContent = randomColor;
});

/* 7:18:50 / 8:13:32 */