#! /usr/bin/env python


full_atom_c2 = '''/home/pylesh/rosetta_builds/main/source/bin/rosetta_scripts.static.linuxgccrelease -database /home/pylesh/rosetta_builds/main/database @rosetta_scripts.flag -s {0} -scorefile score.sc  -parser:script_vars translate_X={1} translate_Y={2} distance={3} -suffix {4} -parser:protocol DHR10mica5H_monomer_honeycomb_C2_scan.xml'''
poly_ala_c2 = '''/home/pylesh/rosetta_builds/main/source/bin/rosetta_scripts.static.linuxgccrelease -database /home/pylesh/rosetta_builds/main/database @rosetta_scripts.flag -s {0} -scorefile score.sc  -parser:script_vars translate_X={1} translate_Y={2} distance={3} -suffix _POLYALA_{4} -parser:protocol DHR10mica5H_monomer_honeycomb_C2_scan_POLYALA.xml'''

translate_surface = '''/home/pylesh/rosetta_builds/main/source/bin/rosetta_scripts.static.linuxgccrelease -database /home/pylesh/rosetta_builds/main/database -s {0} -scorefile score.sc -parser:script_vars axis_X={1} axis_Y={2} distance={3} -suffix _{4} -parser:protocol translate_surface.xml -nstruct 1 -beta -mute all '''

import numpy
import sys



def format_coordinate_string(X,Y,number):
	return '_%.2fX_%.2fY_SymAxis%d'%(X,Y,number)



protein_pdb = sys.argv[1]
surface_pdb = 'K_sublattice.pdb'

''' Coordinates of C2 axes relative to origin in surface model '''
sublayer_C2_axes = [(0, 0), (2.60, 0.00), (1.30, 2.2525), (1.30, -2.2525)]

lattice_direction_a1 = numpy.array([5.2, 0])
lattice_direction_a2 = numpy.array([2.60, 4.5050])

for i, C2_axis in enumerate(sublayer_C2_axes):
	axis_X = C2_axis[0]
	axis_Y = C2_axis[1]
	sym_axis_number = i+1

	# .format(axis_X.round3)
	print translate_surface.format(surface_pdb, axis_X, axis_Y, ((axis_X**2)+(axis_Y**2))**0.5, format_coordinate_string(axis_X, axis_Y, sym_axis_number))

	for a1 in range(-4,4):
		for a2 in range(-4,4):
			lattice_translation = (a1 * lattice_direction_a1) + (a2 * lattice_direction_a2)
			lattice_X = lattice_translation[0]
			lattice_Y = lattice_translation[1]

			combined_X = axis_X + lattice_X 
			combined_Y = axis_Y + lattice_Y
			combined_distance = ((combined_X**2)+(combined_Y**2))**0.5

			print poly_ala_c2.format(protein_pdb, combined_X, combined_Y, combined_distance, format_coordinate_string(combined_X, combined_Y, sym_axis_number) )
			print full_atom_c2.format(protein_pdb, combined_X, combined_Y, combined_distance, format_coordinate_string(combined_X, combined_Y, sym_axis_number) )


