a=[10,20,30,40,50,60,70,70,90]
key=73

def sortedLinearSearch(a,key):
    flag=0
    for i in range(len(a)):
        if a[i]>key:
            print("Search ends here")
            break
        if a[i]==key:
            print("Element",a[i],"found at",(i+1),"position")
            flag=1

    if flag==0:
        print("Element not present in the list")


sortedLinearSearch(a,key)