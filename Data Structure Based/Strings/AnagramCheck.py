#proogram to check if the strings are anagrams of each other

str1="FEEL"
str2="EF"

s1=[]
s2=[]

def anagramCheck(str1,str2):
    flag=0
    m=len(str1)
    n=len(str2)

    if m!=n:
        flag=0
    else:
        str1=str1.lower()
        str2=str2.lower()

        s1=list(str1)
        s2=list(str2)

        s1.sort()
        s2.sort()
        if s1==s2 :
            flag=1
        else:
            flag=0
    return flag

anagramFlag=anagramCheck(str1,str2)
if anagramFlag :
    print("The strings are anagrams of each other")
else:
    print("They are not anagrams of each other")

