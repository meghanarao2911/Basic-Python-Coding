#program to search for the existence of an element in a llist using linear search

a=[10,20,30,40,50,12,23,98,1111,344]

def linearSearch(a,key):
    flag=0
    pos=0
    j=1
    for i in a:
        if i==key:
            flag=1
            pos=i
            break
        j=j+1
    if flag==1:
        print("Element",key,"present in the array at position",j)
    else:
        print("Element doesn't exist")


linearSearch(a,344)