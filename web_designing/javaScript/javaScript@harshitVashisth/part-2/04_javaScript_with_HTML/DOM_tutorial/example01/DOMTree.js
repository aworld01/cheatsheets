/*
document = rootNode
HTML = rootElement (childNode of document)
head = childNode of HTML
title = childNode of head
home = textNode
body = childNode of HTML
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

const rootNode = document.getRootNode(); //to get rootNode

// console.log(rootNode);

// console.log(rootNode.childNodes); //to access childNode

const htmlElementNode = rootNode.childNodes[0]; //to access HTML childNodes
// console.log(htmlElementNode);

// const htmlChild = htmlElementNode.childNodes;
// console.log(htmlChild);

// const textNode1 = htmlElementNode.childNodes[1];
// console.log(textNode1);


console.log(htmlElementNode.parentNode); //to check parentNode





/* 5:00:00 / 8:13:32 */