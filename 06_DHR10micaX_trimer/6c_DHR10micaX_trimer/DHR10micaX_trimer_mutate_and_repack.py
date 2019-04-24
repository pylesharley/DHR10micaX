#! /usr/bin/env python


sample_c3 = '''/EXECUTABLE_PATH/rosetta_scripts.static.linuxgccrelease -database /DATABASE_PATH/database @rosetta_scripts.flag -s {0} -scorefile score.sc  -parser:script_vars translate_X={1} translate_Y={2} distance={3} -suffix {4} -parser:protocol DHR10micaX_trimer_mutate_and_repack.xml'''


import numpy
import sys

import pyrosetta
pyrosetta.init(extra_options='-mute all')


def format_coordinate_string(X,Y,number):
	return 

protein_pdbs = sys.argv[1:]

for protein_pdb in protein_pdbs:
	translate_X = -2.60
	translate_Y = 1.50
	sym_axis_number = 2
	distance = ((translate_X**2)+(translate_Y**2))**0.5

	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	for n in range(1,6):
		for l in alphabet:
			print sample_c3.format(protein_pdb, translate_X, translate_Y, distance, '_%.2fX_%.2fY_SymAxis%d_TrimerInterface_%s%d'%(translate_X,translate_Y,sym_axis_number,l,n) ) 
