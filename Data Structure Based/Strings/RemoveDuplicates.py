#function to remove duplicates

def removeDupes(str):

    list1=" "
    str=str.lower()
    for i in str:
        if i not in list1:
            list1=list1+i
    return list1

str="MMmeeghana"
s=removeDupes(str)

print("The original string",str)
print("After removal of duplicates",s)