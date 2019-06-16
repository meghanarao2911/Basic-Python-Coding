a=1332

def reverse(n):
    print(n)
    rev=0
    while n!=0:
        d=n%10
        #print(d)
        rev = rev * 10 + d
        #print(rev)
        n=n//10
    return rev

re=reverse(a)
print("Reverse of",a,"is",re)

if re==a:
    print("The number is pallindrome")
else:
    print("They are not pallindrome")