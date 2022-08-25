# laser-wavelength-stab
Controls the toptica DLC pro to make automatic changes to the voltage based off readings from the frequency of the laser. Allows user input of desired frequency. The programme will run contiunously until you manually stop it (uses multithreading to detect change from user input of new frequency value)

# Saftey first
You are going to be playing around with lasers so please be safe and take all procautions as you would do normally.

# Requirements (Hardware)
* Toptica DLC pro
* HighFinesse WS7 series wavemeter

# Requirements (Software)
* Python 3.9
* HighFinesse wavelength meter software (deliever with device)

## Disclaimer
The above is the hardware that I used but some commands, setup might be different for different models, so check the requiremetns of your system. Also all our hardware is connected via USB/COM port but it can be done with ethernet connection but this will also have a difference on the code.

# Lets get started

- Download the .py file here
- Install the relevant packaages
- Find the location of you .dll file from toptica (normally in the programme file section where the DLC pro software is installed)

# Things you need to change in the code to match your system requirements
* DLL_PATH
* set_value (the initial value you want the frequency set to) 
* Port connection to DLC pro (port='COMX')
* Frequency2 - change x in wlmData.dll.GetFrequencyNum(x,0) for what channel your wavemeter needs to read from

# Helpful tip-bits when things dont work
* Make sure the wavelength software is running on the same PC you are running the python file (it needs to be on and click start)
* The DLC pro software does not need to be on. But the actual laser does need to be on
* Looking for the list of commands for your toptica laser i.e. what goes into client.get()? There is a pdf file in the USB that came with your laser. THIS IS NOT ON THE ORIGINAL TOPTICA LASER SDK DOCUMENTATION!
* Other examples can be found on the [toptica documentation](https://toptica.github.io/python-lasersdk/index.html#toptica-python-laser-sdk-documentation)
* HighFinnese also has examples in the files installed on your pc.
* I personally use visual studio code when running and writing code but for the final product, I recomend that you just run the programme in the python cell to avoid anyone messing with the code by mistake.

# Future improvements
* Look out for mode jumps


# Help, I still don't know what is happening?
You can write to me on moin[at]404chloenotfound.com. Please be kind to my repo, I'm a physcist- we are not know for our amazing coding skills :) The people at Toptica and HighFinesse are also very lovely and helped me a lot in writing this code. 
