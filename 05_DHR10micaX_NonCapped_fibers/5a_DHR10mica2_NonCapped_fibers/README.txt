
Open low energy model from 04_DHR10mica18_NonCapped in pymol (example: 04_DHR10mica18_NonCapped/low_energy_model/DHR10mica18_NonCapped_on_mica_4Y_0001.pdb)

Enter at pymol command prompt:
alter chain B and resi 101-200, chain='C'
alter chain B and resi 201-300, chain='D'
alter chain B and resi 301-400, chain='E'

remove chain B and resi 401-900

Save as new pdb file, this will be the input pdb. Make sure chains are in right order in pdb
example: DHR10mica2NC_fiber_on_Ksublayer.pdb
