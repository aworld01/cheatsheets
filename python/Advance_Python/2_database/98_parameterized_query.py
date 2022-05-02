"""
A parameterized query is a query which can use the format or pyformat parameterization style for parameters and the parameter values supplied at execution.
These executed with MySQLCursor can use the %s and %(key)s format style.
%s is used as format style in the sql queries, while using tuple parameters.
%(key)s is used as format style in the sql queries, while using dictionary parameters.
Syntax:-
Tuple Parameters
    sql = "INSERT INTO Students(name, roll, fees) VALUES(%s, %s, %s)"
    cur.execute(sql, ("Rohan", 111, 6000))

    sql = "INSERT INTO Students(name, roll, fees) VALUES(%s, %s, %s)"
    params = ("Rohan", 111, 6000)
    cur.execute(sql, params)

Dictionary Parameters
    sql = "INSERT INTO Students(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
    params = {"name": "Kajal", "roll": 777, "fees": 54100}
    cur.execute(sql, params)
"""