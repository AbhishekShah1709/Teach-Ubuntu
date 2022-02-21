for i in range(4,101):
    f = open("delete" + str(i) + ".txt",'w')
    f.write("This is random file number " + str(i))
    f.close()
