#! /usr/bin/env python

import sys
import re

import pyrosetta 
pyrosetta.init(extra_options = "-mute all")
from pyrosetta.rosetta.protocols import grafting 

number_trimmed = 12

def trim_and_dump_one_pdb(pdb):
    # try:
    Pose = pyrosetta.pose_from_pdb(pdb)

    n_residue = Pose.size()
    
    global number_trimmed

    for trim in range(1,number_trimmed+1):
        pdb_ntrim = re.sub(r'(.*).pdb', r'\1_trim{0}.pdb', pdb).format(trim)

        pose_ntrim = grafting.return_region(Pose, 1+trim, n_residue)
  
        pose_ntrim.pdb_info(pyrosetta.rosetta.core.pose.PDBInfo( pose_ntrim ))
        
        pose_ntrim.dump_pdb(pdb_ntrim)

pdbs = sys.argv[1:]

for pdb in pdbs:
    trim_and_dump_one_pdb(pdb)



