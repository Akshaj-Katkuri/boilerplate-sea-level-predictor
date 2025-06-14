import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope = line.slope
    intercept = line.intercept
    x_line = pd.Series(range(1880,2051))
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color='red')

    # Create second line of best fit
    df_recent = df[df['Year']>=2000]
    line2 = linregress(x=df_recent['Year'], y=df_recent['CSIRO Adjusted Sea Level'])
    slope2 = line2.slope
    intercept2 = line2.intercept
    x_line2 = pd.Series(range(2000,2051))
    y_line2 = slope2 * x_line2 + intercept2
    plt.plot(x_line2, y_line2, color='blue')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()