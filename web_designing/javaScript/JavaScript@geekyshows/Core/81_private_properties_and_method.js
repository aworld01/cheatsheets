/* Using var, let, or const you can create private properties and methods. */
// var Mobile = function(model_no, sprice){
//     this.model = model_no;
//     this.color = 'white';
//     this.price = 3000;
//     this.sp = sprice;
//     this.show = function(){return "Hello world";};
// };
// var samsung = new Mobile('Galaxy',2000);
// var nokia = new Mobile('3310',1000);

// console.log(nokia.price);
// console.log(nokia.show());





var Mobile = function(model_no, sprice){
    this.model = model_no;
    this.color = 'white';
    var price = 3000; //To make this private
    this.sp = sprice;
    this.show = function(){return "Hello world";};
};
var samsung = new Mobile('Galaxy',2000);
var nokia = new Mobile('3310',1000);

console.log(nokia.price);
console.log(nokia.show());