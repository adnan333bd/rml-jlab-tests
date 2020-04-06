import os

def install_dependency():
    os.system("sudo apt-get install python-nose python3-nose -y")
    os.system("python3 -m nose")

install_dependency()