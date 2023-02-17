async function redirect(){
    document.body.innerHTML = ""
    let n = await eel.generate_data()();

    /* adding elements */
    /* adding div and its attribute */
    var soft = document.createElement("div");
    soft.setAttribute("class","output");
    document.body.appendChild(soft);

    /* adding a heading */
    var h = document.createElement("h1");
    var t = document.createTextNode("SOFTWARE INFORMATION");
    h.appendChild(t);
    soft.appendChild(h);

    /* creating a table */
    var table = document.createElement("table");
    var i = 0;
    for (const[key,value] of Object.entries(n)){
        var row = table.insertRow(i)
        var cell1 = row.insertCell(0)
        var cell2 = row.insertCell(1)
        cell1.innerHTML = key;
        cell2.innerHTML = value;
        soft.appendChild(table);
        i = i+1;
    }



    /* adding a heading */
    var hr = document.createElement("hr");
    soft.appendChild(table);
}