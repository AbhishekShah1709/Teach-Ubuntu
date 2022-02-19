import sys
from flags import get_flag

cmd = sys.argv[1]
flag = sys.argv[2]

corr_flag = get_flag(cmd)

if flag.strip()==corr_flag.strip():
    print("CONGRATULATIONS! YOU HAVE MASTERED THIS COMMAND")
else:
    print("TRY AGAIN!")
