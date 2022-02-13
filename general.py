import subprocess

def execute_cmd(cmd, usr_cmd):

    user_cmd = subprocess.Popen(usr_cmd.split(" "), stdout=subprocess.PIPE)
    user_output = user_cmd.communicate()[0]

    print(user_output.decode('utf-8'))
