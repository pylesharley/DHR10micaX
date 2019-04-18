The following pdbs are from /9d_DHR10micaXH_honeycomb_P6_layer/low_energy_model/ :
DHR10mica3H_honeycomb_P6_1G_0033.pdb
DHR10mica4H_honeycomb_P6_2S_0002.pdb
DHR10mica6H_honeycomb_P6_1F_0015.pdb
DHR10mica7H_honeycomb_P6_1A_0005.pdb


Ran the following commands in bash:
grep "ATOM.\{17\}A" DHR10mica3H_honeycomb_P6_1G_0033.pdb > DHR10mica3H_repacked_honeycomb_P6.pdb
grep "ATOM.\{17\}A" DHR10mica4H_honeycomb_P6_2S_0002.pdb > DHR10mica4H_repacked_honeycomb_P6.pdb
grep "ATOM.\{17\}A" DHR10mica6H_honeycomb_P6_1F_0015.pdb > DHR10mica6H_repacked_honeycomb_P6.pdb
grep "ATOM.\{17\}A" DHR10mica7H_honeycomb_P6_1A_0005.pdb > DHR10mica7H_repacked_honeycomb_P6.pdb

grep CRYST DHR10mica3H_honeycomb_P6.pdb >> DHR10mica3H_repacked_honeycomb_P6.pdb 
grep CRYST DHR10mica4H_honeycomb_P6.pdb >> DHR10mica4H_repacked_honeycomb_P6.pdb 
grep CRYST DHR10mica6H_honeycomb_P6.pdb >> DHR10mica6H_repacked_honeycomb_P6.pdb 
grep CRYST DHR10mica7H_honeycomb_P6.pdb >> DHR10mica7H_repacked_honeycomb_P6.pdb 


In pymol, symmetry mates were generated from these repacked P6 pdbs, and hexamers were combined with their corresponding K sublayer pdb

This produced:
DHR10mica3H_repacked_honeycomb_hexamer_on_Ksublayer.pdb
DHR10mica4H_repacked_honeycomb_hexamer_on_Ksublayer.pdb
DHR10mica6H_repacked_honeycomb_hexamer_on_Ksublayer.pdb
DHR10mica7H_repacked_honeycomb_hexamer_on_Ksublayer.pdb

