#Reversin using map

word="abcdefghijklmno"

print(word[::-1])

#[start:end:step]


words=["Python","Java","Javascript","C++"]


reversed_words= list(map(lambda word: word[::-1],words))

print(reversed_words)
