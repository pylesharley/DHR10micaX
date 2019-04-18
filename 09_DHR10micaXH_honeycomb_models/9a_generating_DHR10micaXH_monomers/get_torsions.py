#! /usr/bin/env python

import sys

import pyrosetta
# import pyrosetta.rosetta

pyrosetta.init(extra_options = "-mute all ")

# print Pose
def get_torisions(Pose):
	for resi in range( Pose.size() ):
		resi += 1
		yield Pose.phi(resi), Pose.psi(resi), Pose.omega(resi) 


def main(argv=None):
	if argv is None:
		argv = sys.argv	

	Pose = pyrosetta.pose_from_pdb(argv[1])

	if len(argv) > 2:		
		with open(argv[2], 'w') as output_file:
			for position in get_torisions(Pose):
				print>>output_file, '\t'.join([ str(x) for x in position ])

	else:
		for position in get_torisions(Pose):
			print ('\t'.join([ str(x) for x in position ]))


if __name__ == "__main__":
	sys.exit(main())