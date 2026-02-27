'''
sleep() method: This method is used to stop execution of a program temporarily for a given amoumt of time. When this function is called, PVM stops program execution for given amount of time.

It belongs to time module.
'''

import time
for i in range(11):
	time.sleep(1)
	print(i)
	if i==5:
		time.sleep(5)
		print(i)