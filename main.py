# Project: Rocket Launch Simulation
# Title  : Main Script
# Author : Thomas Lando

# This script will be used to run the simulation.  It will outline the general process and assumptions used to run the
# simulation.

# Assumptions:

# Import Packages
from Rocket_Sim_Class import Startup
from Rocket_Sim_Class import LaunchSetup
from Rocket_Sim_Class import DimensionalInitialise

# Start the program and select the  Rocket
non_linear_system = Startup()
# Set Location and Launch Parameters (i.e. number of dimensions to be analysed)
non_linear_system.environmental_data = LaunchSetup()

print('\nNow select the number of dimensions you wish to analyse the rocket launch in: ')
print('\n*** WARNING *** only 2 dimensions available at this time\n')
sim_dimension = input('Simulation Dimensions: ')
non_linear_system.initial_data = DimensionalInitialise(sim_dimension, non_linear_system)
# Run the Simulation

# Plot the Data
