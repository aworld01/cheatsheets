/* 
AH = Ampare per Hour;
v = Volt
w = Watts
pf = Power Fector

Require:-
    AH, v, load


let load = 300;
let pf = .8;
let v = 12;
let batteryAH = 150;

let w = (load / pf);
let dischargingCurrent = (w / v);
let batteryBackup = (batteryAH / dischargingCurrent);
//Note: We can use only 70% of Lead Acid Battery
letuseable = (batteryBackup * 70) / 100;
//or
let useable = (batteryBackup * .7);
console.log(useable);

minutes = (60 * .2);
*/




let batteryAH = 150;
let pf = .8;
let load = 300;
let v = 12;

function calculate(b, p, l, volt){
    let w = (l / p);
    let dischargingCurrent = (w / volt);
    let batteryBackup = (b / dischargingCurrent);
    let useable = (batteryBackup * .7);
    console.log(useable);
}

calculate(batteryAH, pf, load, v)