word = "python"
print(word)
print(word, id(str))
print("*" * 50)
wordx = word + ' 3'
print(word)
print(word[0])
print(word, id(wordx))
# word[0] = "X" # error
