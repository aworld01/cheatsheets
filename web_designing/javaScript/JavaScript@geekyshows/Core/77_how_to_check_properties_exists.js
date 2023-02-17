/* check properties exists in JavaScript */
/* example-1 */
// function Mobile(model_no){
//     this.model = model_no;
//     this.memory = 4;
// }
// var samsung = new Mobile('Galaxy');
// var nokia = new Mobile('3310');
// if(typeof nokia.memory !== 'undefined'){
//     console.log("Available");
// } else{
//     console.log("Doesn't Exist");
// }



/* example-2 */
// function Mobile(model_no){
//     this.model = model_no;
//     // this.memory = 4;
// }
// var samsung = new Mobile('Galaxy');
// var nokia = new Mobile('3310');
// if(typeof nokia.memory !== 'undefined'){
//     console.log("Available");
// } else{
//     console.log("Doesn't Exist");
// }






/* in keyword */
/* example-1 */
// function Mobile(model_no){
//     this.model = model_no;
//     this.memory = 4;
// }
// var samsung = new Mobile('Galaxy');
// var nokia = new Mobile('3310');
// if('memory' in nokia){
//     console.log("Available");
// } else{
//     console.log("Doesn't Exist");
// }



/* example-2 */
// function Mobile(model_no){
//     this.model = model_no;
//     // this.memory = 4;
// }
// var samsung = new Mobile('Galaxy');
// var nokia = new Mobile('3310');
// if('memory' in nokia){
//     console.log("Available");
// } else{
//     console.log("Doesn't Exist");
// }






/* hasOwnProperty() */
/* example-1 */
// function Mobile(model_no){
//     this.model = model_no;
//     this.color = 'white';
// }
// var samsung = new Mobile('Galaxy');
// var nokia = new Mobile('3310');
// if(nokia.hasOwnProperty('color')){
//     console.log("Available");
// } else{
//     console.log("Doesn't Exist");
// }



/* example-2 */
function Mobile(model_no){
    this.model = model_no;
}
var samsung = new Mobile('Galaxy');
var nokia = new Mobile('3310');
if(nokia.hasOwnProperty('color')){
    console.log("Available");
} else{
    console.log("Doesn't Exist");
}