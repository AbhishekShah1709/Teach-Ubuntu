import subprocess

def verify_cmd(cmd, usr_cmd):

    if cmd=="ls":
        corr_cmd = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
        corr_output = corr_cmd.communicate()[0]
        
        user_cmd = subprocess.Popen(usr_cmd.split(" "), stdout=subprocess.PIPE)
        user_output = user_cmd.communicate()[0]
    
        if user_output==corr_output:
            print()
            print("CONGRATULATIONS!")
            print()

            return 1
        else:
            print()
            print("TRY AGAIN!")
            print()
            
            return 0


def take_cmd(cmd):
    usr_cmd = input("Enter the command: ")
    passed = verify_cmd(cmd, usr_cmd)

    return passed
