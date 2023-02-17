const array1 = [1,2,3,4,5];
const array2 = [6,7,8,9];

const newArray = [array1];
console.log(newArray);

const newArray2 = [...array1];
console.log(newArray2);

const newArray3 = [...array1, array2];
console.log(newArray3);

const newArray4 = [...array1, ...array2];
console.log(newArray4);

const newArray5 = [...array1, ...array2, 24];
console.log(newArray5);

const s = [..."abc"];
console.log(s);