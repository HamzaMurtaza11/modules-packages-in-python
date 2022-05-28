#how to work on modules:
#modules are way to organize different python files to keep things much clean and better for long projects.
#if we want to import the code written in other python file to current python file than imported file is called module.
#if imported file is in a folder than that folder is call a package.

#example: we will import our own made module "working":
#for this purpose will make a python file and name it "working.py"
#and then after it, we will import that file here.

import working
from package_shopping import shopping #we are importing package "package_shopping"

var1=working.square_of_number(2)
print(var1)

var2=working.square_root(4)
print(var2)

print(shopping.shopy("shoes"))

