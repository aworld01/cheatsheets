/*
multiDimensional array is Arrays of Arrays;
multiDimensional array can be 2D, 3D, 4D etc.
*/

/* Initiolizing empty 2D array */
let students = [[], [], []];
// console.log(students);

/* aasigning value in 2D Array */
students[0][0] = "Rahul";
students[0][1]="Dell";
students[0][2]=10;
// console.log(students);

students[1][0]="Sonam";
students[1][1]="Hp";
students[1][2]=20;
// console.log(students);
    
students[2][0]="Jay";
students[2][1]="Zed";
students[2][2]=30;
// console.log(students);

let n = students.length;

for(let i=0; i<n; i++){
    console.log(students[i]);
}