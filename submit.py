import sys
from flags import get_flag

cmd = sys.argv[1]
flag = sys.argv[2]

corr_flag = get_flag(cmd)

flag = str(flag)
corr_flag = str(corr_flag)

print("CORR FLAG: ", end='')
print(corr_flag)

print("USR_FLAG: ", end='')
print(flag)

if corr_flag=="err":
    print("TRY AGAIN!")
elif flag.strip()==corr_flag.strip():
    print("CONGRATULATIONS! YOU HAVE MASTERED THIS COMMAND")
    f = open('./solved.txt','a')
    f.write(cmd)
    f.write("\n")
    f.close()
else:
    print("TRY AGAIN!")
