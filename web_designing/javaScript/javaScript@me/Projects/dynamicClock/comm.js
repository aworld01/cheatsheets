/*
setInterval(): method is continue calling the function until clearInterval() is called.

clearInterval(): The clearInterval() method stops the executions of the function specified in teh setInterval() method.
*/


var clock = setInterval(timing, 1000);
function timing(){
    var d = new Date(); //to create instance of date;
    var t = d.toLocaleTimeString();
    document.getElementById('showClock').innerHTML = t;
}