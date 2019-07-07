#Number of perfect squares between a range
import math
def perfectSqaure(m,n):
    print("Inside sqrt")
    lists=[]
    print(m,n)
    for i in range(m,n+1):
        j=1
        while(j*j<=i):
            if j*j==i:
                lists.append(i)
            j=j+1
        i=i+1
    return lists


l=perfectSqaure(6,25)
print(l)