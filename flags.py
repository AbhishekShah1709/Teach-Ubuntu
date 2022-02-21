import subprocess
import os 

def get_flag(cmd):

    if cmd=="ls":
        corr_cmd = subprocess.Popen(("ls test_dir | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="cp":
        if os.path.isfile("./test_dir/dup.txt"):
            corr_cmd_dup = subprocess.Popen(("cat test_dir/dup.txt"), stdout=subprocess.PIPE, shell=True)
            corr_output_dup = corr_cmd_dup.communicate()[0]
        
            corr_cmd_a = subprocess.Popen(("cat test_dir/a.txt"), stdout=subprocess.PIPE, shell=True)
            corr_output_a = corr_cmd_a.communicate()[0]
           
            if corr_output_a==corr_output_dup:
                corr_cmd = subprocess.Popen(("cat test_dir/dup.txt | wc -w"), stdout=subprocess.PIPE, shell=True)
                corr_output = corr_cmd.communicate()[0]
                return corr_output.decode('utf-8')
            else:
                print("File content of a.txt and dup.txt differs")
                return "err"

        else:
            print("File dup.txt does not exists")
            return "err"

    if cmd=="diff":
        corr_cmd = subprocess.Popen(("diff test_dir/a.txt test_dir/b.txt | grep \"^>\" | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="grep":
        corr_cmd = subprocess.Popen(("grep Hello test_dir/c.txt | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="wc":
        corr_cmd = subprocess.Popen(("wc test_dir/a.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        lst = corr_output.decode('utf-8').split(" ")
        val = 0
        for num in lst[:-1]:
            if num!='':
                val += int(num)

        return val

    if cmd=="chmod":
        verify = subprocess.Popen(("ls test_dir -la | grep d.txt"), stdout=subprocess.PIPE, shell=True)
        verified_output = verify.communicate()[0]
        
        val = verified_output.decode('utf-8').split(" ")[0]
        
        if val=="-r--------":
            corr_cmd = subprocess.Popen(("cat test_dir/d.txt"), stdout=subprocess.PIPE, shell=True)
            corr_output = corr_cmd.communicate()[0]

            return corr_output.decode('utf-8')
        else:
            print("Make sure you gave the exact perission as specified")
            return "err"

    if cmd=="piping":
        corr_cmd = subprocess.Popen(("cat test_dir/b.txt | head -3 | wc -w"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="redirect":
        corr_cmd = subprocess.Popen(("ls test_dir > test_dir/my_hidden.txt | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        if os.path.isfile("./test_dir/hidden.txt"):
            cnt=0

            hid_file = subprocess.Popen(("cat test_dir/hidden.txt"), stdout=subprocess.PIPE, shell=True)
            hid_output = hid_file.communicate()[0]

            my_hid_file = subprocess.Popen(("cat test_dir/my_hidden.txt"), stdout=subprocess.PIPE, shell=True)
            my_hid_output = my_hid_file.communicate()[0]

            hid_set = set()
            my_hid_set = set()

            for file_name in hid_output.decode('utf-8').split("\n"):
                if file_name!="":
                    hid_set.add(file_name)

            for file_name in my_hid_output.decode('utf-8').split("\n"):
                if file_name!="my_hidden.txt" and file_name!="":
                    cnt+=1
                    my_hid_set.add(file_name)

            if hid_set==my_hid_set:
                return cnt
            else:
                print("Make sure you made the file with the required conditions")
                return "err"
        else:
            print("Make sure you made the file with the required conditions")
            return "err"


    if cmd=="uname":
        corr_cmd = subprocess.Popen(("uname -s -n"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="md5sum":
        return 5

    if cmd=="sha256sum":
        return 3

    if cmd=="uid":
        corr_cmd = subprocess.Popen(("id -G"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        lst = corr_output.decode('utf-8').split(" ")
        val = 0
        for num in lst:
            val += int(num)

        return val

    if cmd=="gzip":
        return "__THIS_IS_THE_FLAG_FOR_THIS_COMMAND__"

    if cmd=="zgrep":
        return 5 

    if cmd=="ln":
        corr_cmd = subprocess.Popen(("ls -la test_dir | grep ln.py"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        val = corr_output.decode('utf-8').split(" ")[1]

        if val==2:
            return "__THIS_IS_THE_FLAG_FOR_LN_COMMAND__"
        else:
            print("Make hardlink for ln.py")
            return "err"
    
    if cmd=="chattr":
        val = "-----a-------e--"
        
        corr_cmd = subprocess.Popen(("lsattr test_dir/e.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        if val==corr_output.decode('utf-8').split(" ")[0]:
            return val
        else:
            print("Change the attributes of e.txt as mentioned")
            return "err"
    
    if cmd=="ifconfig":
        corr_cmd = subprocess.Popen(("ifconfig -s | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = int(corr_output.decode('utf-8')) - 1
        
        return val
    
    if cmd=="rm":

        if os.path.isdir("./test_dir/delete")==False:
            return 100
        else:
            print("Remove the folder mentioned")
            return "err"

    if cmd=="mv":

        if os.path.isfile("test_dir/this.txt")==False and os.path.isfile("test_dir/that.txt")==True:
            corr_cmd = subprocess.Popen(("grep __FLAG__ test_dir/that.txt -o -i | wc -l"), stdout=subprocess.PIPE, shell=True)
            corr_output = corr_cmd.communicate()[0]

            val = corr_output.decode('utf-8')

            return val

        else:
            print("Make sure this.txt is removed and that.txt exists!")
            return "err"


    if cmd=="pwd":
        corr_cmd = subprocess.Popen(("pwd"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = corr_output.decode('utf-8')

        return val

    if cmd=="tail":
        corr_cmd = subprocess.Popen(("cat test_dir/count.txt | tail -50 | grep '__FLAG__' -o -i | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = corr_output.decode('utf-8')
        
        return val

    if cmd=="whoami":
        corr_cmd = subprocess.Popen(("whoami"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = corr_output.decode('utf-8')
        
        return val

    if cmd=="man":
        val = "man is the system's manual pager"
        return val
    
    if cmd=="nano":
        verify = subprocess.Popen(("cat test_dir/new.txt | tail -1"), stdout=subprocess.PIPE, shell=True)
        verified_output = verify.communicate()[0]

        val = verified_output.decode('utf-8')

        if val.strip()!="This is the last line of the file. Delete this line.":
            return 1501
        else:
            print("Make sure you deleted the last line")
            return "err"

    
    if cmd=="sudo":
        return "__THIS_IS_THE_HIDDEN_FLAG__"

