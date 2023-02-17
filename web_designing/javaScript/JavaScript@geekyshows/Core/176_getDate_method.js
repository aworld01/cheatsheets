/*
getFullYear(): Get the year as a four digit number(yyyy)
getMonth(): Get the month as a number(0-11)
getDate(): Get the day as a number(1-31)
getHours(): Get the hour(0-23)
getMinutes(): Get the minute(0-59)
getSeconds(): Get the seconds(0-59)
getMilliseconds(): Get the milliseconds(0-999)
getTime(): Get the time(milliseconds since January 1, 1970)
getDay(): Get the weekday as a number(0-6)
*/

var tarikh = new Date();
console.log("Full Date: ",tarikh);

var hours = tarikh.getHours();
console.log("Hours: ",hours);

var minutes = tarikh.getMinutes();
console.log("Minutes: ",minutes);

var seconds = tarikh.getSeconds();
console.log("Seconds: ",seconds);

var date = tarikh.getDate();
console.log("Date: ",date);

var month = tarikh.getMonth();
console.log("Month",month);

var year = tarikh.getFullYear();
console.log("Year: ", year);

var day = tarikh.getDay();
console.log("Day: ", day);

