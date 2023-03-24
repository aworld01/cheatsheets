/*
document = rootNode
HTML = rootElement (childNode of document)
head = childNode of HTML
home = textNode (childNode of HTML)
body = childNode of HTML
title = childNode of head
h1 = childNode of body
Heading One = textNode and so on


document
<HTML>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Heading One</h1>
    </body>
</HTML>
*/

const rootNode = document.getRootNode(); //to access childNode
console.log("rootNode =>", rootNode);
console.log("\n");

let rootNodeChilds = rootNode.childNodes; //to access rootNode's childNodes
console.log("rootNode childNodes =>", rootNodeChilds);
console.log("\n");

const html = rootNode.childNodes[0]; //to access HTML Node
console.log("HTML node = >", html);
console.log("\n");

const htmlChild = html.childNodes; //to access htmlChildNodes
console.log("HTMLChild", htmlChild);
console.log("\n");

let head = htmlChild[0]; //to access headNode
console.log(head);
console.log("\n");

const text1 = htmlChild[1]; //to access textNode
console.log("textNode =>",text1);
console.log("\n");

console.log("bodyNode =>", htmlChild[2]); //to access bodyNode
console.log("\n");

console.log("headNextSibling =>", head.nextSibling); //to access head's nextSibling node
console.log("\n");

console.log("textNextSibling",text1.nextSibling);
console.log("\n")

console.log("textNode Parent =>", text1.parentNode); //to check textNode parentNode
console.log("\n")

console.log("headElementSibling =>",head.nextElementSibling); //to ignore text nodes
console.log("\n");

console.log("headChilds =>", head.childNodes);

console.log("headChildren =>", head.children); //to ignore text nodes