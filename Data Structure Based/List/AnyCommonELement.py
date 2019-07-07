a=[10,20,30,40,50]
b=[10,20,80,60,70,80,90]

def anycommon(a,b):
    l=[]
    for i in a:
        if i in b:
            return True
    return False

ans=anycommon(a,b)

if(ans==True):
    print("The list has common elements")
else:
    print("No common element")