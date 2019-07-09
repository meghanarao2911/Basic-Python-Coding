str="the quick brown fox jumps over a lazy dog"

import string
def pangramCheck(str):
    alphabets= "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabets:
        if ch not in str.lower():
          return False
    return True


a=pangramCheck(str)
if a ==True:
    print("String is pangram")
else:
    print("String is not pangram")