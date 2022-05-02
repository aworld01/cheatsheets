"""
Types of menus:- 
add_command
add_cascade
add_separator
"""
from tkinter import*
from tkinter import messagebox
"""defining function"""
def employeeDetails():
    messagebox.showinfo("Employee Information","Name: Abdul Zoha")

root = Tk()
root.title("Tkinter")
root.geometry("800x500+250+50")
root.resizable(False,False)
root.config(bg="#262626")
"""defining a menu"""
"""add_command"""
# myMenu = Menu(root)
# myMenu.add_command(label="Employee",command=employeeDetails)
# myMenu.add_command(label="Employee",command=employeeDetails)

"""Submenus"""
myMenu = Menu(root)
detailsMenu=Menu(myMenu,tearoff=0)
detailsMenu.add_command(label="Add Employee",command=employeeDetails)
detailsMenu.add_command(label="Delete Employee",command=employeeDetails)
detailsMenu.add_command(label="View Employee",command=employeeDetails)


## add_cascade
# employeeMenu=Menu(myMenu)
# employeeMenu=Menu(myMenu,tearoff=0) #to disable tearoff
# employeeMenu.add_command(label="Add Employee",command=employeeDetails)
# employeeMenu.add_command(label="Delete Employee",command=employeeDetails)
# employeeMenu.add_cascade(label="View Employee",menu=detailsMenu)

# departmentMenu=Menu(myMenu,tearoff=0)
# departmentMenu.add_command(label="Add",command=employeeDetails)
# departmentMenu.add_command(label="Delete",command=employeeDetails)
# departmentMenu.add_separator() #to add a separator between two menus
# departmentMenu.add_command(label="View",command=employeeDetails)

# myMenu.add_cascade(label="Employee",menu=employeeMenu)
# myMenu.add_cascade(label="Department",menu=departmentMenu)

root.config(menu=myMenu)

root.mainloop()