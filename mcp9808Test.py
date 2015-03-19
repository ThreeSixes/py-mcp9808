# mcp9808 class by ThreeSixes (https://github.com/ThreeSixes/py-mcp9808)

from mcp9808 import mcp9808
from pprint import pprint
import time


# Set up our thermometer
thermo = mcp9808()

# Don't change this, change the next one
sample = True

# Change this to toggle loop mode.
loopMode = True

# Configure our sensor. The example here specifies defaults.
#thermo.setConfig(thermo.)

# Smaple!
while (sample):
    # Get the ambient temeprature.
    print("Ambient temperature (C): " + str(thermo.getAmbientTemp()))
    
    # If we want to loop, sleep 5 seconds.
    if loopMode:
        time.sleep(5)
    else:
        # If not, exit the loop.
        sample = False
    
