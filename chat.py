print("""
_______________________________________________
|                                              |
|   ███  █   █  ███   █████     █████   █   █  |
|  █     █   █ █   █   █        █   █    █ █   |
|  █     █████ █████   █   ████ ████      █    |
|  █     █   █ █   █   █        █         █    |
|   ███  █   █ █   █   █        █         █    |
|_____________________________________________ |
""")
print("i am your personal ai assistance (just without intelligence)")
print()
print()
while True:
    
    name = input("enter your name plaese--")
    print()
    answer =input("is your name correct?--" + name + " y - yes , n - retry--")

    if answer == "y":
        print("nice to meet you " + name)
        break
    else:
        print("lets try again")

while True:
    print("""

--------------menu------------
1 - say hello (yes it does nothing else)

2 - tell me a joke !!!

3 - hmmm i dont know , just try
    """)        

    choice = input("please chose a option from above- eg- 1")
    if choice == "1":
        print("hello " + name + " !")
    elif choice == "2":
        print("joke!!!")
    elif choice == "3":
        print("hmmmm")
        break
    else:
        print("chose a resonable option from above")



