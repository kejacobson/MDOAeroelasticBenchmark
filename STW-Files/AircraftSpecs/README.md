# Structural files

## File descriptions:

- **`STWSpecs.py`:** Python file containing various aircraft and mission specifications, designed to be imported and used in other scripts, particularly the `aircraftSpecs` dictionary.
- **`STWFlightPoints.py`:** Python file defining each of the flight points used in the benchmark problems.

## Usage:

To import the aircraft and flight point data into your python script, use the following:

```python
from STWFlightPoints import flightPointSets
from STWSpecs import aircraftSpecs
```

If your script is not in the same directory as the specs files, you'll need to use the `sys` module to add the directory to the path:

```python
sys.path.append("path/to/STW-Files/AircraftSpecs")
from STWFlightPoints import flightPointSets
from STWSpecs import aircraftSpecs
```
