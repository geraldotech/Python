"""
import os

out = os.path.basename("/baz/foo")
mypath = os.path.join('c:%s' % os.sep, "Users", %userprofile%)
print(mypath)
"""
import os
print(os.environ['USERPROFILE'],"desktop")

docs = os.path.join(os.environ['USERPROFILE'], "Desktop")
print(docs)


#https://stackoverflow.com/questions/38544618/userprofile-env-variable-for-python")
#https://www.w3resource.com/python-exercises/python-basic-exercise-43.php
