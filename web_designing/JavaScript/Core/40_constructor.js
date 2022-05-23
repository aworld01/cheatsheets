// function Mobile(){
//     this.model = 'Samsung-M30';
//     this.price = function(){
//         console.log(this.model)
//         console.log("Rs. 3000");
//         console.log()
//     }
// }
// var samsung = new Mobile();
// var nokia = new Mobile()
// samsung.price();
// nokia.price()



// constructor with parameter
function Mobile(model_no){
    this.model = model_no;
    this.price = function(){
        console.log(this.model)
        console.log("Rs. 3000");
        console.log()
    };
}
var samsung = new Mobile("Samsung-M30");
var nokia = new Mobile("Nokia-3310");
samsung.price();
nokia.price();