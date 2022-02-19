import sys
from first_hint import get_first_hint
from second_hint import get_second_hint
from third_hint import get_third_hint

cmd = sys.argv[1]
val = sys.argv[2]

val = int(val)

if val==1:
    get_first_hint(cmd)
elif val==2:
    get_second_hint(cmd)
elif val==3:
    get_third_hint(cmd)
else:
    print("Invalid command!")


#    hint_cnt = 0
#    
#    print()
#    while True:
#        usr_input = input("-> ")
#        if usr_input.split(" ")[0]=="hintme":
#            hint_cnt += 1
#            if hint_cnt==1:
#                get_first_hint(cmd)
#            elif hint_cnt==2:
#                get_second_hint(cmd)
#            elif hint_cnt==3:
#                get_third_hint(cmd)
#            else:
#                print("No more hints allowed!")
#
#        elif usr_input.split(" ")[0]=="submit":
#            usr_flag = usr_input.split(" ")[1]
#            corr_flag = get_flag(cmd)
#
#            if usr_flag.strip()==corr_flag.strip():
#                print()
#                print("CONGRATULATIONS! YOU HAVE MASTERED THIS COMMAND")
#                print()
#                break
#            else:
#                print()
#                print("TRY AGAIN!")
#                print()
#        else:
#            execute_cmd(usr_input)
#
