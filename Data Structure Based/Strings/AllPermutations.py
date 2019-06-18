#Program to generate all possible permutations of a string

def generatePermutation(str):

    ch=""
    if len(str)==0:
        return " "
    elif len(str==1):
        return str
    else:
        for i in len(str):
            ch=str[i]

            ros=str[0:i]+str[i:]
            print(ros)
    generatePermutation(ros,)
