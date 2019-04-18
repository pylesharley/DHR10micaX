#! /usr/bin/env python

import argparse
import torsions
import sys
import os
import re


def main(argv=None):
    if argv is None:
        argv = sys.argv 

    # instanciate argparse
    ArgParser = argparse.ArgumentParser(description='run_sicdock arg parser')
    # add args to argparse:
    ArgParser.add_argument('-tor', type = str, help = " list of backbone torison angles ", required = True )
    ArgParser.add_argument('-fas', type = str, help = " fasta file of amino acid sequence", required = True )
    args = ArgParser.parse_args()

    with open(args.fas, 'r') as render_fasta:
        render_lines = render_fasta.readlines()
        for i, line in enumerate( render_lines ):
            if line.startswith('>'):
                name = re.sub(r'>(.+)\n$', r'\1', line)
                seq = re.sub(r'(.+)\n$', r'\1', render_lines[i+1])
                submain(args_phi_psi=args.tor, args_seq=seq, args_name=name )


def submain(args_phi_psi=False, args_seq=False, args_name='render'):

    with open(args_phi_psi, 'r') as phi_psi:
        args_phi_psi = phi_psi.readlines()
    torsion_space_iterable = args_phi_psi


    PhiPsi = []

    if args_seq:
        if os.path.isfile(args_seq):
            with open(args_seq, 'r') as seq:
                args_seq = seq.readlines()
                args_seq = [ line for line in args_seq if len(line) ]
                if len(args_seq) == 1: args_seq = args_seq[0].strip()
        Seq = list(args_seq)
    else:
        Seq = []

    try:
        assert len(torsion_space_iterable) == len(Seq)
    except:
         print ('Sequence and torison iteratable must be same length\n', Seq, len(Seq),  torsion_space_iterable, len(torsion_space_iterable))
         sys.exit()

    # 1st loop through backbone 
    for i, element in enumerate(torsion_space_iterable):
        element=element.strip()
        if len(element) == 1:
            try:
                phi, psi, omega = torsions.abego[element]
            except:
                print ('Cannot find torsions for abego element #%d: %s'%(i+1, element))
            
            if not args_seq:    AminoAcid = torsions.seq[ element ]
        
        else:
            try: 
                pieces = tuple( float(a) for a in element.split() )
                if len(pieces) == 2:
                    phi, psi = pieces
                    omega = 180
                else:
                    assert len(pieces) == 3
                    phi, psi, omega = pieces
            except:
                print ('Having problem with line %d:\n%s'%(i+1, element))
            

        PhiPsi.append( (phi, psi, omega) )
        if not args_seq:
            Seq.append(AminoAcid)

    assert len(PhiPsi) == len(Seq)

    try:
        pyrosetta
    except NameError:
        import pyrosetta
        pyrosetta.init()

    render_pose = pyrosetta.pose_from_sequence( ''.join(Seq) )

    for i, torsion_angles in enumerate(PhiPsi):
        phi, psi, omega = torsion_angles
        p = i+1
        render_pose.set_phi(p, phi)
        render_pose.set_psi(p, psi)
        render_pose.set_omega(p, omega)

    render_pose.dump_pdb( '%s.pdb'%args_name )


if __name__ == "__main__":
  sys.exit( main() )