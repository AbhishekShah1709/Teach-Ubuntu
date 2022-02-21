def get_third_hint(cmd):

    if cmd=="ls":
#        print("Write the command 'ls' and count the number of files and folder")
        print("Write the command 'ls | cat -n'")
    elif cmd=="cp":
        print("Write the command 'cp a a_dup.txt' and then count the number of words in dup.txt using wc command")
    elif cmd=="diff":
        print("Write the command 'diff a.txt b.txt | grep \"^>\" | wc -l'")
    elif cmd=="grep":
        print("Write the command 'grep Hello c.txt | wc -l'")
    elif cmd=="wc":
        print("Write the command 'wc a.txt' and count the sum of the three numbers")
    elif cmd=="chmod":
        print("Write the command 'chmod d.txt 400' and get the first word of the file")
    elif cmd=="piping":
        print("Write the command 'cat b.txt | head -3 | wc -w'")
    elif cmd=="redirect":
        print("Write the command 'ls > hidden.txt | wc -l'")
    elif cmd=="uname":
        print("Write the command 'uname -s -n' and submit the flag within inverted quotes")
    elif cmd=="md5sum":
        print("Write the command 'md5sum -c fingerprints1.txt' and check the number of files that failed")
    elif cmd=="sha256sum":
        print("Write the command 'sha256sum -c fingerprints2.txt' and check the number of files that failed")
    elif cmd=="uid":
        print("Write the command 'id -G' and sum the numbers")
    elif cmd=="gzip":
        print("Write the command 'gzip -d message.gz' and find the flag")
    elif cmd=="zgrep":
        print("Write the command 'zgrep world compress.zip -o | wc -l' and count the number of occurences")
    elif cmd=="ln":
        print("Write the command 'ln ln.py ln1.py' and execute either of this file to get the flag")
    elif cmd=="chattr":
        print("Write the command 'chattr +a e.txt; lsattr e.txt'")
    elif cmd=="ifconfig":
        print("Write the command 'ifconfig -s | wc -l' and subtract 1 from this number for headers")
    elif cmd=="rm":
        print("Write the command rm -rf ./delete to remove all files within the delete folder. But be sure to check the number of files inside it before this to get the flag")
    elif cmd=="mv":
        print("mv this.txt that.txt | grep __FLAG__ that.txt -o -i | wc -l")
    elif cmd=="pwd":
        print("Write the command 'pwd' and submit it as a flag")
    elif cmd=="tail":
        print("Write the command 'cat count.txt | tail -50 | grep __FLAG__ -o -i | wc -l' to get the required value")
    elif cmd=="whoami":
        print("Write the command 'whoami' and submit it as a flag")
    elif cmd=="man":
        print("Write the command 'man man' and get the flag as mentioned and submit it within inverted quotes")
    elif cmd=="nano":
        print("Write the command 'nano new.txt' to open the editor and then delete the last line. Save it and count the number of characters")
    elif cmd=="sudo":
        print("Write the command 'sudo permission.txt' to open the file and get the flag")
