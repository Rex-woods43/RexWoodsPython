def Hello_world():
    print("Hello World")
def Goodbye_World():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
def Goodbye_Person():
    print("Hello")
    name = input("What is your name ? ")
    print("Goodbye",name)
def Good_Teacher():
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(name,"is an ok teacher")   
def For_Loop():
    for number in range(1,500):
        print(number)
def While_Loop():
    subject = input("What is the name of this subject ")
    while subject != "IST":
        print ("Not Correct - try again")
        subject = input("What is the name of this subject ")
    if subject == "IST": 
        print("\n\n Congratulations!!\n\n")
def Menu():
    import os
    os.system('cls')
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Rex Woods                            |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("\n1. Hello World ")
    print("2. Goodbye World ")
    print("3. Goodbye Person ")
    print("4. Good Teacher ")
    print("5. forLoop ")
    print("6. whileLoop ")
    print("7. string Loop ")
    print("8. Convert to ascii ")
    print("9. Encode a string ")
    print("x. To Exit ")
    selection = input("Enter an option ")
    print("\n----Start of Output ---------------------------\n")
    if selection == "1":
        Hello_world()
    elif selection == "2":
        Goodbye_World()
    elif selection == "3":
        Goodbye_Person()
    elif selection == "4":
        Good_Teacher()
    elif selection == "5":
        For_Loop()
    elif selection == "6":
        While_Loop()
    elif selection == "x":
        pass
    else:
        print("invalid option")
    print("\n----End of Output -----------------------------\n\n\n")
    if selection == "x":
        input("Press Enter to continue ")
    else:
        input("Press Enter to continue ")
        return Menu()
Menu()
