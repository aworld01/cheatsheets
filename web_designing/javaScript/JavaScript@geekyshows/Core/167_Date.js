/*
The Date object provides a sophisticated set of methods for manipulationg dates and times.
It reads client machine date and time so if the client's date or time is incorrect, your script will reflect this fact.

Days of week and months of the year are enumerated beginning with zero.
example:-
    0-Sunday, 1-Monday and so on.
    0-January, 1-February and so on.

Days of month begins with one.

Creating Date Object:----
Date objects are created with the new Date() constructor. Date Object created by programmers are static. They don't contain a ticking clock.
Syntax:-
    new Date();
    new Date(milliseconds);
    new Date(year, month, day, hours, minutes, seconds, milliseconds); //minimum 2, maximum 7.
    new Date(dateString);
*/