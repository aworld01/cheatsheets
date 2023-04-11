/* converting 2d and 3d array into one dimensional array */
const arr = [
    ["Zone1", "Zone2",],
    ["Zone3", "Zone4"],
    ["Zone5", "Zone6"],
    ["Zone7", "Zone8"]
];
console.log(arr)

let flatArr = arr.reduce((accu, currVal) => {
    return accu.concat(currVal);
})
console.log(flatArr);