function myfunc(power){
    return function(number){
        return number ** power
    }
}

const square = myfunc(2);
const result = square(3);
console.log(result);