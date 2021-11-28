import numpy as np
  
def ax_scatter(axes, x, y, xlabel, ylabel, title, color='steelblue', reg=False):
    """
    Create a scatter plot on the given axes with certain parameters
    
    """
    # Plot the inputs x,y in the provided color
    axes.scatter(x, y, color=color)

    # Set the x-axis label
    axes.set_xlabel(xlabel, color=color)

    # Set the y-axis label
    axes.set_ylabel(ylabel, color=color)
  
    # Set the title
    axes.set_title(title, color='brown')

    # Set the colors tick params for y-axis
    axes.tick_params('y', colors=color)
    
    # Add a regression line to the plot
    if reg:
        m, b = np.polyfit(x.astype(float), y.astype(float), 1)
  
        axes.plot(x, m*x+b, color = 'salmon')
  