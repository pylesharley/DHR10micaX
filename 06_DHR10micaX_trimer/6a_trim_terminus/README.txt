In pymol, full low energy model from 3a_globabl_docking_on_potassium_sublattice was translated so coordinate origin was located at P6 site (central K ion). The protein was additionally translated so its N-terminus was near origin. The lattice-matched register between the protein and the K sublayer was preserved.  

Five repeats (res 1-250) of DHR10mica18 saved as DHR10mica5_nterminus.pdb

Command to trim termini with Pyrosetta:

python2.7 ./trim_termini.py DHR10mica5_nterminus.pdb 
