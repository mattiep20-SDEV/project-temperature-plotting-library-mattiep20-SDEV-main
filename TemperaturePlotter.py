import matplotlib.pyplot as plt
from typing import Dict
import datetime
import os


class TemperaturePlotter:
    # A simple class to create and save temperature plots from date-value data.

    def __init__(self, output_file_path: str):
        # Create a plotter that will save plots to the specified output file path.
        self._output_file_path = output_file_path

    def plot(self, values: Dict[datetime.date, float]):
       # Create a line plot of temperature values over time and save it to the output file path.
        if not values:
            raise ValueError("No values to plot")

        # Sort the data by date
        sorted_dates = sorted(values.keys())
        temperatures = [values[date] for date in sorted_dates]

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_dates, temperatures, marker='o', linestyle='-', color='blue')

        # Add labels and title
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Over Time')

        # Rotate date labels so they're readable
        plt.xticks(rotation=45)

        # Add grid for easier reading
        plt.grid(True, alpha=0.3)

        # Save the plot
        plt.tight_layout()
        plt.savefig(self._output_file_path, dpi=150, bbox_inches='tight')
        plt.close()  # Close the figure to free memory