
import BluetoothDOSAttack
import os
import sys
import pexpect



# https://pypi.org/project/pexpect/

def DosBot():
    ##os.system('python3 BluetoothDOSAttack.py')
    child = pexpect.spawn('python3 BluetoothDOSAttack.py')
    child.sendline('y')
    child.sendline('target address')
    child.sendline('package size')
    child.sendline('2')
    ##child.logfile = sys.stdout.buffer
    ##print(child.logfile)
    ##child.close()
    ##print(child.exitstatus, child.signalstatus)
    ##child.expect()


def header():
    print("Welcome to the SuiteTooth - the automated Bluetooth and BLE vulnerability scanning and attacking framework")
    print("we will now perform the intial scan")
    scan()

def btlejuiceAttack()
    mydir = os.getcwd()
    mydir_tmp = mydir + "/btlejuice"
    mydir_new = os.chdir(mydir_tmp)
    os.system('')
    mydir = os.getcwd() 


def scan():
    print("Perfoming scanning of the nearby Bluethooth and BLE devices. This may take a while...")
    mydir = os.getcwd()
    mydir_tmp = mydir + "/bluescan"
    mydir_new = os.chdir(mydir_tmp)
    os.system('python3 bluebornescan.py')
    mydir = os.getcwd() 
 
    print("Finished scanning. Saving the MAC addresses into devices.txt")
    
    macs = []
    for mac in macs:
        print("Starting attacks against MAC: " + mac)


if __name__ == "__main__":
    ##DosBot()
    header()
    
