/* You can make only one object using object literal */
var Mobile = function(model, sp){
    this.model = model;
    this.color = 'white';
    this.price = 3000;
    this.sp = sp;
    this.sellingprice = function(){
        return (this.price + this.sp);
    };
    this.data = function(){
        console.log("Model No: "+this.model);
        console.log("Price: "+this.sellingprice());
    }
};
var samsung = new Mobile('Galaxy',2000);
var nokia = new Mobile('3310',1000);
samsung.data()
console.log()
nokia.data()