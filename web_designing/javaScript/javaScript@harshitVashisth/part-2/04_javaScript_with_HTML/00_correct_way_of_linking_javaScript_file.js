/*
Parsing = Reading

example-1
<head>
    <script src="dinamic.js"></script> <!-- it may stop loading html elements and throw errors -->
    <title>Testing</title>
</head>

example-2
<body>

    <script src="dinamic.js"></script> <!-- it may takes so much time to Parsing, Loading, and Executing -->
</body>

example-3
<head>
    <script src="dinamic.js" async></script> <!-- it may parse only half file and try to execute and can throw errors -->
    <title>Testing</title>
</head>

example-4
<head>
    <script src="dinamic.js" defer></script> <!-- it wil parse full file then execute (best way) -->
    <title>Testing</title>
</head>
*/