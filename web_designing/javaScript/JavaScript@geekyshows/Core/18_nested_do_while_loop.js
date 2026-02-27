var i = 1;
do
{
    console.log(i, "Outer loop");
    i++
    var j = 1
    do
    {
        console.log(j, "Inner loop");
        j++
    } while(j <= 5);
}while(i <= 3);