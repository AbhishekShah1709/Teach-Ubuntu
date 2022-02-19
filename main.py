from info import get_info
from challenges import get_challenge
from flags import get_flag

#while 1:

print("Enter the number corresponding to the commmand you want to test yourself on: ")
print()
print("*********************************************************")
print("1: ls")
print("2: cp")
print("3: diff")
print("4: grep")
print("5: wc")
print("6: chmod")
print("7: ifconfig")
print("8: chattr")
print("9: ln")
print("10: gzip")
print("11: zgrep")
print("12: piping")
print("13: redirect")
print("14: uname")
print("15: md5sum")
print("16: sha256sum")
print("17: uid")
print("18: chmod")
print("19: rm")
print("20: mv")
print("21: pwd")
print("22: tail")
print("23: touch")
print("24: whoami")
print()
print("Enter quit to EXIT")
print("*********************************************************")

usr_choice = input("Input your choice: ")

if usr_choice=="1":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="2":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="3":
    get_info("diff")
    get_challenge("diff")

if usr_choice=="4":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="5":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="6":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="7":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="8":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="9":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="10":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="11":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="12":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="13":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="14":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="15":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="16":
    get_info("ls")
    get_challenge("ls")

if usr_choice=="17":
    get_info("chmod")
    get_challenge("chmod")

if usr_choice=="quit":
   exit(0) 
