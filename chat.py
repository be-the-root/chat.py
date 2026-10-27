RESET ="\033[0m"
CYAN = "\033[36m"
GREEN ="\033[32m"
YELLOW ="\033[33m"
RED ="\033[31m"
GREY = "\033[90m"
BOLD = "\033[1m"

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
print(GREEN + "i am your personal ai assistance (just without intelligence)" + RESET)
print()
print()
while True:
    
    name = input(YELLOW + BOLD + "enter your name plaese--" + RESET)
    print()
    answer =input("is your name correct?--" + name + " y - yes , n - retry--")

    if answer == "y".strip().lower:
        print("nice to meet you " + name)
        break
    else:
        print("lets try again")

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
    choice = input("please chose a option from above- eg- 1   ")
    if choice == "1":
        print("hello " + name + " !")
    elif choice == "2":
        print("joke!!!")
    elif choice == "3":
        print("hmmmm")
    else:
        print("chose a resonable option from above")



