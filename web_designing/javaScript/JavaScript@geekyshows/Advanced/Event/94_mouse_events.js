/*
mousedown: It fires when mouse button is pressed down;

mouseup: It fires when the mouse button is released;

click: It fires when something is clicked, mousedown, mouseup and click events fires in sequence.

dblclick: It fires when something is clicked twice in rapid succession. mousedown, mouseup, click, mousedown, mouseup, click, and dblclick events fires in sequence.

mouseenter: It fires when a mouse starts to hover over some element. No bubble.

mouseleave: It fires when a mouse exits while hovering over some element. No bubble.

mouseover: It fires when mouse is hovering over some element.

mouseout: It fires when mouse leaves from hovering over some element.

mousemove: It fires when the mouse moves.

contextmenu: It fires when mouse right button is clicked.


HTML
    <button id="mybtn">Click</button>
    <script src="event1.js"></script>

JavaScript:
    function disp(event){
        document.body.style.backgroundColor = "#00aced";
        document.body.style.color = "white";
    }

    //example-1
    btn = document.getElementById("mybtn");
    btn.addEventListener("contextmenu", disp, false);

    //example-2
    document.getElementById("mybtn").oncontextmenu = disp;
*/

function disp(event){
    document.body.style.backgroundColor = "#00aced";
    document.body.style.color = "white";
}

btn = document.getElementById("mybtn");

/* example-1 */
// btn.addEventListener("mousedown", disp, false);

/* example-2 */
// btn.addEventListener("mouseup", disp, false);

/* example-3 */
// btn.addEventListener("click", disp, false);

/* example-4 */
// btn.addEventListener("dblclick", disp, false);

/* example-5 */
// btn.addEventListener("mouseenter", disp, false);

/* example-6 */
// btn.addEventListener("mouseleave", disp, false);

/* example-7 */
// btn.addEventListener("mouseover", disp, false);

/* example-8 */
// btn.addEventListener("mouseout", disp, false);

/* example-9 */
// btn.addEventListener("mousemove", disp, false);

/* example-10 */
// btn.addEventListener("contextmenu", disp, false);

/* example-11 */
document.getElementById("mybtn").oncontextmenu = disp;