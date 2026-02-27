const head1 = document.querySelector(".heading1");
const head2 = document.querySelector(".heading2");
const head3 = document.querySelector(".heading3");
const head4 = document.querySelector(".heading4");
const head5 = document.querySelector(".heading5");

function changText(element, text, color, time, callback){
    setTimeout(() => {
        element.textContent = text;
        element.style.color = color;
    }, time);
};

changText(head1, "One", "blue", 3000);
