/*
A Leap Year has 366 days (the exatra day is the 29th of February)

How th know if it is a Leap Year:-
1: Leap Years are any year that can be exactly divided by 4 (such as 2016, 2020, 2024, etc)
    2: except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
        3: exept if it can be exactly divided by 400, then it is (such as 2000, 2400)
*/

var year = 2022;

if(year % 4 === 0){
    if(year % 100 === 0){
        if(year % 400 === 0){
            console.log("The year " + year + " is a leap year");
        }else{
            console.log("The year "+ year + " is not a leap year");
        }
    }else{
        console.log("The year " + year + " is a leap year");
    }
}else{
    console.log("The year "+ year + " is not a leap year");
};