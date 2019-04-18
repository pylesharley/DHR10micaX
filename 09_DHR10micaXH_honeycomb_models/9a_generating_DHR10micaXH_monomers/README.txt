DHR10mica5_monomer_Ctrim_38E_0001_1L_0026.pdb from /07_DHR10mica5H_incorrect_tile_model/7c_loop_relax/low_energy_model/ renamed as DHR10mica5H_monomer.pdb

Get sequence and backbone torsion angles from DHR10mica5H_monomer.pdb:

./pdb_sequence.py DHR10mica5H_monomer.pdb > DHR10mica5H_monomer.fas

./get_torsions.py DHR10mica5H_monomer.pdb > DHR10mica5H_monomer_bb_torsions.txt

Add and remove internal repeats (residues 49-98 and 99-148) from DHR10mica5H_monomer.fas for DHR10mica3H, DHR10mica4H, DHR10mica6H and DHR10mica7H. Make sure sequence name following > in fasta file is changed too, as this will be applied to a pdb later.

This results in:
DHR10mica3H_monomer.fas
DHR10mica4H_monomer.fas
DHR10mica6H_monomer.fas
DHR10mica7H_monomer.fas


Likewise, add and remove internal repeats (lines 49-98 and 99-148) from DHR10mica5H_monomer_bb_torsions.txt for DHR10mica3H, DHR10mica4H, DHR10mica6H and DHR10mica7H.

this results in:
DHR10mica3H_monomer_bb_torsions.txt
DHR10mica4H_monomer_bb_torsions.txt
DHR10mica5H_monomer_bb_torsions.txt
DHR10mica6H_monomer_bb_torsions.txt
DHR10mica7H_monomer_bb_torsions.txt


Use sequence and torsion files to produce new pdbs:

python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas
python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas
python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas
python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas
python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas
python ./generate_backbone.py -tor  DHR10mica3H_monomer_bb_torsions.txt -fas DHR10mica3H_monomer.fas


this yields:

DHR10mica3H_monomer.pdb
DHR10mica4H_monomer.pdb
DHR10mica5H_monomer.pdb
DHR10mica6H_monomer.pdb

