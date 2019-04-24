#! /usr/bin/env python

relax_c2 = '''/EXECUTABLE_PATH/rosetta_scripts.static.linuxgccrelease -database /DATABASE_PATH/database @rosetta_scripts.flag -s {0} -scorefile score.sc  -parser:script_vars translate_X={1} translate_Y={2} distance={3} -suffix _relax{4} -parser:protocol DHR10mica5H_monomer_honeycomb_C2_interface_relax.xml'''

import numpy
import sys

def format_coordinate_string(X,Y,number):
	return '_%.2fX_%.2fY_SymAxis%d'%(X,Y,number)

protein_pdb = sys.argv[1]


# from /8a_screening_DHR10mica5H_honeycomb_C2_interfaces/selected_dimer_translations/selected_translations.txt
# (X, Y, SymAxis)
candidate_translations = [(11.70, 2.25, 3), (10.40, 0.00, 1), (3.90, 11.26, 4), (5.20, 9.01, 1), (2.60, 13.52, 1), (6.50, 6.76, 4), (14.30, -6.76, 4), (13.00, -4.50, 1), (9.10, 2.25, 4), (7.80, 4.50, 1), (11.70, -2.25, 4), (10.40, 4.50, 2), (3.90, 15.77, 3), (7.80, 9.01, 2), (9.10, 6.76, 3), (6.50, 11.26, 3), (15.60, -4.50, 2), (5.20, 13.52, 2), (3.90, 15.77, 3)]

for X, Y, sym_axis_number in candidate_translations:
		
		distance = ((X**2)+(Y**2))**0.5

		print relax_c2.format(protein_pdb, X, Y, distance, format_coordinate_string(X, Y, sym_axis_number) )


