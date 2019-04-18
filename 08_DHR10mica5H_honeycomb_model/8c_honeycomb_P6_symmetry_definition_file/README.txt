
Run Rosetta Scripts to generate dimers-of-trimers for honeycomb-like C2s with commands in:
rosetta_scripts_make_trimer_dimers.txt


In pymol load DHR10mica5H_trimer_honeycomb_C2_repack_9.10X_6.76Y_SymAxis3_0001.pdb 

select chains in one trimer and copy to new object ('obj01')

select chains in second trimer and copy to new object ('obj02')

At the pymol command prompt run /07_DHR10mica5H_incorrect_tile_model/7e_P6_layer_symmetry_definition_file/unit_cell.py

At the pymol command prompt type: 
p6('obj01', 'obj02')

this print a crystal symmetry line for a pdb:
CRYST1  202.667  202.667  999.000  90.00  90.00 120.00 P 6           2


Save one protein chain of the translated dimer-of-trimers (DHR10mica5H_honeycomb_9.10X_6.76Y_S3_p6.pdb)

Copy/paste crystal symmetry line into this new pdb file. You can test the symmetry by using 'generate symmetry mates' 


use Rosetta/main/source/src/apps/public/symmetry/make_symmdef_file.pl

with arguments:

make_symmdef_file.pl -m CRYST -p DHR10mica5H_honeycomb_9.10X_6.76Y_S3_p6.pdb > DHR10mica5H_honeycomb_9.10X_6.76Y_S3_p6.sym


this makes a symmetry definition file for a P6 lattice with this trimer and dimer interface


process repeated for alternative C2 interfaces
