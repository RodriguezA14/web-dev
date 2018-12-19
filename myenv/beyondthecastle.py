def riddle_room():
 print(""" Once you enter the room, you look around.
 It looks a lot like a forest, tall trees and various plants galore.
 You notice a troll napping on a tree stump in the middle of the room. 
 The door behind you slams shut and the troll wakes up.
 What do you do?""")
 
def reset_riddle_room():
    print("You're in the room of riddles. What now?")
    choice = input(" >")

riddle_room()

first_riddle_right = False
second_riddle_right = False

def first_riddle():
    print(""" "Let's begin! I have no mouth, but I still consume. Feed me well, and I will be strong. Get me to drink water, and I die.
    What am I?" """)
    choice = input(" >")
    if "fire" in choice:
        first_riddle_right = True
        print(""" "That's right, I'm fire! Talk to me when you want to try the next one. It won't be nearly as easy." """)
        reset_riddle_room()
    else:
        while first_riddle_right == False:
                print("Nope, try again! You can quit the game if you want to think on it.")
                choice = input(" >")
                if "quit" in choice:
                    print("Talk to me if you want to try again!")
                    reset_riddle_room()
                    
def second_riddle():
    print(""" "You just received word that the princess is dead! In her room there's broken glass on the floor and a puddle of water. 
    Her window is open, and it's storming outside. The nightstand by her window is knocked over as well. If nobody was present when the princess
    died, then how did she die?" """)
    choice = input(" >")
    if "princess" in choice and "was" in choice and "fish" in choice:
        second_riddle_right = True
        print(""" "That's correct! The princess died because she was a fish! The wind from the storm broke her window
        and knocked down her nightstand, so her fish bowl broke and she suffocated as a result." *The door ahead opens*
        "Good luck in the next room!" """)
        reset_riddle_room()
    else:
            while second_riddle_right == False:
                print("Nope, try again!")
                choice = input(" >")
                if "quit" in choice:
                    print("Talk to me if you want to try again!")
                    reset_riddle_room()
                    
            
choice = input(" >")
if "talk" in choice and "troll" in choice:
    print(""" "Welcome to my room of riddles!", says the troll. "I'll get straight to the point. I'm going to ask you
    a series of riddles. If you answer the first one correctly, I'll open the door from which you came.
    If you answer the second, I'll open the door that leads to the next room. If you feel you're not up to the task, 
    I might kill you right here! What do you say? Would you like to play?" """)
    
    choice = input(" >")
    if choice == "Yes":
        first_riddle()
    elif choice != "Yes" and choice == "No":
        dead("The troll snaps his fingers, and you keel over in pain. Your last words were \" I don't feel so good\"")
    elif choice != "Yes" and choice != "No":
        while choice != "Yes" and choice != "No":
            print("It's a simple Yes or No answer!")
            choice = input(" >")
            
else:
    while "leave" in choice or "go south" in choice and first_riddle_right == False:
        print("You can't, the door is shut.")
        choice = input(" >")
        reset_riddle_room()
        
if "leave" not in choice and "go south" not in choice and "go north" not in choice and "talk" not in choice and "troll" not in choice and "Yes" not in choice and "No" not in choice:
    print("The troll looks very excited to see you. Maybe you should go and talk to him?")
    choice = input(" >")
    reset_riddle_room()