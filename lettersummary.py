
word = input('Please enter a word: ')

letterSummary = {}

for letter in word:
    keys = letterSummary.keys()
    if letter in keys:
        letterSummary[letter] += 1
    else:
        letterSummary[letter] = 1
print(letterSummary)
    