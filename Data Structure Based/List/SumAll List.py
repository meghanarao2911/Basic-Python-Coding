
a=[1,20,3,4,5,6,7,8]

def sumall(a):

    sum=0
    for i in a:
        #print(i)
        sum=sum+i
    return sum

a=sumall(a)
print("Sum of all elements is",a)