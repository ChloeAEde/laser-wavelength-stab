# laser-wavelength-stab
Python file that keeps the Toptica laser at a constant frequency by changing the piezo voltages based on the frequency wanted by the user (avoiding drifts). The program will run continuously until you manually stop it (uses multithreading to detect change from user input of new frequency value based upon the read value on a HighFinesse wavelength meter)

# Safety first
You are going to be playing around with lasers so please be safe and take all precautions as you would do normally.

# Requirements (Hardware)
* Toptica DLC pro
* HighFinesse WS7 series wavemeter

# Requirements (Software)
* Python 3.9
* HighFinesse wavelength meter software (deliver with device)

# Requirements (Python packages)
* ctypes
* threading
* time
* sys
* toptica_lasersdk

## Disclaimer
The above is the hardware that I used but some commands, setup might be different for different models, so check the requirements of your system. Also, all our hardware is connected via USB/COM port but it can be done with ethernet connection but this will also have a difference on the code.

# Let’s get started

- Download the .py file here
- Install the relevant python packages
- Find the location of you .dll file from Toptica (normally in the program file section where the DLC pro software is installed)
- Change value is the python code as below
- Whooo run your code

# Things you need to change in the code to match your system requirements
* DLL_PATH (from HighFinesse folder)
* set_value (the initial value you want the frequency set to) 
* Port connection to DLC pro (port='COMX')
* Frequency2 - change x in wlmData.dll.GetFrequencyNum(x,0) for what channel your wavemeter needs to read from

# Helpful tip-bits when things don’t work
* Make sure the wavelength software is running on the same PC you are running the python file (it needs to be on and click start)
* The DLC pro software does not need to be on. But the actual laser does need to be on
* Looking for the list of commands for your Toptica laser i.e. what goes into client.get()? There is a pdf file in the USB that came with your laser. THIS IS NOT ON THE ORIGINAL TOPTICA LASER SDK DOCUMENTATION!
* Other examples can be found on the [Toptica documentation](https://toptica.github.io/python-lasersdk/index.html#toptica-python-laser-sdk-documentation)
* HighFinesse also has examples in the files installed on your pc.
* I personally use visual studio code when running and writing code but for the final product, I recommend that you just run the program in the python cell to avoid anyone messing with the code by mistake.

# Future improvements
* Look out for mode jumps


# Help, I still don't know what is happening?
You can write to me on moin[at]404chloenotfound.com. Please be kind to my repo, I'm a physicist- we are not known for our amazing coding skills :) The people at Toptica and HighFinesse are also very lovely and helped me a lot in writing this code.

