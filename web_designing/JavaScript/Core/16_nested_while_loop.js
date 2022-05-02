var i = 1;

while(i <= 3)
{
    console.log(i, "Outer loop");
    i++
    var j = 1;
    while(j <= 5)
    {
        console.log(j, "Inner loop");           
    j++
    }
}