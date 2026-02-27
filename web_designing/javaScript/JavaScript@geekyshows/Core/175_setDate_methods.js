/*
Date methods
============
setTime(): Sets a date to a specified number of milliseconds after/before January 1, 1970.
setUTCDate(): Sets the day of the month of a date object, according to universal time.
setUTCFullYear(): Sets the year of a date object, according to universal time.
setUTCHours(): Sets the hour of a date object, according to universal time.
setUTCMilliseconds(): Sets the millliseconds of a date object, according to universal time.
setUTCMinutes(): Sets the minutes of a date object, according to universal time.
setUTCMonth(): Sets the month of a date object, according to universal time.
setUTCSeconds(): Sets the seconds of a date object, according to universal time.
toDateString(): Convert the date portion of a Date object into a readable string.
toTimeString(): Converts the time portion of a Date object to a string.
toISOString(): Returns the date as a string, using the ISO standard.
toJSON(): Returns the date as a string, formatted as a JSON date.
toLocaleDateString(): Returns the date portion of a Date object as a string, using locale conventions.
toLocaleTimeString(): Returns the time portion of a Date object as a string, using locale conventions.
toString(): Converts a Date object to a string.
toUTCString(): Converts a Date object to a string, according to universal time.
UTC(): Returns the number of milliseconds in a date since midnight of January 1, 1970, according to UTC time.
valueOf(): Returns the primitive value of a Date object.

Set Date methods
================
setDate(): Set the day as a number(1-31)
setFullYear(): Set the year (optionally month and day)
setHours(): Set the hour(0-23)
setMilliseconds(): Set the milliseconds(0-999)
setMinutes(): Set the minutes(0-59)
setMonth(): Set the month(0-11)
setSeconds(): Set the seconds(0-59)
setTime(): Set the time(milliseconds since January, 1, 1970)
*/

var tarikh = new Date();
console.log(tarikh);

tarikh.setHours(22); //to set hours
console.log(tarikh);

tarikh.setMinutes(56); //to set minutes
console.log(tarikh);

tarikh.setSeconds(40); //to set seconds
console.log(tarikh);

tarikh.setDate(26); //to set date
console.log(tarikh);

tarikh.setMonth(11); //to set month
console.log(tarikh);

tarikh.setFullYear(2012); //to setFullYear
console.log(tarikh);

tarikh.setFullYear(2012, 3, 15); //to setFullYear and date (optionally)
console.log(tarikh);