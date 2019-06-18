#program to print all substring

def substring(str):
    n=len(str)
    j=0
    sublist=[]
    i=0
    for k in str:
        sublist.append(k[i:j])
        j=j+1
    return sublist

str="abc"
sList=substring(str)
print("All substrings",sList)

