/*
keydown: It fires as a key is pressed down.

keyup: It fires as the key is released

keypress: It fires after a key is pressed down(after keydown). It only works with printable characters.

HTML:
    Home: <input type="text" id="mytext">

JavaScript:
    let txt = document.getElementById("mytext");

    function ke(e){
        console.log(e.type, "", e.keyCode, "", String.fromCharCode(e.keyCode));
    }

    txt.addEventListener("Keydown", ke, false);
    txt.addEventListener("Keypress", ke, false);
    txt.addEventListener("Keydown", ke, false);
*/
let txt = document.getElementById("mytext");

function ke(e){
    console.log(e.type+ " "+ e.keyCode+ " "+ String.fromCharCode(e.keyCode));
}

txt.addEventListener("keydown", ke, false);
txt.addEventListener("keypress", ke, false);
txt.addEventListener("keydown", ke, false);