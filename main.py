import datetime
from DateValueCollection import DateValueCollection
# from TemperatureFileParser import TemperatureFileParser
# from TemperaturePlotter import TemperaturePlotter

'''
This is simply a test harness for the program and will not be graded.
What will be graded is implementation and understanding of the three other classes.
'''
def main():
    # #########################################################
    # Uncomment these to test your program.
    # It is recommended that you implement these in the order shown.
    # You may edit this file as needed to test your program.
    # Use breakpoints and print statements as you are developing to see what
    # your program is doing.
    # #########################################################

    ## DateValueCollection tests
    values = DateValueCollection()
    values.add_value(datetime.date(2020, 1, 1), 10.0)
    values.add_value(datetime.date(2020, 1, 2), 20.0)
    values.add_value(datetime.date(2020, 1, 3), 30.0)
    print("All values:", values.get_values())

    # Test duplicate key error
    try:
        values.add_value(datetime.date(2020, 1, 3), 30.0)
        print("ERROR: Should have raised ValueError for duplicate date")
    except ValueError as e:
        print(f"Correctly caught duplicate error: {e}")

    # Test peak yearly values
    values.add_value(datetime.date(2021, 1, 1), 15.0)
    values.add_value(datetime.date(2021, 1, 2), 25.0)  # This should be the peak for 2021
    values.add_value(datetime.date(2021, 1, 3), 20.0)
    print("Peak yearly values:", values.get_peak_yearly_values())

    ## TemperatureFileParser tests
    # parser = TemperatureFileParser("data/sample_data_partial.csv")
    # values = parser.parse()
    # DEBUG
    # print(values)

    ## TemperaturePlotter tests
    # plotter = TemperaturePlotter("output/temperature_plot.png")

    ## Example usage - both should work when you are finished
    # plotter.plot(values['Japan'].get_values())
    # plotter.plot(values['Japan'].get_peak_yearly_values())
    pass

if __name__ == "__main__":
    main()
