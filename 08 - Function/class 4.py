
word= "rar"


def palindrome(word):
    l= len(word)
    newWord=""
    for i in range(l):
        print(word[l-i-1])
        newWord+=word[l-i-1]
    return newWord
w=palindrome(word)

if w==word:
    print(f"{w} == {word}")
else:
    print("No lo son")

'''



'''

def check_palindrome(word):
    l=len(word)
    for i in range(l):
        if word[i]!=word[l-1-i]:
            return False
    return True

print(check_palindrome("madam"))