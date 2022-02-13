def get_first_hint(cmd):

    if cmd=="ls":
        print("List all files and count it")
    elif cmd=="cp":
        print("Copy ")
    elif cmd=="diff":
        print("'diff' command can be used here along with piping operation")
    elif cmd=="wc":
        print("'wc' command can be used here")
    elif cmd=="chmod":
        print("'chmod' command can be used here")
    elif cmd=="piping":
        print("Use piping along with head and wc command")
    elif cmd=="redirect":
        print("Use redirection along with piping and ls command")
    elif cmd=="uname":
        print("'uname' command can be used here with some flags")
    elif cmd=="md5sum":
        print("'md5sum' command can be used here")
    elif cmd=="sha256sum":
        print("'sha256sum' command can be used here")
    elif cmd=="uid":
        print("'id' command can be used here with some flag")
    elif cmd=="gzip":
        print("'gzip' command can be used here with some flag")
    elif cmd=="zgrep":
        print("'zgrep' command can be used here")
    elif cmd=="ln":
        print("'ln' command can be used here")
    elif cmd=="chattr":
        print("'chattr' command can be used here and 'lsattr' command can be used to get the flag")
    elif cmd=="ifconfig":
        print("'ifconfig' command can be used here with some flag")
