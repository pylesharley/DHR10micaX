#! /usr/bin/env python


sample_c3 = '''/EXECUTABLE_PATH/rosetta_scripts.static.linuxgccrelease -database /DATABASE_PATH/database  @rosetta_scripts.flag -s {0} -scorefile score.sc  -parser:script_vars translate_X={1} translate_Y={2} distance={3} -suffix {4} -parser:protocol DHR10micaX_c3_scan.xml'''

translate_surface = '''/EXECUTABLE_PATH/rosetta_scripts.static.linuxgccrelease -database /DATABASE_PATH/database  -s {0} -scorefile surface.sc -parser:script_vars axis_X={1} axis_Y={2} distance={3} -suffix _{4} -parser:protocol translate_surface.xml -nstruct 1 -beta -mute all'''

import numpy
import sys


def format_coordinate_string(X,Y,number):
	return '_%.2fX_%.2fY_SymAxis%d'%(X,Y,number)


protein_pdbs = sys.argv[1:]
surface_pdb = 'K_sublattice.pdb'

''' Coordinates of C3 axes relative to origin in surface model (K_sublattice.pdb)'''
sublayer_C3_axes = [(0, 0), (2.600000,1.501667), (2.600000,-1.501667)]

lattice_direction_a1 = numpy.array([5.2, 0])
lattice_direction_a2 = numpy.array([2.60, 4.5050])

with open('DHR10micaX_c3_scan.list', 'w') as command_list:

	for i, C3_axis in enumerate(sublayer_C3_axes):
		axis_X = C3_axis[0]
		axis_Y = C3_axis[1]
		sym_axis_number = i+1

		print>>command_list, translate_surface.format(surface_pdb, axis_X, axis_Y, ((axis_X**2)+(axis_Y**2))**0.5, format_coordinate_string(axis_X, axis_Y, sym_axis_number))

		for protein_pdb in protein_pdbs:

			for a1 in range(-3,4): # 0 +- 3 steps
				for a2 in range(-3,4):
					lattice_translation = (a1 * lattice_direction_a1) + (a2 * lattice_direction_a2)
					lattice_X = lattice_translation[0]
					lattice_Y = lattice_translation[1]

					combined_X = axis_X + lattice_X 
					combined_Y = axis_Y + lattice_Y
					combined_distance = ((combined_X**2)+(combined_Y**2))**0.5

					print>>command_list, sample_c3.format(protein_pdb, combined_X, combined_Y, combined_distance, format_coordinate_string(combined_X, combined_Y, sym_axis_number) )

