import re

word1 = 'SSssbbbQqr'

def duplicate_encode(word):
    #your code here
    letters = [letter for letter in word.lower()]
    numbers = [str(letters.count(letter)) for letter in letters]
    new_word = "".join(numbers)
    first = re.sub(r'[0,1]', '(', new_word)
    second = re.sub(r'[^(]', ')', first)
    return second

x1 = duplicate_encode(word1)
print(x1)
