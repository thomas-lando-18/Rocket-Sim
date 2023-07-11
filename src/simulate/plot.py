import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Plotting Functions
class Plotter:

    # def __init__(self) -> None:
    #     pass


    def initialise_figure(args):
        fig, ax = plt.subplots()

        return fig, ax


    def add_scatter(args, fig: plt, x_data: list, y_data: list, data_label: str, color=None):
        
        # Check lengths
        if len(x_data) != len(y_data):
            return 'Error, data vectors must be same length'
        
        fig.scatter(x_data, y_data, color=color, label=data_label)
        
        return fig
    

    def add_line(args, fig: plt, x_data: list, y_data: list, data_label: str, color=None):
        
        # Check lengths
        if len(x_data) != len(y_data):
            return 'Error, data vectors must be same length'
        
        fig.plot(x_data, y_data, color=color, label=data_label)
        
        return fig
    
    def add_grid(args, ax):
        ax.grid()
        return ax

    def add_axis_labels(args, ax, x_label, y_label):
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        return ax
    
    

