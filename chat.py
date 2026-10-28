import time 
import random
import string

RESET ="\033[0m"
CYAN = "\033[36m"
GREEN ="\033[32m"
YELLOW ="\033[33m"
RED ="\033[31m"
GREY = "\033[90m"
BOLD = "\033[1m"
# yes and no
def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print(RED + "please answer y or n" + RESET)
# password geneator
def generate_password():
    print()
    print(YELLOW + BOLD + "===========password forge ===========")


    while True:
        text = input("how long? (8-64)")
        if text.isdigit():
            length = int(text)
            if length >= 8 and length <= 64:
                break
            print(RED + "give a number between 8 and 64")


    use_lower  = ask_yes_no("include lowercase letters?")
    use_upper  = ask_yes_no("include uppercase letters?")
    use_digits  = ask_yes_no("include numbers?")
    use_symbols = ask_yes_no("include symbols??")

    pool = []
    required = []

    if use_lower:
        for ch in string.ascii_lowercase:
            pool.append(ch)
        required.append(random.choice(string.ascii_lowercase))

    if use_upper:
        for ch in string.digits:
            pool.append(ch)
        required.append(random.choice(string.digits))



    if use_digits:
        for ch in string.digits:
            pool.append(ch)
        required.append(random.choice(string.digits))


    if use_symbols:
        symbols = "!@#$%^&*(){};:,.?"
        for ch in symbols:
            pool.append(ch)
        required.append(random.choice(symbols))


    if len(pool) == 0:
        print(RED + BOLD +"you didnt picked any character types :( " + RESET)
        return



    chars = []

    for ch in required:
        chars.append(ch)

    while len(chars) < length:
        chars.append(random.choice(pool))

    random.shuffle(chars)

    pw = ""
    for ch in chars:
        pw = pw + ch

    print()
    print(GREEN + BOLD + "your password : " + RESET)
    print(CYAN + BOLD + "      " + pw + RESET)
    print()
# for typeing effect
def typeout(text, color=""):


    print(color, end="", flush=True)
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.04)
    print(RESET)
# for exit
def kill(name):
    answer2 = input("are you sure? (y/n)")
    if answer2 == "y":
        typeout("goodbye " + name + "!")
        return True

    else:
        typeout("okey staying")
        return False
# for space   
def space():
    print()
    print()
# quiz
def quiz():
    score = 0
    print(YELLOW + """


 ███  █   █ █████ ███  ███  █   █ █████     ███  █   █ ███ █████ 
█   █ ██  █   █    █  █   █ █   █ █        █   █ █   █  █     █  
█████ █ █ █   █    █  █   █ █   █ ████     █   █ █   █  █    █   
█   █ █  ██   █    █  █  █  █   █ █        █  █  █   █  █   █    
█   █ █   █   █   ███  ██ █  ███  █████     ██ █  ███  ███ █████ 
    
------------- answer all the questions coorectly--------------------    
    
    
    """ + RESET)
    typeout(YELLOW + BOLD + "just say the option" + RESET)



    # question 1
    typeout( GREEN + "ques1--- in which century was the victorian era?" + RESET)
    print("  a) 16th")
    print("  b) 17th")
    print("  c) 19th")
    print("  d) 20th")
    print()
    
    ans = input("your answer")
    if ans == "c":
        typeout( GREEN + BOLD +"correct" + RESET)
        score += 1
    else:
        typeout( RED + BOLD +"wrong answer , moving to the next question!" + RESET)
    print()
    print()

    # ques 2
    typeout(GREEN + BOLD + "ques2--- what is 'patina' on an antique?")
    print("   a) a type of wood")
    print("   b) the aged surface flim")
    print("   c) a brand name")
    print("   d) a kind of glue")
    ans = input("your answer--- ")
    if ans == "b":
        typeout(GREEN + BOLD + "correct" + RESET)
        score += 1
    else:
        typeout(RED + "wrong , moving to the next question" + RESET)
    print()
    print()


# question3
    typeout(GREEN + "  which wood is prized in antique furniture???" + RESET)
    print("  a) pine")
    print("  b) mahogany")
    print("  c) plywood")
    print("  d) bamboo")
    ans =  input("your answer:  ")
    if ans == "b":
        typeout("correct!!")
        score += 1
    else:
        typeout("wrong , moving to the next question")
    print()
    print()

    #question4
    typeout("what does 'provenance' mean for an antique?")
    print("  a) its price")
    print("  b) its color")
    print("  c) its documented owenship history")
    print("  d) its weight")
    ans == input("your answer --")
    if ans == "c":
        typeout("correct" ,GREEN)
        score += 1
    else:
        typeout("wrong , moving to the next question", RED)
    space()

    #ques5
    typeout("which era came just before victrorian?")
    print("  a) tudor")
    print("  b) georgian")
    print("  c) edwardian")
    print("  d) elizabethan")
    ans == input("your answer ---")
    if ans == "b":
        typeout("correct", GREEN , BOLD)
        score += 1
    else:
        typeout("wrong ")
    space()








    # score
    typeout("you scrored " + str(score) + "out of 3")
    space()
    if score == 5:
        typeout("parfect score")
    elif score == 4:
        typeout("almost perfect")
    elif score == 1:
        typeout("we will get better")
    else:
        typeout("wow dumbo")
# banner
print(RED + BOLD +  """
_______________________________________________
|                                              |
|   ███  █   █  ███   █████     █████   █   █  |
|  █     █   █ █   █   █        █   █    █ █   |
|  █     █████ █████   █   ████ ████      █    |
|  █     █   █ █   █   █        █         █    |
|   ███  █   █ █   █   █        █         █    |
|_____________________________________________ |
""" + RESET )
while True:
    print(GREEN + "i am your personal ai assistance (just without intelligence)" + RESET)
    print()
    print()
    break
# name question
while True:
    
    name = input(YELLOW + BOLD + "enter your name plaese--" + RESET)
    print()
    answer =input("is your name correct?--" + name + " y - yes , n - retry--")

    if answer == "y":
        typeout("nice to meet you " + name)
        break
    else:
        print("lets try again")
#c menu
def menu():
    print(GREEN + BOLD + """

------------------menu------------------
||  1 - say hello (yes it does nothing else)

||  2 - tell me a joke !!!

||  3 - hmmm i dont know , just try

||  4 - quit

||  5 - quiz

||  6 - password generator
    """ + RESET) 
# menu loop
while True:

    menu()
    choice = input(YELLOW + BOLD +"please chose a option from above- eg- 1   " + RESET)
    if choice == "1":
        print("hello " + name + " !")
    elif choice == "2":
        print("joke!!!")
    elif choice == "3":
        print("hmmmm")
    elif choice == "4":
        if kill(name):
            break
    elif choice == "5":
        quiz()

    elif choice == "6":
        generate_password()
        
        
    else:
        print()
        print(RED + BOLD + "chose a resonable option from above" + RESET)



