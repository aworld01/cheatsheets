/*
const input = document.querySelector(".string").value; //to input field

//example-0
HTML
    <button onclick="console.log('Hello world!!!')">clickMe</button>


//example-1
HTML
    <button onclick="disp()">clickMe</button>


HTML
    <button id="mybtn">Click</button>
    <script src="event1.js"></script>

JavaScript
function disp(){
    document.body.style.backgroundColor = "#00aced";
    document.body.style.color = "white";
}

//example-1
btn = document.getElementById("mybtn");
btn.onclick = disp;


//example-2
document.getElementById("mybtn").onclick = disp;

// example-3
// btn.addEventListener("click", disp, false);

*/

function disp(){
    document.body.style.backgroundColor = "#00aced";
    document.body.style.color = "white";
}


/* example-1 */
// btn = document.getElementById("mybtn");
// btn.onclick = disp;

/* example-2 */
document.getElementById("mybtn").onclick = disp;