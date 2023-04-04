var area = "circle";
var PI = 3.142, length = 5, width = 4, redios = 3;

/* example1 (if-else) */
// if(area == "circle"){
//     console.log("The area of the circle is: " + PI*redios**2);
// }else if(area == "triangle"){
//     console.log("The area of the triangle is: " + (length*width)/2);
// }else if(area == "rectangle"){
//     console.log("The area of the rectangle is: " + length*width);
// }else{
//     console.log("please enter a valid data");
// }



/* example1 (switchStatement) */
switch(area){
    case "circle":
        console.log("The area of the circle is: " + PI*redios**2);
        break
    case "triangle":
        console.log("The area of the triangle is: " + (length*width)/2);
        break
    case "rectangle":
        console.log("The area of the rectangle is: " + length*width);
        break
    default:
        console.log("please enter a valid data");
}
