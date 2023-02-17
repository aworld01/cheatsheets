var tarikh = new Date();
var month = tarikh.getMonth();
var day = tarikh.getDay();

console.log(monthFun(month));
console.log(dayFun(day));

function monthFun(monthNum){
    var monthNam = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    return monthNam[monthNum];
}

function dayFun(dayNum){
    var dayNam = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"];
    return dayNam[dayNum];
}