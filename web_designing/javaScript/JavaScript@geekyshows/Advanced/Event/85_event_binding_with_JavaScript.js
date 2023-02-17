/*
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