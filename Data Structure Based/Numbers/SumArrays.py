def sumArray(a):
    s=0
    n=len(a)
    l=[]
    for i in range(0,n):
        for j in range(i,n):
            if a[j] %2 !=0:
                s=s+a[j]
                l.append(s)
                print(s)



a=[1,2,3,4]
sumArray(a)