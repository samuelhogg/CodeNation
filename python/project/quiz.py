from hangman import HANGMANPICS
import sys
import time
import random
# -------------------------
yes = ["Y", "y", "yes","Yes"]                           #limiting the response for the user
no = ["N", "n", "no","No"]
letters = ["A", "B", "C", "D"]
words = ["codenation", "programmer", "javascript"]      #list of words for the anagram at the end

#------------------------------

questions = {
"Who created Python?: ": "A",
"What year was Python created?: ": "B",
"Python is tributed to which comedy group?: ": "C",
"""What is missing from the code to print out fanta? favourite_drinks = ["coke", "fanta", "tonic", "lemonade"]""": "D",    #list of questions showing the correct answer at the end
"What is missing from the code to print down from 11 to 1?": "A",
"How many data types are there in Python?": "C",
"Which of the following games use Python?": "D",
"What is the output of print('[%c]' % 65)?": "B",
"What is the data type of print(type(0xFF))": "A",
"What is the output of the following code? print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))": "D",
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. print(favourite_drinks[3])","B. print(favourite_drinks[0])", "C. print(favourite_drinks[2])", "D. print(favourite_drinks[1])"], #multiple choice answers
    ["A. for i in range(11,1,-1:)","B. for i in range(11,1,1:) ", "C. for i in range(11,1,0:)","D. for i in range(11,1,-2:)"],
    ["A. 3", "B. 4", "C. 5", "D. 6"],
    ["A. Eve Online", "B. The Sims 4", "C. Battlefield 2", "D. All of the above"],
    ["A. 65", "B. [A]", "C. A", "D. Syntax Error"],
    ["A. int", "B. hex", "C. hexint", "D. number"],
    ["A. False True False True", "B. True True False True", "C. True False True False", "D. False True True True"],
    ]

#-------------------------------

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)             #slowprint the simulate someone typing out the questions
        sys.stdout.flush()
        time.sleep(1./30)

def change_word():
    global wordconundrum
    global word    
    random.shuffle(words)                #function the rotate and shuffle the anagram ending
    word = words[0]
    charlst = list(word) 
    random.shuffle(charlst)
    wordconundrum = "".join(charlst)

i = 0
c = 0

def intro():
    change_word()
    print("""

 █████   █████   █████████   ██████   █████   █████████  ██████   ██████   █████████   ██████   █████
░░███   ░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░██████ ██████   ███░░░░░███ ░░██████ ░░███ 
 ░███    ░███  ░███    ░███  ░███░███ ░███  ███     ░░░  ░███░█████░███  ░███    ░███  ░███░███ ░███ 
 ░███████████  ░███████████  ░███░░███░███ ░███          ░███░░███ ░███  ░███████████  ░███░░███░███ 
 ░███░░░░░███  ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███ ░░░  ░███  ░███░░░░░███  ░███ ░░██████ 
 ░███    ░███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███      ░███  ░███    ░███  ░███  ░░█████ 
 █████   █████ █████   █████ █████  ░░█████ ░░█████████  █████     █████ █████   █████ █████  ░░█████
░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░ 
____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ 
||P |||Y |||T |||H |||O |||N |||       |||C |||O |||D |||E |||R |||       |||S |||T |||Y |||L |||E ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_y_\|/_______\|/__\|/__\|/__\|/__\|/__\|              

by the Red Team""")

    slowprint("""
    Your coding tutor has been captured and it's your job to save them.
    You will have to answer questions, for every correct answer you will get a letter from a secret word.
    For every wrong answer your tutor will be one step closer to coding heaven.
    Once all questions have been answered you will have 3 chances to solve the secret word to save your teacher.

    Do you accept the challenge? Y/N""")
    
    choice = input(">>>")
    if choice in yes:
        print("ok here we go")
        new_game()
    else:
        exit()

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    change_word()

    for key in questions:
        print("___________________________________________________________________________________________________________________________________")
        slowprint(key)
        
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        while guess not in letters:
            guess = input("Please only enter (A, B, C, or D): ")   #this will limit the users input to only A,B,C or D
            guess = guess.upper()

        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    guess_word()    
    # display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):
    global c
    global i
    
    if answer != guess:
        i = i + 1               
        if i == 6:
            print(HANGMANPICS[i])
            print("""You have made 6 mistakes therefore you will not get chance to get to guess the secret word, so your teacher will now hang!

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   """)
            play_again() 
        else:
            print(HANGMANPICS[i])
            print("WRONG!")
            print(wordconundrum[0:c] + ((len(wordconundrum) - c) * "-"))
            return 0
           
    else:
        c = c + 1
        print(HANGMANPICS[i])
        print("CORRECT!\n")
        print(wordconundrum[0:c] + ((len(wordconundrum) - c) * "-"))
        return 1
    



def guess_word():
    slowprint ("""
    Ready to guess the word to save your teacher? 
    
    You have 3 guesses. 
    
    Clue: You have probably guessed by now but the letters are conundrum for the real secret word!
    
    """)
    count = 0
    while count < 3:
        guess = str(input("Please enter your guess:"))
        count += 1
        if guess != word:
            print("Wrong, have another go")
        if guess != word and count == 3:
            print("""You have guessed the secret word incorrrectly 3 times , so your teacher will now hang!

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   """)
            play_again()
        if guess == word:
            print("""You have have guessed the secret word correctly and your teacher will now be released.

 $$$$$$\                                                    $$\               $$\            $$\     $$\                               
$$  __$$\                                                   $$ |              $$ |           $$ |    \__|                              
$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\   $$\   $$\ $$ | $$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$$\ 
$$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \____$$\\_$$  _|  $$ |  $$ |$$ | \____$$\\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|
$$ |      $$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$$$$$$ | $$ |    $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\  
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
\$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |     \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
 \______/  \______/ \__|  \__| \____$$ |\__|      \_______|  \____/  \______/ \__| \_______|  \____/ \__| \______/ \__|  \__|\_______/ 
                              $$\   $$ |                                                                                               
                              \$$$$$$  |                                                                                               
                               \______/                                                                                                


""")
            play_again()
            break


# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
    
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()

#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")

#-------------------------
def play_again():

    response = input("Do you want to play again? (yes or no):")
    #response = response.upper()

    if response in yes:
        global i
        global c
        i = 0
        c = 0
        new_game()
    else:
        print("Byeeeeee!")
        exit()
# -------------------------

intro() 

while play_again():
    intro()

print("Byeeeeee!")

# -------------------------