from general import take_cmd
from first_hint import get_first_hint
from second_hint import get_second_hint
from third_hint import get_third_hint

def print_challenge(cmd):

    if cmd=="ls":
        print("Print all the files and directories in the current directory")
    elif cmd=="cp":
        print("Make a copy of a.txt and name it as a_dup.txt")
    elif cmd=="diff":
        print("Check if the content of a.txt and b.txt differs. The number of lines that differ is the flag!")
    elif cmd=="grep":
        print("Print the lines which contain the word Hello (Case sensitive) in c.txt. The number of lines containing the word Hello in c.txt is the flag!")
    elif cmd=="wc":
        print("Get number of character, number of words and number of lines for a.txt. The sum of these 3 is the flag!")
    elif cmd=="chmod":
        print("Give read permission for the file d.txt only for user mode. The first word of this file is the flag!")
    elif cmd=="vim":
        print("")
    elif cmd=="gedit":
        print("")
    elif cmd=="piping":
        print("")
    elif cmd=="redirect":
        print("")

def get_user_choice(val):

    if val<=3:
        print()
        print("*********************************************************")
        print("1: Enter challenge command")
        print("2: Get HINT-"+str(val))
        print()

        usr_hint_choice = input("Enter your choice: ")
        print("*********************************************************")
        print()


    return val, usr_hint_choice

def option(val, hint_val, cmd): 
    if hint_val=="1":
        passed = take_cmd(cmd)

    elif hint_val=="2":
        if val==1:
            get_first_hint(cmd)
            print()
            val, hint_val = get_user_choice(2)
            passed = option(val, hint_val, cmd)
        elif val==2:
            get_second_hint(cmd)
            print()
            val, hint_val = get_user_choice(3)
            passed = option(val, hint_val, cmd)
        elif val==3:
            get_third_hint(cmd)
            print()
            print("Type the command in HINT-3 to pass the challenge")
            passed = take_cmd(cmd)

    return passed

def get_challenge(cmd):

    print_challenge(cmd)
    val, hint_val = get_user_choice(1)
    passed = option(val, hint_val, cmd)

    return passed
