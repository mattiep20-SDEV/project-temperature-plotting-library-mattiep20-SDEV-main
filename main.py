import datetime
from DateValueCollection import DateValueCollection
from TemperatureFileParser import TemperatureFileParser
from TemperaturePlotter import TemperaturePlotter


def main():

    ## DateValueCollection tests
    values = DateValueCollection()
    values.add_value(datetime.date(2020, 1, 1), 10.0)
    values.add_value(datetime.date(2020, 1, 2), 20.0)
    values.add_value(datetime.date(2020, 1, 3), 30.0)
    print("All values:", values.get_values())   

    # Test peak yearly values
    values.add_value(datetime.date(2021, 1, 1), 15.0)
    values.add_value(datetime.date(2021, 1, 2), 25.0)  # This should be the peak for 2021
    values.add_value(datetime.date(2021, 1, 3), 20.0)
    print("Peak yearly values:", values.get_peak_yearly_values())

    ## TemperatureFileParser tests
    parser = TemperatureFileParser("data/sample_data_partial.csv")
    parsed_data = parser.parse()
    print(f"Parsed data for {len(parsed_data)} countries:")
    for country, collection in parsed_data.items():
        values = collection.get_values()
        print(f"  {country}: {len(values)} data points")
        # Show first few values
        sorted_dates = sorted(values.keys())[:3]
        for date in sorted_dates:
            print(f"    {date}: {values[date]}°C")

    ## TemperaturePlotter tests
    # Create some test data
    test_values = DateValueCollection()
    test_values.add_value(datetime.date(2020, 1, 1), 10.0)
    test_values.add_value(datetime.date(2020, 2, 1), 15.0)
    test_values.add_value(datetime.date(2020, 3, 1), 20.0)
    test_values.add_value(datetime.date(2020, 4, 1), 25.0)

    plotter = TemperaturePlotter("test_plot.png")
    plotter.plot(test_values.get_values())
    print("Created test_plot.png")

    ## Example usage - both should work when you are finished
    # Create output directory if it doesn't exist
    import os
    os.makedirs("output", exist_ok=True)

    plotter2 = TemperaturePlotter("output/japan_temperatures.png")
    plotter2.plot(parsed_data['Japan'].get_values())
    print("Created output/japan_temperatures.png")

    plotter3 = TemperaturePlotter("output/japan_peaks.png")
    plotter3.plot(parsed_data['Japan'].get_peak_yearly_values())
    print("Created output/japan_peaks.png")

if __name__ == "__main__":
    main()
