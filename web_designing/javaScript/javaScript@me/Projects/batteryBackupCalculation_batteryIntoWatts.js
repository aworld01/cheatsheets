/*
V = Volts
I = Ampare
W = Watts
PF = Power Fector

Require:-
    V, I, PF


let V = 12;
let I = 150;
let PF = .8;

let kVA = (V * I);
let W = (kVA * PF);
//Note: We can use only 70% of Lead Acid Battery
letuseable = (batteryBackup * 70) / 100;
//or
let useable = (batteryBackup * .7);
console.log(useable);

minutes = (60 * .2);
*/


let V = 12;
let I = 150;
let PF = .8;
function calculate(v, i, pf){
    let kVA = (v * i);
    let W = (kVA * pf);
    //Note: We can use only 70% of Lead Acid Battery
    let useable = (W * .7);
    let final = Math.round(useable)
    console.log(final, "Watts");
}
calculate(V,I,PF)