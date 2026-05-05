# 'datetime' is a built-in module for working with dates and times.
import datetime 
# 'Dict' is a type hint for dictionaries, which are collections of key-value pairs.
from typing import Dict
from DateValueCollection import DateValueCollection 
# 'TemperatureFileParser' is a class that reads temperature data from CSV files and organizes it by country.
from TemperatureFileParser import TemperatureFileParser
# 'TemperaturePlotter' is a class that creates and saves temperature plots from date-value data.
from TemperaturePlotter import TemperaturePlotter

# This is the main file that will run the program. It will use the other classes to read data, process it, and create plots.
def main():

    ## DateValueCollection tests
    values = DateValueCollection()
    # Test adding and retrieving values
    values.add_value(datetime.date(2020, 1, 1), 10.0)
    # Add more values for the same year to test peak yearly values
    values.add_value(datetime.date(2020, 1, 2), 20.0)
    # This should be the peak for 2020
    values.add_value(datetime.date(2020, 1, 3), 30.0)
    # Add values for a different year
    values.add_value(datetime.date(2021, 1, 1), 15.0)
    print("All values:", values.get_values())   

    # Test peak yearly values
    # Add more values for 2021 to test peak yearly values
    values.add_value(datetime.date(2021, 1, 2), 25.0)  # This should be the peak for 2021
    # Add a lower value for 2021 to ensure it doesn't affect the peak
    values.add_value(datetime.date(2021, 1, 3), 20.0)
    # The expected output should show the peak value for 2020 as 30.0 on 2020-01-03 and the peak value for 2021 as 25.0 on 2021-01-02
    print("Peak yearly values:", values.get_peak_yearly_values())

    ## TemperatureFileParser tests
    # This should read the sample CSV file and print out the parsed data for each country, showing the number of data points and a few sample values.
    parser = TemperatureFileParser("data/sample_data_partial.csv")
    parsed_data = parser.parse()
    print(f"Parsed data for {len(parsed_data)} countries:")
    # For each country, print the number of data points and a few sample values to verify that the parsing worked correctly.
    for country, collection in parsed_data.items():
        # Get all values for this country and print the count and a few samples.
        all_values = collection.get_values()
        # Print the country name and the number of data points.
        print(f"  {country}: {len(all_values)} data points")
        # Show first few values
        sorted_dates = sorted(all_values.keys())[:3]
        # Print the first few date-value pairs for this country.
        for date in sorted_dates:
            # Print the date and the corresponding temperature value for this country.
            print(f"    {date}: {all_values[date]}°C")

    ## TemperaturePlotter tests
    # Create some test data
    test_values = DateValueCollection()
    # Add some sample date-value pairs to the collection to test the plotting functionality. These values will create a simple line plot when we call the plot method.
    test_values.add_value(datetime.date(2020, 1, 1), 10.0)
    # Add more values to create a more interesting plot.
    test_values.add_value(datetime.date(2020, 2, 1), 15.0)
    test_values.add_value(datetime.date(2020, 3, 1), 20.0)
    test_values.add_value(datetime.date(2020, 4, 1), 25.0)

    plotter = TemperaturePlotter("test_plot.png")
    # This will create a line plot of the test values and save it as "test_plot.png". The plot should show a steady increase in temperature from January to April 2020.
    plotter.plot(test_values.get_values())
    # After running this code, you should find a file named "test_plot.png" in your current directory, which contains the generated plot of the test temperature data.
    print("Created test_plot.png")

    
    # Create output directory if it doesn't exist
    import os
    # This will create an "output" directory if it doesn't already exist, which is where we will save the plots for Japan's temperatures and peaks.
    os.makedirs("output", exist_ok=True)
    # This will create a plot of all temperature values for Japan and save it as "output/japan_temperatures.png". The plot should show the temperature trends over time for Japan based on the data in the CSV file.

    plotter2 = TemperaturePlotter("output/japan_temperatures.png")
    # This will create a plot of the peak yearly temperature values for Japan and save it as "output/japan_peaks.png". 
    # The plot should show the highest temperature for each year, with the date corresponding to when that peak occurred.
    plotter2.plot(parsed_data['Japan'].get_values())
    # After running this code, you should find two files in the "output" directory: "japan_temperatures.png" 
    # which shows the temperature trends for Japan, and "japan_peaks.png" which shows the peak yearly temperatures for Japan.
    print("Created output/japan_temperatures.png")

    plotter3 = TemperaturePlotter("output/japan_peaks.png")
    # This will create a plot of the peak yearly temperature values for Japan and save it as "output/japan_peaks.png". 
    # The plot should show the highest temperature for each year, with the date corresponding to when that peak occurred.
    plotter3.plot(parsed_data['Japan'].get_peak_yearly_values())
    # After running this code, you should find two files in the "output" directory: "japan_temperatures.png" 
    # which shows the temperature trends for Japan, and "japan_peaks.png" which
    print("Created output/japan_peaks.png")

# When you run this main function, it will execute the tests for the DateValueCollection, TemperatureFileParser, 
# and TemperaturePlotter classes.
if __name__ == "__main__":
    main()
