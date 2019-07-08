a=[10,20,3,480,50,6,70,45]


def selectionsort(a):
    for i in range(len(a)-1):
        for j in range((i+1),len(a)):
            if a[j]<a[i]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    print(a)

selectionsort(a)