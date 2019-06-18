#Common elements in two lists
l1=[1,2,3,4,5,6,7]
l2=[8,9,10,5,6,8,56,9]

def findCommon(l1,l2):
    count=0
    common=[]
    for i in l1:
        if i in l2:
            count=count+1
            common.append(i)
    return common,count

c,cu=findCommon(l1,l2)
print("Common of elements",c,"are",cu)