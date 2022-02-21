def get_first_hint(cmd):

    if cmd=="ls":
        print("List all files and count it")
    elif cmd=="cp":
        print("Copy exact content of one file to another using some terminal command")
    elif cmd=="diff":
        print("Try to think of a command which could help you compare the content of two files")
    elif cmd=="grep":
        print("Try to think of a command which could help you find a word inside a file")
    elif cmd=="wc":
        print("Get the count statistics of the given file and find the sum")
    elif cmd=="chmod":
        print("The permission for a file or a folder in a Unix-like operating system is represented by ---------- (10 '-'). Try to learn what each - represents.")
    elif cmd=="piping":
        print("You need to send the output of one command as an input to another command. Think what can be used!")
    elif cmd=="redirect":
        print("You need to divert the output of a command to a file. Think what can be used!")
    elif cmd=="uname":
        print("Try to think of a command which could get such information about your system.")
    elif cmd=="md5sum":
        print("Try to get md5 fingerprints for each file in fingerprints1.txt")
    elif cmd=="sha256sum":
        print("Try to get sha256 fingerprints for each file in fingerprints2.txt")
    elif cmd=="uid":
        print("First try to get both user and group IDs and then use a flag to filter out only group IDs")
    elif cmd=="gzip":
        print("Try to think of a command which could unzip a .gz file through terminal")
    elif cmd=="zgrep":
        print("We learned 'grep' can be used to find a word inside a file. Can something similar be used to find a word inside a compressed file?")
    elif cmd=="ln":
        print("Lookup which command can be used for establishing links between files. For better clarity, also check out the difference between links of a file and copy command")
    elif cmd=="chattr":
        print("The attributes of a file in Unix-like system is represented by -------------e-- (16 '-'). Try to learn what each - represents and how can we change modes of a files.")
    elif cmd=="ifconfig":
        print("First get a list of all interfaces and then use a flag to get the short list.")
    elif cmd=="rm":
        print("Check which command can be used to remove a folder containing files inside it!")
    elif cmd=="mv":
        print("Moving a file is same as renaming the file in that folder.")
    elif cmd=="pwd":
        print("Think of a command which can give you the absolute path")
    elif cmd=="tail":
        print("First try to get the content of the whole file and then use some command to get only the last lines. Counting occurences can be done further considering the filtered text as new content.")
    elif cmd=="whoami":
        print("Think of a command which can list out the username")
    elif cmd=="man":
        print("Use a command to get the manual page for the given command")
    elif cmd=="nano":
        print("Open some editor to add this line to the file")
    elif cmd=="sudo":
        print("Don't have the permission to access the file? Can you take the root access to open the file?")
