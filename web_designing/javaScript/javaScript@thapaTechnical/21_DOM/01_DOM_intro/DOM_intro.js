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
    window.history.back() //to goback on history
    window.location: to get location url.
    location: to get location url. //we don't need to refer the window object.
    location.href: to get url
    innerHeight: to get Height of browserWindow
    innerWidth: to get Width of browserWindow
Document
    document: to access document
    document.documentElement: to access only root element
    document.head: to access only head tag
    document.body: to access only body tag
    document.body.style.background = "grey";

*/
