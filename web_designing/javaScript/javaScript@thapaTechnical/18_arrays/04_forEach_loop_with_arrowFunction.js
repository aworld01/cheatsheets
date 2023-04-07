let students = ["Rahul", "Mahesh", "Abid", "Subhan", "Akbar"];

/* .forEach loop */
// students.forEach(function(element, index, array){
//     console.log(`${index} => ${element}`);
// });


/* .forEach loop with arrowFunction */
students.forEach((element, index, array) =>{
    console.log(`${index} => ${element}`)
});