#to print factorial of a number

def factorial(num):

    i=1
    f=1
    while i<=num:
        f=f*i
        i=i+1
    return f
n=6
f=factorial(n)
print("The factorial of",n,"is",f)