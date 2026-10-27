import time 

RESET ="\033[0m"
CYAN = "\033[36m"
GREEN ="\033[32m"
YELLOW ="\033[33m"
RED ="\033[31m"
GREY = "\033[90m"
BOLD = "\033[1m"


def typeout(text):
    for letter in text:
        print(letter, end="" , flush=True)
        time.sleep(0.08)
    print()


def kill(name):
    answer2 = input("are you sure? (y/n)")
    if answer2 == "y":
        typeout("goodbye " + name + "!")
        return True

    else:
        typeout("okey staying")
        return False


    
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
    """ + RESET) 



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
        
        
    else:
        print()
        print(RED + BOLD + "chose a resonable option from above" + RESET)

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


# question 1
    typeout( GREEN + "ques1--- in which century was the victorian era?" + RESET)
    print("  a) 16th")
    print("  b) 17th")
    print("  c) 19th")
    print("  d) 20th")
    print()
    typeout(YELLOW + BOLD + "just say the option" + RESET)
    ans = input("your answer")
    if ans == "c":
        typeout("correct")
        score += 1
    else:
        typeout( RED + BOLD +"wrong answer , moving to the next question!" + RESET)
    print()
    print()

    # ques 2
    typeout(GREEN + "ques2--- what is 'patina' on an antique?")
    print("   a) a type of wood")
    print("   b) the aged surface flim")
    print("   c) a brand name")
    print("   d) a kind of glue")
    if ans == "b":
        typeout("correct")
        score += 1
    else:
        typeout(RED + "wrong , moving to the next question" + RESET)
    print()
    print()


