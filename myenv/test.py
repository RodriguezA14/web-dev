import random
words = open('myenv/words.txt').read().split()
word = random.choice(words).upper()
correct_guesses = 0
wrong_letters = ""
num_guesses = len(word)*2
print(word)
dashes = " - " * len(word)
secret_letters = word.split()
list(secret_letters)
print(list)