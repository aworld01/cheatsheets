const body = document.body;
const btn = document.querySelector("button");

const intervalId = setInterval(() => {
    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);
    const rgb = `rgb(${red}, ${green}, ${blue})`;
    body.style.background = rgb;
}, 1000);

btn.addEventListener("click", () => {
    clearInterval(intervalId);
    btn.style.background = "red";
});