import datetime
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

def notes_load():
    notes = []
    try:
        with open("notes.txt") as f:
            for line in f:
                line = line.strip()
                if line:
                    notes.append(line)
    except FileNotFoundError:
        pass
    return notes



def notes_save(notes):
    with open("notes.txt" , "w") as f:
        for note in notes:
            f.write(note + "\n")




def notes_parse(note):
    parts = note.split("|||")
    while len(parts) < 5:
        parts.append("")
    return parts

def notes_formet(title , body , tags , date , pinned):
    return title + "|||" + body + "|||" + tags + "|||" + date + pinned


def notes_word_count(body):
    count = 0
    for word in body.split():
        count = count + 1



    return count

def notes_menu():
    notes = notes_load()

    while True:
        print()
        print("____________the ledger__________")
        print("  "+ str(len(notes)) + " notes")
        print()
        print("  1 - add a note")
        print("  2 - list all")
        print("  3 - read a note")
        print("  4 - back")
        print()
        pick = input("  >> ").strip()




        if pick == "1":
            title = input("   title:").strip()
            body = input("   body:").strip()
            tags = input("   tags:").strip()
            if len(title) > 0 and len(body) > 0:
                today = str(datetime.date.today())
                new_note = notes_formet(title, body , tags, today, "0")
                notes.append(new_note)
                notes_save(notes)
                print("  saved")
            else:
                print(" need title and a body")

        elif pick == "2":
            if len(notes) == 0:
                print("   nothing here  yet")
            else:
                for i in range(len(notes)):
                    parts = notes_parse(notes[i])
                    mark = ""
                    if parts[4] == "1":
                        mark = " *"
                    print("  " + str(i + 1) + mark + "   " + parts [0])









        elif pick == "3":
            num = input("    number: ").strip()
            if not num.isdigit():
                print(" >>> type a number")
                continue
            n = int(num)
            if n < 1 or n > len(notes):
                print("    no such note")
                continue
            parts = notes_parse(notes[n - 1])
            print()
            print("    ---" + parts[0] + "----")
            if len(parts[3]) > 0:
                print("   date  : " + parts[3])
            if len(parts[2]) > 0:
                print("   tags : " + parts[2])
            print("    words : " + str(notes_word_count(parts[1])))
            print()
            print("   " + parts[1])

            print()
        elif pick == "4":
            break




                



# strenght checker
def check_strength(pw , lenght):
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in pw:
        if ch in string.ascii_lowercase:
            has_lower = True
        elif ch in string.ascii_uppercase:
            has_upper = True
        elif ch in string.digits:
            has_digit = True
        else:
            has_symbol = True

    types = 0
    if has_upper:
        types += 1
    if has_lower:
        types += 1
    if has_digit: 
        types += 1
    if has_symbol:
        types += 1



    score = types * 25
    if lenght >= 16:
        score += 10
    if score > 100:
        score = 100

    filled = score // 10
    bar = "" 
    for i in range(10):
        if i < filled:
            bar += "█"
        else:
            bar += "░"

    print("strength: " + bar + "  " + str(score) + "%")
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
        text = input("how long? (8-64)").strip()
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
        for ch in string.ascii_uppercase:
            pool.append(ch)
        required.append(random.choice(string.ascii_uppercase))



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

    check_strength(pw , length)
# for typeing effect
def typeout(text, color=""):


    print(color, end="", flush=True)
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.04)
    print(RESET)
# for exit
def kill(name):
    answer2 = input("are you sure? (y/n)").strip().lower()
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
    typeout( GREEN+ BOLD + "ques1--- in which century was the victorian era?" + RESET)
    print("  a) 16th")
    print("  b) 17th")
    print("  c) 19th")
    print("  d) 20th")
    print()
    
    ans = input(CYAN + BOLD + "your answer" + RESET ).strip().lower()
    if ans == "c":
        typeout( GREEN + BOLD +"correct" + RESET)
        score += 1
    else:
        typeout( RED + BOLD +"wrong answer , moving to the next question!" + RESET)
    print()
    print()

    # ques 2
    typeout(GREEN + BOLD + "ques2--- what is 'patina' on an antique?" +  RESET)
    print("   a) a type of wood")
    print("   b) the aged surface flim")
    print("   c) a brand name")
    print("   d) a kind of glue")
    ans = input(CYAN + BOLD + "your answer--- " + RESET ).strip().lower()
    if ans == "b":
        typeout(GREEN + BOLD + "correct" + RESET)
        score += 1
    else:
        typeout(RED + BOLD + "wrong , moving to the next question" + RESET)
    print()
    print()


# question3
    typeout(GREEN + BOLD + "  which wood is prized in antique furniture???" + RESET)
    print("  a) pine")
    print("  b) mahogany")
    print("  c) plywood")
    print("  d) bamboo")
    ans =  input(CYAN + BOLD + "your answer:  " + RESET ).strip().lower()
    if ans == "b":
        typeout("correct!!")
        score += 1
    else:
        typeout(RED + BOLD + "wrong , moving to the next question" + RESET)
    print()
    print()

    #question4
    typeout(GREEN + BOLD + "what does 'provenance' mean for an antique?" + RESET)
    print("  a) its price")
    print("  b) its color")
    print("  c) its documented owenship history")
    print("  d) its weight")
    ans = input(CYAN + BOLD + "your answer --" + RESET).strip().lower()
    if ans == "c":
        typeout(GREEN + BOLD + "correct" + RESET)
        score += 1
    else:
        typeout(RED + BOLD + "wrong , moving to the next question" + RESET)
    space()

    #ques5
    typeout(GREEN + BOLD + "which era came just before victrorian?" + RESET)
    print("  a) tudor")
    print("  b) georgian")
    print("  c) edwardian")
    print("  d) elizabethan")
    ans = input(CYAN + BOLD + "your answer ---" + RESET ).strip().lower()
    if ans == "b":
        typeout("correct", GREEN + BOLD)
        score += 1
    else:
        typeout(RED + BOLD +"wrong " + RESET)
    space()








    # score
    typeout(GREEN + BOLD + "you scrored " + str(score) + "out of 5" + RESET)
    space()


    if score == 5:
        typeout(RED + BOLD + "parfect score" + RESET )
    elif score == 4:
        typeout(RED + BOLD + "almost perfect" + RESET)
    elif score == 3:
        typeout(RED + BOLD  +"good" + RESET)
    elif score == 2:
        typeout(RED + BOLD + "not bad" + RESET )
    elif score == 1:
        typeout(RED + BOLD + "we will get better" + RESET)
    else:
        typeout(RED + BOLD + "wow dumbo" + RESET )
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
    
    name = input(CYAN + BOLD + "enter your name plaese--" + RESET)
    print()
    answer =input( RED + BOLD + "is your name correct?--" + name + "(y/n) >>" + RESET)

    if answer == "y":
        typeout(CYAN + BOLD  + "nice to meet you " + name + RESET )
        break
    else:
        print("lets try again")
#c menu
def menu():
    print(CYAN + BOLD + """

------------------menu------------------
||  1 - say hello (yes it does nothing else)

||  2 - tell me a joke !!!

||  3 - hmmm i dont know , just try

||  4 - password generator

||  5 - quiz

||  6 - the ledger

||  7 - quit
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
        generate_password()
    elif choice == "5":
        quiz()
    elif choice == "6":
        notes_menu()

    elif choice == "7":
        if kill(name):
            break
        
        
    else:
        print()
        print(RED + BOLD + "chose a resonable option from above" + RESET)



