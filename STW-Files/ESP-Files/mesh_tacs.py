from mpi4py import MPI
from tacs import caps2tacs
import os

comm = MPI.COMM_WORLD

base_dir = os.path.dirname(os.path.abspath(__file__))

# make the tacs model
tacs_model = caps2tacs.TacsModel.build(
    csm_file="aob-kulfan.csm",
    comm=comm,
    problem_name="struct_mesh",
    verbosity=0,
)

tacs_model.mesh_aim.set_mesh(
    edge_pt_min=2,
    edge_pt_max=20,
    global_mesh_size=0.3,
    max_surf_offset=0.2,
    max_dihedral_angle=15,
).register_to(tacs_model)

egads_aim = tacs_model.mesh_aim
tacs_aim = tacs_model.tacs_aim

tacs_aim.set_config_parameter("view:flow", 0)
tacs_aim.set_config_parameter("view:struct", 1)

if comm.rank == 0:
    aim = egads_aim.aim
    aim.input.Mesh_Sizing = {
        "chord": {"numEdgePoints": 40},
        "span": {"numEdgePoints": 20},
        "vert": {"numEdgePoints": 20},
    }

if comm.rank == 0:
    egads_aim.aim.runAnalysis()
    egads_aim.aim.geometry.view()

exit()
