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
print("i am your personal ai assistance (just without intellegence)")

while True:
    
    name = input("enter your name plaese--")
    answer =input("is your name correct?--" + name + "y - yes , n - retry")

    if answer == "y":
        print("nice to meet you " + name)
        break
    else:
        print("lets try again")



