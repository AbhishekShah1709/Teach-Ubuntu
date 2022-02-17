import subprocess

def execute_cmd(usr_cmd):

    user_cmd = subprocess.Popen(usr_cmd, stdout=subprocess.PIPE, shell=True)
    user_output = user_cmd.communicate()[0]

    print(user_output.decode('utf-8'))
