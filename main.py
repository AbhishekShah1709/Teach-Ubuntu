from challenges import print_challenge
from flags import get_flag

cmd_lst=['ls',
        'cp',
        'diff',
        'grep',
        'wc',
        'chmod',
        'ifconfig',
        'chattr',
        'ln',
        'gzip',
        'zgrep',
        'piping',
        'redirect',
        'uname',
        'md5sum',
        'sha256sum',
        'uid',
        'chmod',
        'rm',
        'mv',
        'pwd',
        'tail',
        'touch',
        'whoami',
        'man',
        'nano',
        'sudo']

f = open('./solved.txt','r+')
content = f.read()
f.close()

solved_cmd = set()

for line in content.split("\n"):
    solved_cmd.add(line)

cmd_idx = {}

print("Enter the number corresponding to the commmand you want to test yourself on: ")
print()
print("*********************************************************")

cnt=1

for i in range(len(cmd_lst)):
    if cmd_lst[i] not in solved_cmd:
        print(cnt, end=": ")
        print(cmd_lst[i])
        cmd_idx[cnt] = cmd_lst[i]
        cnt+=1

print()
print("Enter quit to EXIT")
print("*********************************************************")

usr_choice = input("Input your choice: ")

idx_keys = []
for key in cmd_idx.keys():
    idx_keys.append(str(key))

if usr_choice=="quit": 
    exit(0)
    
elif usr_choice in idx_keys:
    print_challenge(cmd_idx[int(usr_choice)])

else:
    print()
    print("Please give correct input!")

