Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def sqroot(n):
	if n < 0:
		return False
	else:
		root = math.sqrt(n)
		floored = math.floor(root)
		if root * floored == n:
			return True
		else:
			return False

		
>>> 