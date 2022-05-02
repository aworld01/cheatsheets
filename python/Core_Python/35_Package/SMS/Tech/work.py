"""/root/Tech/work.py"""

def tech_work():
    print("Tech Package/work Module")
    print("tech_work Function")
    print()




"""
You need to follow the steps below to execute siblings file

import sys
sys.path.append("/home/thor/Desktop/SMS/User")
import request
request.user_request()

OR

cd ..
python3 -m Tech.work
"""
from User import request
request.user_request()