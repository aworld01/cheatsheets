/* object literal (You can make only one object using object literal) */
// var fees = {}; // creating an empty object.
// console.log(fees);

/* assigning values */
// fees["Rahul"] = 100;
// fees["Sumit"] = 200;
// fees["Rohan"] = 300;
// console.log(fees);






/* Object Constructor */
// var fees = new Object(); // creating an empty object.
// console.log(fees);

// fees["total"] = function() {return(300+250);};
// console.log("a: ",fees);

// console.log("b: ",fees["total"])

// console.log("c: ",fees["total"]())






/* You can make multiple objects using Factory Function */
// function mobile(){
//     return {
//         model: "Samsung-M31",
//         price: function(){
//             return "Price: Rs. 3000";}
//         };
//     }
//     var sam = samsung = mobile();
// console.log(samsung.model);
// console.log(samsung.price());






/* Constructor Function */
function Mobile(){
        this.model = 'Samsung-M30';
        this.price = function(){
            console.log(this.model, "Rs. 3000");
        }
    }
    var samsung = new Mobile();
    var nokia = new Mobile()
    samsung.price();
    nokia.price()