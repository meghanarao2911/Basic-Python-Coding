#Program to search a list using binary search

a=[10,20,30,40,50,60,70,80,90,100]

def binarySearch(a,key):
    flag=0
    low=0
    high=len(a)
    mid=(low+high)//2
    pos=0
    if key==a[mid]:
        flag=1
    elif key<a[mid]:
        low=0
        high=mid-1
        for i in range(low,mid):
            if a[i]==key:
                flag=1
                pos=i
                break
    else:
        low=mid+1
        for i in range(low,mid):
            if(a[i]==key):
                flag=1
                pos=i
                break
    if flag==1:
        print("Element",key,"present in the list at position",(pos+1))
    else:
        print("Element not present in the list")


binarySearch(a,60)
