#program to check if all the elements in the list are same or not

a=[10,20,10,10,10,10]

def sameorno(a):
    flag=1
    item=a[0]
    for i in a:
        if item!=i:
            flag=0
            break
    if flag==1:
        print("All the elements are same")
    else:
        print("They are different")


sameorno(a)