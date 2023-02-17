int = document.getElementById("ent").value.toUpperCase();
lst = document.getElementById("list")

function chat(){
    var you = document.createElement("p"); //to create a paragraph.
    var txtNode = document.createTextNode(int); //to create textNode.
    you.appendChild(txtNode); //to add text in paragraph.
    lst.appendChild(you); //to add in body.

    if(int == "HI"){
        var me = document.createElement("p"); //to create a paragraph.
        var txtNode = document.createTextNode("Hello"); //to create textNode.
        me.appendChild(txtNode); //to add text in paragraph.
        lst.appendChild(me); //to add in body.
        me.style.textAlign="right"
    }else{
        var me = document.createElement("p"); //to create a paragraph.
        var txtNode = document.createTextNode("Say that again"); //to create textNode.
        me.appendChild(txtNode); //to add text in paragraph.
        lst.appendChild(me); //to add in body.
        me.style.textAlign="right"
        me.toUpperCase()
    }
}