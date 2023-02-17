let num = [4, 6, 8, 29, 24];
let t = 29;

function findTarget(array, target){
    for(let i = 0; i<array.length; i++){
        if(array[i] === target){
            return i;
        }
    }
    return "not found"
}

ans = findTarget(num, t);
console.log(ans);