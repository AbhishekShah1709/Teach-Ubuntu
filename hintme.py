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
