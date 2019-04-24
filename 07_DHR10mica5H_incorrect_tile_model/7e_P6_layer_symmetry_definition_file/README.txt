
DHR10mica5_trimer_tile_-1.30X_2.25Y_SymAxis4_0001.pdb is from /7a_translate_and_dimerize_on_lattice/selected_dimer_interface/

In pymol load DHR10mica5_trimer_tile_-1.30X_2.25Y_SymAxis4_0001.pdb 

select chains in one trimer and copy to new object ('obj01')

select chains in second trimer and copy to new object ('obj02')

At the pymol command prompt run the unit_cell.py script by typing:
run /PATH/unit_cell.py
where 'PATH' is the location of unit_cell.py on your computer 

At the pymol command prompt type: 
p6('obj01', 'obj02')

this print a crystal symmetry line for a pdb:
CRYST1  120.966  120.966  999.000  90.00  90.00 120.00 P 6           2

Save one protein chain of the translated dimer-of-trimers (DHR10mica5_p6_monomer.pdb)

Copy/paste crystal symmetry line into this new pdb file. You can test the symmetry by using 'generate symmetry mates' 


use Rosetta/main/source/src/apps/public/symmetry/make_symmdef_file.pl

with arguments:

make_symmdef_file.pl -m CRYST -p DHR10mica5_p6_monomer.pdb > DHR10mica5_p6_tiling.sym


this makes a symmetry definition file for a P6 lattice with this trimer and dimer interface
