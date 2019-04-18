
Uses DHR10_on_mica4_surface_thread_2V_0001.pdb output from 01_DHR10mica4


python2.7 ./pdb_sequence.py DHR10_on_mica4_surface_thread_2V_0001.pdb > DHR10_mica4.fas

Open fasta in text editor (like Sublime Text)

Copy sequence of residues 51-150, move cursor to inbetween residue 150 and 151 and paste sequence seven times (total sequence length should be 900)

Change sequence name to "DHR10_mica18" and save modified fasta file as DHR10_mica18.fas 


python2.7 ./get_torsions.py DHR10.pdb > DHR10_torsions.tsv 

Open DHR10_torsions.tsv in text editor

Copy lines 101-150 and paste 18 times in a new file (DHR10_18repeat_torsions.tsv)



python2.7 ./generate_backbone.py -fas DHR10_mica18.fas -tor DHR10_18repeat_torsions.tsv 

This will create a new pdb named after the sequence in the fasta ( DHR10_mica18.pdb )