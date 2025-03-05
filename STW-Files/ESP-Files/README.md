# Engineering Sketch Pad Model

This directory contains the implementation of the Simple Transonic Wing in Engineering Sketch Pad: enabling parametric CAD. This has been used with FUNtoFEM and FUN3D. The airfoil shapes are parameterized with Kulfan parameters. The main script is `aob-kulfan.csm`, which references *user-defined components* in `comps/`. Design parameters are created and listed in `aob-kulfan.csm`. 

To create the structural model, set the configure parameters: `cfgpmtr view:flow 0` and `cfgpmtr view:struct 1`. To create the aerodynamic model, set the configure parameters: `cfgpmtr view:flow 1` and `cfgpmtr view:struct 0`. These values can be set after the model is loaded into pyCAPS. 

The `test_csm` folder contains several `.csm` files to test the various user-defined components. Meshes may be generated prior to runtime using the `mesh_fun3d.py` and `mesh_tacs.py` scripts. Alternatively, the CAPS models may be loaded into the FUNtoFEM model through `caps2fun` and `caps2tacs` for shape design.