// // Property
// // declaration of object (method1)

// var fees = new Object();
// fees["Rahul"] = 100;
// fees["Sumit"] = 200;
// fees["Rohan"] = 300;
// console.log(fees["Sumit"]);



// // declaration of object (method2)
// var fees = new Object();
// fees.Rahul = 100;
// fees.Sumit = 200;
// fees.Rohan = 300;
// fees.Abhishek_Kumar = 500;
// console.log(fees.Rohan)



// // Method
// var fees = new Object();
// fees["total"] = function() {return(300+200);};
// console.log(fees["total"] ());



// var fees = new Object();
// fees["total"] = function() {return(400+200);};
// console.log(fees.total());



// var fees = new Object();
// fees.total = function() {return(500+200);};
// console.log(fees.total());



var fees = new Object();
fees.total = sum;
function sum(){
    return(100+400+30);
}
console.log(fees.total());