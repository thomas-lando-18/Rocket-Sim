from .intergrator import integrate_trap
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import argparse
from .plot import Plotter

m2ft = 3.28084  # Converts from metre to ft.


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--show_plots", help="Triggers plot display", action='store_true')
    parser.add_argument("--units", help="Sets final units for presentation")


    args = parser.parse_args()

    print("Welcome to the Rocket Simulator")
    if args.show_plots:
        simulate(plot=True)
    else:
        simulate(plot=False)



def simulate(plot=True):
    # thrust = float(input("Enter Thrust value: "))
    thrust = 1000
    drag_coef = 0.01
    a_g0 = 9.81
    radius_e = 6371e3
    rho0 = 1.225
    area = 5
    scale_height = 8.5e3

    mass = 60

    time_start = 0
    time_end = 300
    dt = 0.1
    num_steps = int(np.round((time_end - time_start)/dt))

    a0 = 0
    v0 = 0
    s0 = 0

    # Initialise Result 
    time = [time_start]
    acceleration = [a0]
    velocity = [v0]
    displacement = [s0]

    for n in range(num_steps):

        rho = rho0 * np.exp(-displacement[n]/scale_height)
        a_g = a_g0 * (radius_e/(radius_e + displacement[n]))

        time.append(time[n] + dt)
        # print(time)
        a_n = thrust/mass - 0.5 * rho * velocity[n] ** 2 * area * drag_coef / mass - a_g
        acceleration.append(a_n)

        v_n = integrate_trap(time, acceleration)
        velocity.append(v_n)

        s_n = integrate_trap(time, velocity)
        displacement.append(s_n)

    print('Acceleration (m/s2): ' + str(acceleration[n]))
    print('Velocity (m/s): ' + str(velocity[n]))
    print('Displacement (m): ' + str(displacement[n]))

    plotter = Plotter()

    fig1, ax1 = plotter.initialise_figure()
    ax1 = plotter.add_line(fig=ax1, x_data=time, y_data=acceleration, data_label="Rocket A")
    ax1 = plotter.add_axis_labels(ax1, "Time (s)", "Acceleration (m/s)")
    ax1 = plotter.add_grid(ax1)

    fig2, ax2 = plotter.initialise_figure()
    ax2 = plotter.add_line(ax2, time, velocity, "Rocket A", 'b')
    ax2 = plotter.add_grid(ax2)
    ax2 = plotter.add_axis_labels(ax2, "Time (s)", "Velocity (m/s)")


    if plot:
        plt.show()
    
