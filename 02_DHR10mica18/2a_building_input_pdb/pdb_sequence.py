#! /usr/bin/env python
import sys, re

def GetFasta(PdbName):
    ThreeToOne = {'GLY':'G','ALA':'A','VAL':'V','LEU':'L','ILE':'I','MET':'M','PRO':'P','PHE':'F','TRP':'W','SER':'S','THR':'T','ASN':'N','GLN':'Q','TYR':'Y','CYS':'C','CYD':'C','LYS':'K','ARG':'R','HIS':'H','HIP':'H','ASP':'D','GLU':'E'}
    Pdb = open(PdbName, 'rU')
    PdbLines = Pdb.readlines()
    Pdb.close()
    FastaName = PdbName.replace('.pdb','')
    FastaName = re.sub(r'[\.\-\:\,\;]',r'_',FastaName)
    AminoAcids = []
    Res = 0
    for Line in PdbLines:
        if Line.startswith('ATOM'):
            Line = re.sub(r' +\n',r'',Line)
            Line = re.sub(r' +',r'|',Line)
            LineList = Line.split('|')
            if int(LineList[5]) > Res:
                Res = int(LineList[5])
                AminoAcids.append(ThreeToOne[LineList[3]])
    Seq = ''.join(AminoAcids)
    return FastaName, Seq


def main():
    if len(sys.argv) < 2:
        print '''usage:
        PdbSeq.py file.pdb (additional .pdbs) > Fasta.fas
        
        if two pdbs of same length provided bp file for conversions is exported'''

    Fasta = {}
    Names = []
    for PdbName in sys.argv[1:]:
        Name, Seq = GetFasta(PdbName)
        Fasta[Name] = Seq
        Names.append(Name)

    for Name in Names:
        print '>%s'%Name
        print Fasta[Name]


if __name__ == "__main__":
  sys.exit(main())
            