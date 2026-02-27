const main = document.querySelector(".main");
// console.log(main);
const info = main.getBoundingClientRect();
console.log(info)

const height = main.getBoundingClientRect().height; //to get only height
console.log(height);

const topm = main.getBoundingClientRect().top; //to get top margin
console.log(topm);