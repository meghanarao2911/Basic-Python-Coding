a=[10,20,30,50,78,34,1,233,11111]

def maxinList(a):
    m=a[0]
    for i in a:
        if i>=m:
            m=i
    print("The largest element in the list is",m)

maxinList(a)


#To find the smallest element in the list

def minList(a):
    m=a[0]
    for i in a:
        if i<=m:
            m=i
    print("The smallest element in a list",m)

minList(a)