/*
callbacks, callback hell, pyramid of doom
aSynchronous programming
*/
const head1 = document.querySelector(".heading1");
const head2 = document.querySelector(".heading2");
const head3 = document.querySelector(".heading3");
const head4 = document.querySelector(".heading4");
const head5 = document.querySelector(".heading5");

function change(){
    head1.textContent = "Heading1";
    head1.style.color = "blue";
    setTimeout()
}
setTimeout(() => {
    head1.textContent = "Heading1";
    head1.style.color = "blue";
    setTimeout(() => {
        head2.textContent = "Heading2";
        head2.style.color = "green";
        setTimeout(() => {
            head3.textContent = "Heading3";
            head3.style.color = "orange";
            setTimeout(() => {
                head4.textContent = "Heading4";
                head4.style.color = "purple";
                setTimeout(() => {
                    head5.textContent = "Heading5";
                    head5.style.color = "magenta";
                }, 2000);
            }, 2000);
        }, 2000);
    }, 2000);
}, 2000);


/* 01:10:37 / 03:49:26 */