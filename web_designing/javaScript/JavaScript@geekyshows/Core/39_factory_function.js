// function mobile(){
//     return {
//         model: 'Samsung-M30',
//         price: function(){
//             return "Price: Rs. 3000";}
//     };
// }
// var samsung = mobile();
// console.log("Model:", samsung.model)
// console.log(samsung.price())



function mobile(model_no){
    return {
        model: model_no,
        price: function(){
            return "Price Rs. 3000";}
    };
}
var samsung = mobile('Samsung-M30');
var nokia = mobile('Nokia-3320');
console.log(samsung.model)
console.log(samsung.price())
console.log()
console.log(nokia.model)
console.log(samsung.price())