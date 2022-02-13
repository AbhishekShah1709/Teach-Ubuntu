from general import execute_cmd
from first_hint import get_first_hint
from second_hint import get_second_hint
from third_hint import get_third_hint
from flags import get_flag

def print_challenge(cmd):

    if cmd=="ls":
        print("CHALLENGE: Print all the files and directories in the current directory excluding hidden files and folders. The total number of files and folders is the flag!")
    
    elif cmd=="cp":
        print("CHALLENGE: Make a copy of a.txt and name it as a_dup.txt")
    
    elif cmd=="diff":
        print("CHALLENGE: Check if the content of a.txt and b.txt differs. The number of lines that differ is the flag!")
    
    elif cmd=="grep":
        print("CHALLENGE: Print the lines which contain the word Hello (Case sensitive) in c.txt. The number of lines containing the word Hello in c.txt is the flag!")
    
    elif cmd=="wc":
        print("CHALLENGE: Get number of character, number of words and number of lines for a.txt. The sum of these 3 is the flag!")
    
    elif cmd=="chmod":
        print("CHALLENGE: Give read permission only to the owner for the file d.txt. The first word of this file is the flag!")
    
    elif cmd=="piping":
        print("CHALLENGE: Print only top 3 lines from b.txt. The total number of words in those 3 lines is the flag!")
    
    elif cmd=="redirect":
        print("CHALLENGE: Create a new file named hidden.txt with all the hidden files and folder in the current directory. The number of lines in hidden.txt is the flag!")
    
    elif cmd=="uname":
        print("CHALLENGE: Get the network host nodename and the kernel name for your system and submit that as the flag!")
    
    elif cmd=="md5sum":
        print("CHALLENGE: Check if the fingerprints for all python files match with the ones given in fingerprints1.txt. The number of files for which the fingerprints differ is the flag!")
    
    elif cmd=="sha256sum":
        print("CHALLENGE: Check if the fingerprints for all python files match with the ones given in fingerprints2.txt. The number of files for which the fingerprints differ is the flag!")
    
    elif cmd=="uid":
        print("CHALLENGE: Get a list of all group ID associated with the user. The sum of all those ID's is the flag!")
    
    elif cmd=="gzip":
        print("CHALLENGE: Uncompress message.zip file and find the flag inside one of the three files.")
    
    elif cmd=="zgrep":
        print("CHALLENGE: Find the word 'world' inside compress.zip file. The number of occurences of 'world' inside this file is the flag!")
    
    elif cmd=="ln":
        print("CHALLENGE: Create hardlink for the file ln.py and name it as ln1.py. Run either of the file to get the flag!")
    
    elif cmd=="chattr":
        print("CHALLENGE: Change the mode of e.txt file to append only mode. The new attributes of this file is the flag!")
    
    elif cmd=="ifconfig":
        print("CHALLENGE: Display a short list of interfaces available. The number of interfaces in the list displayed is the flag!")

def get_challenge(cmd):

    print_challenge(cmd)
    hint_cnt = 0
    
    print()
    while True:
        usr_input = input("-> ")
        if usr_input.split(" ")[0]=="hintme":
            hint_cnt += 1
            if hint_cnt==1:
                get_first_hint(cmd)
            elif hint_cnt==2:
                get_second_hint(cmd)
            elif hint_cnt==3:
                get_third_hint(cmd)
            else:
                print("No more hints allowed!")

        elif usr_input.split(" ")[0]=="submit":
            usr_flag = usr_input.split(" ")[1]
            corr_flag = get_flag(cmd)

            if usr_flag.strip()==corr_flag.strip():
                print()
                print("CONGRATULATIONS! YOU HAVE MASTERED THIS COMMAND")
                print()
                break
            else:
                print()
                print("TRY AGAIN!")
                print()
        else:
            execute_cmd(cmd, usr_input)

    return
