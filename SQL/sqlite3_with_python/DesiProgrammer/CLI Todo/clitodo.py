import dbhelper2
import os

os.system('clear') 

ch = int(input('Choose What you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. QUIT\n\t>'))

while ch != 4:
    if(ch == 1):
        os.system('clear')
        print('ID' + '\t' + 'TASK\n\n')
        for rows in dbhelper2.show():
            print(str(rows[0]) + '\t' + rows[1])
        ch = int(input('Choose What you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. QUIT\n\t>'))
    elif(ch == 2):
        task = input('Enter A Task: ')
        if(len(task) != 0):
            dbhelper2.insertdata(task)
        ch = int(input('Choose What you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. QUIT\n\t>'))
    elif(ch == 3):
        os.system('clear')
        print('ID' + '\t' + 'TASK\n\n')
        for rows in dbhelper2.show():
            print(str(rows[0]) + '\t' + rows[1])
        id = int(input('Choose a Task ID To Delete: '))
        dbhelper2.deletebyid(id)
        ch = int(input('Choose What you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. QUIT\n\t>'))
    else:
        print('Choose A Currect Option')
        ch = int(input('Choose What you want ?\n\t1. View Task\n\t2. Add a Task\n\t3. Delete a Task\n\t4. QUIT\n\t>'))
else:
    print('Thank You For Using The Application!!!')