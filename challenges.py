from first_hint import get_first_hint
from second_hint import get_second_hint
from third_hint import get_third_hint
from flags import get_flag

def print_challenge(cmd):

    if cmd=="ls":
        print("CHALLENGE: Print all the files and directories in the current directory excluding hidden files and folders. The total number of files and folders is the flag!")
    
    elif cmd=="cp":
        print("CHALLENGE: Make a copy of a.txt and name it as a_dup.txt. The flag is the number of words in dup.txt")
    
    elif cmd=="diff":
        print("CHALLENGE: Check if the content of a.txt and b.txt differs. The number of lines that differ is the flag!")
    
    elif cmd=="grep":
        print("CHALLENGE: Print the lines which contain the word Hello (Case sensitive) in c.txt. The number of lines containing the word Hello in c.txt is the flag!")
    
    elif cmd=="wc":
        print("CHALLENGE: Get number of character, number of words and number of lines for a.txt. The sum of these 3 is the flag!")
    
    elif cmd=="chmod":
        print("CHALLENGE: Give read permission only to the owner for the file d.txt. The content of this file is the flag!")
    
    elif cmd=="piping":
        print("CHALLENGE: Print only top 3 lines from b.txt. The total number of words in those 3 lines is the flag!")
    
    elif cmd=="redirect":
        print("CHALLENGE: Create a new file named all.txt with all the visible files and folder in the current directory. The number of lines in all.txt is the flag!")
    
    elif cmd=="uname":
        print("CHALLENGE: Get the network host nodename and the kernel name for your system and submit that as the flag!")
    
    elif cmd=="md5sum":
        print("CHALLENGE: Check if the md5 fingerprints for all python files match with the ones given in fingerprints1.txt. The number of files for which the fingerprints differ is the flag!")
    
    elif cmd=="sha256sum":
        print("CHALLENGE: Check if the sha256 fingerprints for all python files match with the ones given in fingerprints2.txt. The number of files for which the fingerprints differ is the flag!")
    
    elif cmd=="uid":
        print("CHALLENGE: Get a list of all group ID associated with the user. The sum of all those ID's is the flag!")
    
    elif cmd=="gzip":
        print("CHALLENGE: Uncompress message.gz file and find the flag inside the file.")
    
    elif cmd=="zgrep":
        print("CHALLENGE: Find the word 'world' inside compress.zip file without uncompressing it. The number of occurences of 'world' (Case sensitive) inside this file is the flag!")
    
    elif cmd=="ln":
        print("CHALLENGE: Create hardlink for the file ln.py and name it as ln1.py. Run either of the file to get the flag!")
    
    elif cmd=="chattr":
        print("CHALLENGE: Change the mode of e.txt file to append only mode. The new attributes of this file is the flag!")
    
    elif cmd=="ifconfig":
        print("CHALLENGE: Display a short list of interfaces available. The number of interfaces in the list displayed is the flag!")

    elif cmd=="rm":
        print("CHALLENGE: Check number of files inside the 'delete' folder and then remove that folder. The number of files inside that folder is the flag! Be sure to check the number of files before removing the folder because once the folder is removed, all files inside it will be deleted.")

    elif cmd=="mv":
        print("CHALLENGE: Rename 'this.txt' to 'that.txt' and open the renamed file and count the occurences of __FLAG__ in this file and use that as the flag.")

    elif cmd=="pwd":
        print("CHALLENGE: Get the absolute path for the current directory you are in and use it as the flag!")

    elif cmd=="tail":
        print("CHALLENGE: Get the last 50 lines of the file count.txt and count the occurence of the word __FLAG__ in it. The value is the flag!")

    elif cmd=="whoami":
        print("CHALLENGE: Print the user name associated with the current effective user ID and use it as a flag!")

    elif cmd=="man":
        print("CHALLENGE: Print the man page of the man command and use the first sentence of it's description as the flag (do not include fullstop)!")
    
    elif cmd=="nano":
        print("CHALLENGE: Delete the last line of the file 'new.txt' and count the total number of characters after this and use it as a flag!")
    
    elif cmd=="sudo":
        print("CHALLENGE: Open the file permission.txt. Read the content of the file to get the flag!")
    
    return
