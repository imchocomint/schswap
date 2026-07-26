import subprocess
import sys
def listsch():
    subprocess.run(["ls /usr/bin | grep scx_ > /tmp/scx_list.txt"], shell=True, check=True)
    subprocess.run(["ls /usr/bin | grep scx- >> /tmp/scx_list.txt"], shell=True, check=True)

def showlist():
    with open("/tmp/scx_list.txt", "r") as f:
        print("Available schedulers:")
        for line in f:
            print(line.strip())
