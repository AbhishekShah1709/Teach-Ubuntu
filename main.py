from info import get_info
from challenges import get_challenge
from flags import get_flag

while 1:

    print("Enter the number corresponding to the commmand you want to test yourself on: ")
    print()
    print("*********************************************************")
    print("1: ls")
    print("2: cp")
    print("3: touch")
    print("4: grep")
    print("5: vim")
    print()
    print("Enter quit to EXIT")
    print("*********************************************************")

    usr_choice = input("Input your choice: ")

    if usr_choice=="1":

        get_info("ls")
        passed = get_challenge("ls")
    
        print(passed)
        if passed==1:
            get_flag("ls")

    if usr_choice=="quit":
        break


