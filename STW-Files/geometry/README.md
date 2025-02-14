# Wing geometry

## File descriptions:

- **`wing.igs/tin/dat`:** Geometry files of the wing outer mold line (OML)
- **`rae2822.dat`:** Airfoil coordinates for the RAE2822 airfoil
- **`wing-ffd-advanced-coarse/med/fine.xyz`:** FFD control volume definitions compatible with [pyGeo](github.com/mdolab/pygeo)
- **`generateOML.py`:** Python script that generates the wing OML geometry and FFD files using [pyGeo](github.com/mdolab/pygeo)
- **`wingGeometry.py`:** Python script that defines all of the wing's geometric parameters, designed to be used as the single source of truth, i.e imported into other scripts whenever they need values related to the wing geometry.
- **`setupDVGeo.py`:** Python function and script that demonstrates how to set up a valid geometry parameterization using the provided FFD files and pyGeo


## Usage:

To import the geometry data into your python script, use the following:

```python
from wingGeometry import wingGeometry
```

If your script is not in the same directory as the geometry file, you'll need to use the `sys` module to add the directory to the path:

```python
sys.path.append("path/to/STW-Files/geometry")
from wingGeometry import wingGeometry
```
