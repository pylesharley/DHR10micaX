 

DHR10mica5H_trimer_-2.60X_1.50Y_SymAxis2_TrimerInterface_S5_0013.pdb is from /07_DHR10mica5H_incorrect_tile_model/7d_trimer_with_loop_replacement/low_energy_model


DHR10mica5H_trimer_-2.60X_1.50Y_SymAxis2_TrimerInterface_S5_0013.pdb was translated to sample C2 interfaces between the C-terminal repeat and saved as:
'DHR10mica5H_monomer_honeycomb_C2_scan.pdb'


Python script generates lattice-matched translations and makes Rosetta scripts commands for screening for surface-compatable dimers:

DHR10mica5H_honeycomb_C2_scan.py DHR10mica5H_monomer_honeycomb_C2_scan.pdb > DHR10mica5H_honeycomb_C2_scan.list

Dimers are screened with full sequence and as poly-alanine backbone. Translations producing C2 docks with a non-zero ddg under 1000 REU were selected for further modeling (pdbs are in /selected_dimer_translations/ )

