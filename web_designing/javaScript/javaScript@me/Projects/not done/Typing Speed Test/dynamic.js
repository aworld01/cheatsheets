/*
Dynamic Typing Test
1: When user pressed start button then only active the textarea else disabled it and vice-versa.
2: Every time a new set of lines on top. Whenever a start button is pressed. Not the Done one.
3: Get the time and change the button text to done.
4: Get the end time when user clicked on done button. find the total time taken.
5: Find the total words on the setofwords.
6: Find the speed of the user and show it on top when user clicked on done.
7: Then call the compareWords fun and find how many of the words are matching and how many not. Display the result on top with speed. 
25:00 / 41:27
*/

/* creating Array */
const setOfWords = [
    "My name is Vinod Bahadur Thapa and I am a YouTuber.",
    "Hope you are having fun this is a simple game you can make.",
    "If you want the source code then link is given in the description",
    "So you can create your own version of this challenge."
];

n = setOfWords.length; //gettin length of setOfWords

let startTime, endTime;
const msg = document.getElementById("msg");
const typedWords = document.getElementById("mywords");
const btn = document.getElementById("btn");
btn.onclick = func1;

const playGame = () => {
    var randomNumber = Math.random()*n;
    var randomNumber = Math.floor(randomNumber);
    msg.innerText = setOfWords[randomNumber]

    /* to get start time */
    let date = new Date();
    startTime = date.getTime();

    /* Change buttonText */
    btn.innerText = "Done";
}

const endPlay = () => {
    let date = new Date();
    endTime = date.getTime();
    let totalTime = (endTime - startTime) / 1000;
    totalTime = Math.floor(totalTime);
    console.log(totalTime);
}

function func1(){
    if(this.innerText == "Start"){
        typedWords.disabled = false;
        playGame();
    }else if(this.innerText == "Done"){
        typedWords.disabled = true;
        btn.innerText = "Start";
        endPlay();
    }
}
