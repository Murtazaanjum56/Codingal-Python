word = str(input("Enter a word: "))
char = str(input("Enter a character to search for: "))
i = 0
count = 0
while i < len(word):
    if word[i] == char:
        count = count + 1
    i = i + 1


print("The total number of times that the character", char, "has occurred in word",
      word, "is", count)
