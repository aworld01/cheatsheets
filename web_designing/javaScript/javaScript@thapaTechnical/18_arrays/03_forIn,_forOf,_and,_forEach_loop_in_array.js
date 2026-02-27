
let students = ["Rahul", "Mahesh", "Abid", "Subhan", "Akbar"];

/* traditional way */
// for(let i=0; i<students.length; i++){
//     console.log(`${i} => ${students[i]}`);
// }


/* After ES6 we have for..in and we have for..of loop too */
/* for..in loop (returns index of element) */
// for(let index in students){
//     console.log(`${index} => ${students[index]}`);
// }


/* for..of loop (returns element) */
// for(let elements of students){
//     console.log(elements);
// }


/* .forEach loop (returns element and index), this is Array.prototype */
students.forEach(function(element, index, array){
    console.log(`${index} => ${element}`);
});