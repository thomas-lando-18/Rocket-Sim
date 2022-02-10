# Project: Rocket Launch Simulation
# Title  : Class Script
# Author : Thomas Lando (Oceania Engineering)

# Import Packages
import astropy.time.utils
import numpy as np
# Define Functions

# Build Classes


class Startup:

    def __init__(self):
        print('Welcome to Oceania Engineering\'s Rocket Simulator, please ensure that you enter everything carefully ')
        print('as the program is case sensitive.  Enjoy\n')
        default_filename = 'Default_Rocket_Database.dat'
        database_check = input('Enter the Database name, else Enter \'Default\' to access built in Rockets: ')
        if database_check == 'Default':
            database_filename = default_filename
        elif database_check == 'Manager':
            SoftwareManager(default_filename)
            database_filename = default_filename
        else:
            database_filename = database_check + '.dat'
        # Check to input new rocket
        new = input('Do you want to use a new rocket (yes/no)?: ')
        if new == 'yes':
            self.rocket_data = InputNewRocket(database_filename)
        else:
            print('Using Existing Rocket Data')
            see_data_check = input('Do you wish to see available Rockets in this database (yes/no)?: ')
            if see_data_check == 'yes':
                RocketNameList(database_filename)
                rocket_name = input('Enter the Rocket you wish to use: ')
            else:
                rocket_name = input('Enter the Rocket you wish to use: ')
            self.rocket_data = FindExistingRocket(database_filename, rocket_name)


class RocketNameList:

    def __init__(self, database_filename):
        print('The available rockets in this database:\n')
        fid = open(database_filename, 'r')
        file_lines = fid.readlines()
        for n in range(len(file_lines)):
            if file_lines[n].find('Rocket Name:') != -1:
                rocket_list = str.split(file_lines[n], ': ')[1]
                print(rocket_list)
        fid.close()

    def get_system(self):
        return self


class InputNewRocket:

    def __init__(self, rocket_data_filename):
        fid = open(rocket_data_filename, 'a')
        rocket_name = input('New Rocket Name: ')
        fid.write('Rocket Name: %s\n' % rocket_name)
        fid.write('Specific Impulse (s): %s\n' % input('Enter Specific Impulse (s): '))
        fid.write('Max Thrust (N): %s\n' % input('Enter Maximum Thrust (N): '))
        fid.write('Initial Mass (kg): %s\n' % input('Enter Initial Mass (kg): '))
        fid.write('Mass Ratio : %s\n' % input('Enter Mass Ratio: '))
        fid.write('Diameter (m): %s\n' % input('Enter Rocket Diameter (m): '))
        fid.write('Height (m): %s\n' % input('Enter Rocket Height (m): '))
        fid.close()

        self.rocket_data = FindExistingRocket(rocket_data_filename, rocket_name)

    def get_rocket(self):
        return self


class FindExistingRocket:

    def __init__(self, rocket_data_filename, rocket_name):
        fid = open(rocket_data_filename, 'r')
        file_lines = fid.readlines()
        for n in range(len(file_lines)):
            rocket_find = file_lines[n].find(rocket_name)
            if rocket_find != -1:
                self.Isp = float(str.split(file_lines[n+1])[3])
                self.max_thrust = float(str.split(file_lines[n+2])[3])
                self.mass_0 = float(str.split(file_lines[n+3])[3])
                self.mass_ratio = float(str.split(file_lines[n+4])[3])
                self.diameter = float(str.split(file_lines[n+5])[2])
                self.height = float(str.split(file_lines[n+6], ':')[1])
        fid.close()

    def get_rocket(self):
        return self


class LaunchSetup:

    def __init__(self):

        print('\nFollowing Vehicle selection the launch location must be chosen. The following launch locations are available in this version.')
        location_database_filename = 'Location_Database.dat'
        LocationNameList(location_database_filename)
        location_select = input('Enter name of Launch Location: ')
        self.location_data = GetLocationData(location_select, location_database_filename)

    def get_environment(self):
        return self


class SoftwareManager:

    def __init__(self, rocket_data_filename):
        enter_default_rocket_check = input('Add to Default Rocket Database (yes/no): ')
        if enter_default_rocket_check == 'yes':
            InputNewRocket(rocket_data_filename)
        enter_location_data_check = input('Add to Loaction data Database (yes/no): ')
        location_database_filename = 'Location_Database.dat'
        if enter_location_data_check == 'yes':
            AddLocationData(location_database_filename)


class AddLocationData:

    def __init__(self, location_database_filename):
        fid = open(location_database_filename, 'a')
        fid.write('Location Name: %s\n' % input('Enter Location Name: '))
        fid.write('Average Air Pressure (Pa): %s\n' % input('Enter Average Air Pressure (Pa): '))
        fid.write('Average Temperature (K): %s\n' % input('Enter Average Temperature (K): '))
        fid.write('Altitude (m): %s\n' % input('Enter Alttutde above Sea Level (m): '))
        fid.close()


class LocationNameList:

    def __init__(self, location_database_filename):
        fid = open(location_database_filename, 'r')
        file_lines = fid.readlines()
        for n in range(len(file_lines)):
            if file_lines[n].find('Location Name: ') != -1:
                print(str.split(file_lines[n], ':')[1])


class GetLocationData:

    def __init__(self, location_name, location_database_filename):
        fid = open(location_database_filename, 'r')
        file_lines = fid.readlines()
        for n in range(len(file_lines)):
            if file_lines[n].find(location_name) != -1:
                self.Pressure_0 = float(str.split(file_lines[n+1], ':')[1])
                self.Temperature_0 = float(str.split(file_lines[n+2], ':')[1])
                self.Altitude_0 = float(str.split(file_lines[n+3], ':')[1])

    def get_environment(self):
        return self


class DimensionalInitialise:

    def __init__(self, n_dim, system):

        # for two dimensional analysis
        if n_dim == '2' or n_dim == 'two':
            self.x = 0
            self.y = system.environmental_data.Altitude_0
            self.theta = np.pi/2
            self.xd = 0
            self.yd = 0
            self.thetad = 0
        elif n_dim == '3' or n_dim == 'three':
            print('\nComing soon please start again and select \'2\' or \'two\'')

    def __getnewargs__(self):
        return self


class TwoDimensionSim:

    def __init__(self, system):
        time_final = float(input('State the time you wish to run the sim for: '))
        system.time_vector =  np.linspace(0, time_final)

        for n in range(len(system.time_vector)):



    def get_state(self, state):
        return state

    def x_dim_change(self, system):

    def y_dim_change(self, system):

    def rotation_change(self, system):