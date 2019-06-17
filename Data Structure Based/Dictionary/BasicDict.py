#Program - Basic dictionary creation


nList=[1,1,1,2,3,4,2]
d={}
def dictAdd(nList):
    d={}
    for i in nList:
       d[i]=nList.count(i)

    return d

d=dictAdd(nList)
print("The dictionary from the list",d)


