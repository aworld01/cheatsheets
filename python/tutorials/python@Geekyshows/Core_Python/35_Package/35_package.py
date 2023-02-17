"""
Packages are a way of structuring Python's module namespace by using "dotted module names".
A package can have one or more modules which means, a package is collection of modules and packages.
A package can contain packages.
Package is nothing but a Directory/Folder.
Package is nothing but a Directory/Folder which MUST contain a special file called __init__.py.
__init__.py file can be empty, it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

1)HOW TO USE PACKAGE
Syntax:-
    import packageName.moduleName
    import packageName.subPackageName.moduleName
Example:-
    import Admin.service #package name should be start from capital letter (convension)
    import Admin.Common.footer

HOW TO ACCESS VARIABLE, FUNCTION, METHOD, CLASS
Syntax:-
    packageName.moduleName.functionName()
    packageName.subPackageName.moduleName.functionName()
Example:-
    Admin.service.admin_service()
    Admin.Common.footer.admin_common_footer()

2)HOW TO USE PACKAGE
Syntax:-
    from packageName import moduleName
    from packageName.subPackageName import moduleName
Example:-
    from Admin import service
    from Admin.Common import footer

HOW TO ACCESS VARIABLE, FUNCTION, METHOD, CLASS
Syntax:-
    moduleName.functionName() #no need package name
Example:-
    service.admin_service() #no need package name
    footer.admin_common_footer()

3)HOW TO USE PACKAGE (importing function)
Syntax:-
    from packageName.moduleName import func_name
    from packageName.subPackageName.moduleName import func_name
Example:-
    from Admin.service import admin_service
    from Admin.Common.footer import admin_common_footer

HOW TO ACCESS VARIABLE, FUNCTION, METHOD, CLASS
Syntax:-
    functionName() #no need Package and subPackage name
Example:-
    admin_service() #no need Package and subPackage name
    admin_common_footer()

4)HOW TO USE PACKAGE (__all__)
If a package's __init__.py code defines a list named __all__, it taken to be the list of module names that should be imported when from package import * is encountered.
__init__.py / __all__["dashboard", "service", "product"]

27:00/1:26:20
"""