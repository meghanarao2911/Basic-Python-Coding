#Program to remove a character from a string
str="Meghana is a gaaaaad girl"
char='a'

def charRemove(str,ch):
    #print(str)
    #print(ch)
    charlist=" "
    for i in str:
        #print("i",i)
        if ch == i:
            continue
        else:
            charlist=charlist+i
    print(charlist)
    return charlist

c=charRemove(str,char)
print("Original string",str)
print("Modified String",c)