#program to merge multiple strings into a list

import ast

# Initialization of strings
str1 = "'Geeks', 'for', 'Geeks'"
str2 = "'paras.j', 'jain.l'"
str3 = "'india'"

# Initialization of list
list = []

# Extending into single list
for x in (str1, str2, str3):
    list.extend(ast.literal_eval(x))

# printing output
print(list) 