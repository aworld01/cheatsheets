/*
Example1
HTML:-
    <body>
        <h1 style="text-align: center">Events</h1>
        <div class="rapper" style="text-align: center;">
            <input type="text" placeholder="Type something..."><br><br>
            <button class="btn" onclick="show()">clickMe</button>
        </div>
    </body>

javaScript:-
    function show(){
    console.log("Hello world!")
}


Example2
HTML:-
    <body>
        <h1 style="text-align: center">Events</h1>
        <div class="rapper" style="text-align: center;">
            <input type="text" placeholder="Type something..."><br><br>
            <button class="btn">clickMe</button>
        </div>
    </body>

javaScript:-
    function show(){
        console.log("Hello world!")
    }

    const btn = document.querySelector(".btn");
    btn.onclick = show;


Example3
HTML:-
    <body>
        <h1 style="text-align: center">Events</h1>
        <div class="rapper" style="text-align: center;">
            <input type="text" placeholder="Type something..."><br><br>
            <button class="btn">clickMe</button>
        </div>
    </body>

javaScript:-
    function show(){
        console.log("Hello world!")
    }

    const btn = document.querySelector(".btn");
    btn.addEventListener("click", show);

*/
function show(){
    console.log("Hello world!")
}

const btn = document.querySelector(".btn");
btn.addEventListener("click", show);