// // declaration of object (method1)
// var fees = {};
// fees["Rahul"] = 100;
// fees["Sumit"] = 200;
// fees["Rohan"] = 300;
// console.log(fees)
// console.log(fees["Rohan"])


// // declaration of object (method2)
// var fees = {};
// fees.Rahul = 100;
// fees.Sumit = 200;
// fees.Rohan = 300;
// fees.Abhishek_Kumar = 500;
// console.log(fees.Sumit)


// //Method
// var fees = {};
// fees["total"] = function(){
//     return(100+200);
// };
// console.log(fees["total"]());


// var fees = {};
// fees["total"] = function(){
//     return(300+200);
// };
// console.log(fees.total());


// var fees = {};
// fees.total = function(){
//     return(500+200);
// };
// console.log(fees.total());


// var fees = {};
// fees.total = sum;
// function sum(){
//     return(100+400+30);
// };
// console.log(fees.total());


// // declaration and initialization of object (Property)
// // method1
// var fees = {Rahul: 100, Sumit: 200, Rohan: 300};
// console.log(fees["Sumit"]);


// // method2
// var fees = {
//     Rahul: 100,
//     Sumit: 200,
//     Rohan: 300,
//     "Rajesh Kumar": 500
// };
// console.log(fees["Rajesh Kumar"])


// // method1
// var fees = {Rahul: 100, Sumit: 200, Rohan: 300, total:function(){return(300+300+100);}};
// console.log(fees.total());


// method2
var fees = {
    Rahul: 100,
    Sumit: 200,
    Rohan: 300,
    "Rajesh Kumar": 500,
    total: function(){return(500+200+400);}
};
console.log(fees.total());
console.log(fees["total"]());