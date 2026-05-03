import datetime
from typing import Dict


class DateValueCollection:
    # A simple collection that stores date-value pairs.

    def __init__(self):
        # Create an empty collection.
        self._values = {}  # This will store date -> value pairs

    def add_value(self, date: datetime.date, value: float):
        # Add a date-value pair to the collection.
        # If the date already exists, raise a ValueError.
        if date in self._values:
            raise ValueError(f"Date {date} already exists in collection")
        self._values[date] = value

    def get_values(self) -> Dict[datetime.date, float]:
        # Get all values in the collection.
        return self._values.copy()  # Return a copy to prevent external modification    
    def get_peak_yearly_values(self) -> Dict[datetime.date, float]:
        # Get the peak (maximum) value for each year in the collection.
        yearly_peaks = {}

        # Group values by year
        values_by_year = {}
        for date, value in self._values.items():
            year = date.year
            if year not in values_by_year:
                values_by_year[year] = []
            values_by_year[year].append((date, value))

        # Find peak for each year
        for year, date_value_pairs in values_by_year.items():
            # Find the maximum value and its earliest date
            max_value = max(value for date, value in date_value_pairs)
            # Get the earliest date with this max value
            peak_date = min(date for date, value in date_value_pairs if value == max_value)
            yearly_peaks[peak_date] = max_value

        return yearly_peaks
