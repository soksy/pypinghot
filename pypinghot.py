#pypinghot.py
#author Soksy - but i really just googled it!

import subprocess
import os

net = input("What Network: ")
firstip = input("Start IP: ")
lastip = input("Last IP: ")

with open(os.devnull, "wb") as bitbucket:
    for n in range(1, 11):
        ip=net + ".{0}".format(n)
        result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],shell=False,stdout=bitbucket, stderr=bitbucket).wait()
        if result:
            print(ip, "inactive")
	else:
            print(ip, "active")
