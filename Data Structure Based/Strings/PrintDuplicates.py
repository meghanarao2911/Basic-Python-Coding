#program to print duplicates

def printDupes(str):

    str2=" "
    str=str.lower()
    #print(str)
    for i in str:
        if i not in str2:
            str2=str2+i
    return str2

str="MMMeeghana"
str2=printDupes(str)
print("Print original string is",str)
print("Strings with duplicates",str2)