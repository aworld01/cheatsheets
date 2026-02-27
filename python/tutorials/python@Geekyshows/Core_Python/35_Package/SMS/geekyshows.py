"""/root (Service Management System)"""
"""1:20:01/1:26:20"""

"""example-1"""
# import Admin.product
# Admin.product.admin_product()

# import Admin.Common.footer
# Admin.Common.footer.admin_common_footer()

# import User.profile
# User.profile.user_profile()



"""example-2"""
# from Admin import product
# product.admin_product()

# from Admin.Common import footer
# footer.admin_common_footer()

# from User import profile
# profile.user_profile()



"""example-3"""
# from Admin.product import admin_product
# admin_product()

# from Admin.Common.footer import admin_common_footer
# admin_common_footer()

# from User.profile import user_profile
# user_profile()



"""example-3"""
# from Admin import product, service
# product.admin_product()
# service.admin_service()

# from Admin.Common import footer, header
# footer.admin_common_footer()
# header.admin_common_header()

# from User import profile, request
# profile.user_profile()
# request.user_request()



# """example-4
# ("Admin/__init__.py/__all__ = ["product", "service"] #to export all modules")"""
# from Admin import *
# product.admin_product()
# service.admin_service()

# """("Admin/Common/__init__.py/__all__ = ["footer", "header"] #to export all modules")"""
# from Admin.Common import *
# footer.admin_common_footer()
# header.admin_common_header()



"""example-5"""
from Admin import *
from Admin.Common import *
product.admin_product()
service.admin_service()
footer.admin_common_footer()
header.admin_common_header()