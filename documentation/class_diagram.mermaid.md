```
classDiagram
    class TemperatureFileParser {
        -_data_file_path: str
        +__init__(data_file_path: str)
        -_get_date_from_row(row: list~str~) datetime.date
        -_validate_header(header: list~str~)
    }

    class DateValueCollection {
        -_values: dict~datetime.date, float~
        +__init__()
        +add_value(date: datetime.date, value: float)
        +get_values()
        +get_peak_yearly_values() dict~datetime.date, float~
    }

    class TemperaturePlotter {
        -_output_file_path: str
        +__init__(output_file_path: str)
        +plot(values: dict~datetime.date, float~) None
    }

    TemperatureFileParser --> DateValueCollection : parses into collections
    TemperaturePlotter ..> DateValueCollection : plots values from
```
