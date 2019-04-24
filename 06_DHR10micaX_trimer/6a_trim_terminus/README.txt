In pymol, low energy protein+surface model from protocol 3a (example: 03_DHR10mica18_on_mica001_Ksublayer/3a_DHR10mica18_docking_on_potassium_sublattice/low_energy_model/DHR10mica18_rotamers_on_Ksublayer_Dock_12G_0015.pdb) was translated so coordinate origin was located at P6 site (central K ion). The protein was translated so its N-terminus was near origin. The lattice-matched register between the protein and the K sublayer was preserved during translation).

Five repeats (res 1-250) of DHR10mica18 saved as DHR10mica5_nterminus.pdb

Command to trim termini with Pyrosetta:

python2.7 ./trim_termini.py DHR10mica5_nterminus.pdb 
