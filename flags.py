import subprocess

def get_flag(cmd):

    if cmd=="ls":
        corr_cmd = subprocess.Popen(("ls | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="cp":
        corr_cmd = subprocess.Popen(("cp a.txt a_dup.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="diff":
        corr_cmd = subprocess.Popen(("diff a.txt b.txt | grep \"^>\" | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="wc":
        corr_cmd = subprocess.Popen(("wc a.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        lst = corr_output.decode('utf-8').split(" ")
        val = 0
        for num in lst:
            val += int(num)

        return val

    if cmd=="chmod":
        corr_cmd = subprocess.Popen(("chmod d.txt 400; cat d.txt | head -1"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = corr_output.decode('utf-8').split(" ")[0]
        return val

    if cmd=="piping":
        corr_cmd = subprocess.Popen(("cat b.txt | head -3 | wc -w"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="redirect":
        corr_cmd = subprocess.Popen(("ls -ad .?* > hidden.txt | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="uname":
        corr_cmd = subprocess.Popen(("uname -s -n"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="md5sum":
        corr_cmd = subprocess.Popen(("md5sum fingerprints1.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="sha256sum":
        corr_cmd = subprocess.Popen(("sha256sum fingerprints1.txt"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]
        
        return corr_output.decode('utf-8')

    if cmd=="uid":
        corr_cmd = subprocess.Popen(("id -G"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        lst = corr_output.decode('utf-8').split(" ")
        val = 0
        for num in lst:
            val += int(num)

        return val

    if cmd=="gzip":
        return "gzip_flag"

    if cmd=="zgrep":
        return "zgrep_flag"

    if cmd=="ln":
        return "ln_flag"
    
    if cmd=="chattr":
        
        return corr_output.decode('utf-8') 
    
    if cmd=="ifconfig":
        corr_cmd = subprocess.Popen(("ifconfig -s | wc -l"), stdout=subprocess.PIPE, shell=True)
        corr_output = corr_cmd.communicate()[0]

        val = corr_output.decode('utf-8') - 1
        
        return val

