import csv
import datetime
from typing import Dict
from DateValueCollection import DateValueCollection


class TemperatureFileParser:
    """Reads temperature data from CSV files and organizes it by country."""

    def __init__(self, data_file_path: str):
        """Create a parser for a specific CSV file."""
        self._data_file_path = data_file_path

    def parse(self) -> Dict[str, DateValueCollection]:
        """
        Read the CSV file and return temperature data organized by country.

        Returns:
            Dictionary where keys are country names and values are DateValueCollection objects
        """
        countries = {}

        with open(self._data_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            # Process each data row
            for row in reader:
                self._process_row(row, countries)

        return countries

    def _process_row(self, row: list, countries: Dict[str, DateValueCollection]):
        """Process one row of data."""
        # Expect 4 columns: date, temperature, uncertainty, country
        if len(row) != 4:
            print(f"Skipping row with {len(row)} columns (expected 4)")
            return

        date_str, temp_str, uncertainty_str, country = row

        # Skip if any required field is empty
        if not date_str or not temp_str or not country:
            print("Skipping row with empty fields")
            return

        # Convert date string to date object
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print(f"Skipping invalid date: {date_str}")
            return

        # Convert temperature string to float
        try:
            temperature = float(temp_str)
        except ValueError:
            print(f"Skipping invalid temperature: {temp_str}")
            return

        # Get or create collection for this country
        if country not in countries:
            countries[country] = DateValueCollection()

        # Add the temperature data
        try:
            countries[country].add_value(date, temperature)
        except ValueError:
            print(f"Skipping duplicate date for {country}: {date}")
            return