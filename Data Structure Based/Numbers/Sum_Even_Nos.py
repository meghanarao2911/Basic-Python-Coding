#Sum of all odd numbers in an array

def sumOfOdds(a):
    n=len(a)
    #print("Length of array",n)
    curr=1
    s=0
    j=0
    l=[]
    for i in range(0,n):
        if a[i]%2!=0:
            l.append(a[i])
    print(l)
    m=len(l)
    #print("Length of odd array",m)
    while j!=m:
        print(a[j])
        s=s+a[j]
        print("Sum= ",s)
        j=j+1



print(sumOfOdds([1,2,3]))