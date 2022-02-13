def get_third_hint(cmd):

    if cmd=="ls":
        print("Write the command 'ls' and count the number of files and folder")
    elif cmd=="cp":
        print("Write the command 'cp a a_dup.txt'")
    elif cmd=="diff":
        print("Write the command 'diff a.txt b.txt | grep \"^>\" | wc -l'")
    elif cmd=="wc":
        print("Write the command 'wc a.txt' and count the sum of the three numbers")
    elif cmd=="chmod":
        print("Write the command 'chmod d.txt 400' and get the first word of the file")
    elif cmd=="piping":
        print("Write the command 'cat b.txt | head -3 | wc -w'")
    elif cmd=="redirect":
        print("Write the command 'ls -ad .?* > hidden.txt | wc -l'")
    elif cmd=="uname":
        print("Write the command 'uname -s -n'")
    elif cmd=="md5sum":
        print("Write the command 'md5sum fingerprints1.txt' and check the number of files that failed")
    elif cmd=="sha256sum":
        print("Write the command 'sha256sum fingerprints2.txt' and check the number of files that failed")
    elif cmd=="uid":
        print("Write the command 'id -G' and sum the numbers")
    elif cmd=="gzip":
        print("Write the command 'gzip -d message.zip' and find the flag")
    elif cmd=="zgrep":
        print("Write the command 'zgrep world compress.zip' and count the number of occurences")
    elif cmd=="ln":
        print("Write the command 'ln ln.py ln1.py' and execute either of this file to get the flag")
    elif cmd=="chattr":
        print("Write the command 'chattr +a e.txt; lsattr e.txt'")
    elif cmd=="ifconfig":
        print("Write the command 'ifconfig -s | wc -l' and subtract 1 from this number for headers")
