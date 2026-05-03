import datetime
from typing import Dict


class DateValueCollection:
    # A simple collection that stores date-value pairs.

    def __init__(self):
        # Create an empty collection.
        self._values = {}  # This will store date -> value pairs

    def add_value(self, date: datetime.date, value: float):
        """
        Add a temperature value for a specific date.

        Args:
            date: The date (like datetime.date(2020, 1, 1))
            value: The temperature value (like 25.5)

        Raises:
            ValueError: If we try to add the same date twice
        """
        if date in self._values:
            raise ValueError(f"Date {date} already exists!")
        self._values[date] = value

    def get_values(self) -> Dict[datetime.date, float]:
        
        # Get all the date-value pairs we have stored. Returns: A dictionary with dates as keys and values as temperatures
      
        return self._values.copy()  # Return a copy so they can't change our data

    def get_peak_yearly_values(self) -> Dict[datetime.date, float]:
        
        # For each year, find the highest temperature and return it with its date. 
        # Returns: A dictionary where each date is the day with the highest temp for that year
        
        yearly_peaks = {}

        # Go through each date and value we have
        for date, value in self._values.items():
            year = date.year

            # If we haven't seen this year yet, or this value is higher than what we have
            if year not in yearly_peaks or value > yearly_peaks[year][1]:
                yearly_peaks[year] = (date, value)

        # Convert back to the format we need: date -> value
        result = {}
        for year, (date, value) in yearly_peaks.items():
            result[date] = value

        return result