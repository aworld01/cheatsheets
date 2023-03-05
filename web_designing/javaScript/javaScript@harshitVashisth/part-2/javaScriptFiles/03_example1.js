function func(){
    let counter = 0;
    return function(){
        if(counter < 1){
            console.log("Hi you called me");
            counter++;
        }else{
            console.log("mai already ek bar call ho chuka hun");
        }
    }
}

const myf = func();
myf();
myf();