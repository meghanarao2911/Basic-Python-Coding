a=[90,80,70,60,50,40,30,20,10]

def bubbleSort(a):
    n=len(a)
    temp=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(a)

bubbleSort(a)