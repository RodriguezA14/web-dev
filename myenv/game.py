import random
def play_game():
    words = open('myenv/words.txt').read().split()
    word = random.choice(words).upper()
    correct_guesses = 0
    wrong_letters = ""
    num_guesses = len(word)*2
    print(word)
    word_letters = list(word)
    print(word_letters)
    dashes = len(word)
    
    while num_guesses > 0 and correct_guesses < len(word):
        print("Word:", " - " * dashes)
        print("Guesses left:", num_guesses)
        print("Incorrect letters:", wrong_letters)
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("You're only supposed to guess a single letter!")
            
        elif guess.upper().isalpha() == False:
            print("You're only supposed to guess a single letter!")

        elif guess.upper() in wrong_letters:
            print("You can't guess the same letter twice!")
            
        elif guess.upper() in word:
            print("Correct!")
            correct_guesses += 1
            
        elif guess.upper() not in word:
            print("Incorrect!")
            num_guesses -= 1
            if wrong_letters == "":
                wrong_letters = guess.upper()
                
            else:
                wrong_letters += ", " + guess.upper()
                
    if num_guesses <= 0:
        print("Too bad! The word was", word)
        
    else:
        print("Nice job! The word was", word)
            
            
            
print("""
Welcome to Hangman.
Would you like me to explain the rules?""")
    
hear_rules = input("Yes or No: ")
    
if "Yes".lower() in hear_rules:
    print(""" We're going to play a game of Hangman.
    I'll think up a word, and you have a limited
    number of guesses to figure out what it is.
    The number of guesses you have is proportional
    to the difficulty of the word. If you run out of
    guesses and the word isn't filled out, you lose.
    Make sure your guess is a capital letter.
    Good luck and have fun!""")
    
    play_game()
    
else:
    if "No".lower() in hear_rules:
        
        play_game()