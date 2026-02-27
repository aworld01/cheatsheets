/*
Window vs Document:
Window
======
    1: Window is the main container or we can say the "Global Object" and any operations related to entire browser window can be part of window object.
    2: All the members like objects, methods, properties. If they are the part of window object then we don't refer the window object.
    3: Window has methods, properties and object.
    ex:
        setTimeout(), or setInterval() are the methods, whereas Documents is the object of the Window and it also has a screen object with properties describing the physical display.
Document
=======
    1: Whereas the DOM is the child of window object.
    2: Where in the DOM we need to refer the document, if we want to use the document object, methods or properties.
    3: Document is just the object of the global object that is Window, which deals with the document, the HTML elements themselves.

DOM vs BOM (DOM=Documet Object Model, BOM=Browser Object Model)
DOM Navigation
Searching and getting Elements Reference

consoleCommands:-
Window
    window: to get window object.
    window.history.back() to goback on history
    window.location: to get location url.
    location: to get location url. //we don't need to refer the window object.
    location.href: to get url
    innerHeight: to get Height of browserWindow
    innerWidth: to get Width of browserWindow
Document
    document: to access document
    document.documentElement: returns the Element that is the root element of the document.
    document.head: to access only head tag
    document.body: to access only body tag
    document.body.style.background = "grey";

    CHILD
    =====
    document.body.childNodes: to see the list of direct children only (include tab, enter, and whiteSpace)
    document.body.children: to see only regularElements (without textNode)
    document.body.children.length: to see the length of body child
    document.body.firstChild: to fecth firstChild of body including textNode (tab, enter, and whiteSpace)
    document.body.firstElementChild: to fech only regularElements (without textNode)

    PARENT
    =====
    document.body.parentNode: to see the parentNode
    document.body.parentElement: to see the parentNode

    SIBLING
    =======
    document.head.nextSibling //to check nextSibling
    document.body.previousSibling //to check previousSibling
    document.head.nextElementSibling //to check next sibling (without textNode)
    document.body.previousElementSibling //to check previous sibling (without textNode)

    SEARCH THE ELEMENTS
    ===================
    console.log(document.getElementsByClassName("para"))
    console.log(document.getElementsByTagName("p"));
    console.log(document.getElementsByName("txt"));
    console.log(document.getElementById("name").value); //for input fields
    console.log(document.querySelector("#heading")) //it finds first element
    console.log(document.querySelectorAll("p")) //returns all the elements

*/
