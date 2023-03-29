const bucket = ["coffee", "chips", "vegetables", "salt", "rice"];

/* produce */
const friedRicePromise = new Promise((resolve, reject)=>{
    if(bucket.includes("vegetables") && bucket.includes("salt") && bucket.includes("rice")){
        resolve("Fried Rice")
    }else{
        reject("Couldn't do it");
    }
})


/*consume (example1)*/
// friedRicePromise.then((myFriedRice)=>{
//     console.log("Let's eat: ", myFriedRice);
// }, (error)=>{
//     console.log("Promise can't be fullfilled...")
// });


/*consume (example2)*/
friedRicePromise.then((myFriedRice)=>{
    console.log("Let's eat: ", myFriedRice);
}).catch(
    (error)=>{
    console.log("Promise can't be fullfilled...")
});

/* 1:58:00 / 3:49:26 */