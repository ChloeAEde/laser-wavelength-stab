####### This code should have two connections: wave meter and DLC pro
######## from reading the values, it will keep running in the background
######## keeping the wavelength stable at the set_value frequency you tell it to
######## this set value can be adjusted without interrupting the code
########################## importing libraries ################################
from os.path import exists
import ctypes
import threading
import string
# wlmData.dll related imports
import wlmData
import wlmConst

# others
import sys
import time

#from toptica files
from time import sleep
from toptica.lasersdk.client import Client, SerialConnection
from toptica.lasersdk.client import UserLevel, Subscription, Timestamp, SubscriptionValue
from toptica.lasersdk.client import *


################# Connection with wavemeter #######################
#check can connect to the wavemeter
# Set the DLL_PATH variable according to your environment here:
DLL_PATH = r'C:/Users/admin/Downloads/HighFinesse Python Examples/wlmData.dll'

file_exists = exists(DLL_PATH)#check the dll file is here

print(file_exists)
print(ctypes.WinDLL(DLL_PATH))


# Set the Data acquisition time (sec) here:
DATA_ACQUISITION_TIME = 5

# Set the CallBack Thread priority here:
CALLBACK_THREAD_PRIORITY = 2

# Create callback function type using stdcall (WINFUNCTYPE) calling convention.
# The original function signature is void function(long, unsigned long, double)
# For more information see ctypes python library documentation.
#can ignore as not that important
CallBackFuncType = wlmData.ctypes.WINFUNCTYPE(None, wlmData.ctypes.c_long, wlmData.ctypes.c_ulong, wlmData.ctypes.c_double)

#### getting values from wavemeter ####
# Main program execution starts here
# Load DLL from DLL_PATH
try:
    wlmData.LoadDLL(DLL_PATH)
except:
    sys.exit("Error: Couldn't find DLL on path %s.\nPlease check the DLL_PATH variable!" % DLL_PATH)

set_value=float(319.01960)#319.01960 or the frequency you want the laser to be at
def checkChangeValue():
    """Function that will check if user enters a new set_value in the terminal"""
    global set_value
    while True:
        newSetValue=float(input())
        if isinstance(newSetValue,float):#if value is differnt than before otherwise it sets to 0
            set_value=float(newSetValue)
            print("new value assigned: ", set_value)


def main():
    """Function to connect to the DLC pro and change the set voltage based on the P value """
    pgain = 1000
    sum_dev = 0.0
    
    with Client(SerialConnection(port='COM5',baudrate=115200,timeout=5)) as client:#connect to dlc pro
        Frequency2=round(wlmData.dll.GetFrequencyNum(5,0),5)#Frequency on channel 5 of our fiber switch,round to 5 decimal points
        #print("Read out frequency: ", Frequency2)
        sum_dev = (set_value - Frequency2)

        voltage=client.get('laser1:dl:pc:voltage-set')#read original set voltage of our laser (not the acutal voltage)
        #print("Current voltage: ", voltage)
        #print("Sum dev: ", sum_dev)

        #print(pgain*sum_dev)
        voltage_new = voltage+pgain*sum_dev
        #print("Change in voltage: ", voltage_new-voltage)

        client.set('laser1:dl:pc:voltage-set',voltage_new)#change the set voltage
        
        time.sleep(1)#wait time to allow voltage to change in real time
            
            

#keep_me_going=True
    
if __name__ =='__main__':#runs the main files
    threading.Thread(target=checkChangeValue).start()#will loop over the checkChangeValue while still running the main function
    while True:
        main()