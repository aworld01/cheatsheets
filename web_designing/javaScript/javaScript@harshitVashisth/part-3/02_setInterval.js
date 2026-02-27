/* example1 */
// var num = 0;
// function count(){
//     console.log(num);
//     num++
// }

// setInterval(count, 1000);


/* example2 */
var num = 0;
function count(){
    console.log(num);
    num++
}

const stop = setInterval(count, 1000);
if(num == 15){
    clearInterval(stop);
}
/* 00:31:00 / 3:49:26 */