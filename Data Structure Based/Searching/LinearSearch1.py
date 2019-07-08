a=[10,30,60,80,55]
key=35
def linearSearch(a,key):
    print("key=",key)
    flag=0
    for i in range(len(a)):
        if a[i]==key:
            print("Element ",key,"was found at ",(i+1),"position")
            flag=1
    if flag==0:
        print("Element Not Found")

linearSearch(a,key)
