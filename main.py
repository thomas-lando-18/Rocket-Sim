# Project: Rocket Launch Simulation
# Title  : Main Script
# Author : Thomas Lando

# This script will be used to run the simulation.  It will outline the general process and assumptions used to run the
# simulation.

# Assumptions:

# Import Packages
import numpy as np

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

# ----------------------------------------------------------------------------------------------------------------------
#                                                   TESTING CODE
# ----------------------------------------------------------------------------------------------------------------------

# Running the 2D Simulation

# Set up time vector
time_final = float(input('Please state the amount of time you wish to run the Simulation for: '))
time_n = int(input('Please state the number or time steps you wish to conduct: '))
time_vector = np.linspace(0, time_final, num=time_n)


# functions to use
def x_dim_change(system):
    system.state.xdd = 1 / system.state.mass * np.cos(system.state.theta) * (
                system.rocket_data.max_thrust - 1 / 2 * system.state.xd ** 2 *
                system.environmental_data.location_data.Density_0 * 0.3)
    system.state.xd = system.state.xdd * system.state.dt
    system.state.x = system.state.xd * system.state.dt

    return system.state


def y_dim_change(system):
    system.state.ydd = 1 / system.state.mass * np.sin(system.state.theta) * (system.rocket_data.max_thrust - 1 / 2 *
                                                                             system.state.yd ** 2 *
                                                                             system.environmental_data.location_data.
                                                                             Density_0 * 0.3) - 9.81
    system.state.yd = system.state.ydd * system.state.dt
    system.state.y = system.state.yd * system.state.dt

    return system.state


# set up initial state for looping
non_linear_system.state = non_linear_system.initial_data
non_linear_system.state.dt = time_vector[1] - time_vector[0]
# loop through simulation
for n in range(len(time_vector)):
    non_linear_system.state = x_dim_change(non_linear_system)
    non_linear_system.state = y_dim_change(non_linear_system)
    # print(non_linear_system.state.x)
    print(non_linear_system.state.y)
