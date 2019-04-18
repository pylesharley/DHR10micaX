#! /usr/bin/env python

# This pymol script generates CRYST lines for pdbs with p6 symmetry from a dimer-of-trimers input pdb.
# It was shared by Tim Craven and Will Sheffler, who both agreed to its inclusion here.

# importing from Will's pymol_util and xyzMath modules
from pymol_util import alignaxis, trans, com, rotz
from xyzMath import Vec
import numpy as np

# this function is from Tim Craven
def p6(c3a,c3b):
    ''' prep unit cell for P6 propogation '''
    c3a_com = com(c3a)
    c3b_com = com(c3b)

    center = (c3b_com+c3a_com) / 2
    center_tuple = center.tuple()
    xy_center = [center_tuple[0], center_tuple[1], 0.0]
    # print 'xy_center', xy_center
    # print 'np.linalg.norm(xy_center)', np.linalg.norm(xy_center)
    if np.linalg.norm(xy_center) > 0.00001:
        'move to origin'
        trans(c3a, -Vec(xy_center) )
        trans(c3b, -Vec(xy_center) )
    else:
        'close enough'
    c3a_com = com(c3a).tuple()
    c3b_com = com(c3b).tuple()
    c3_dist = ( np.abs(c3a_com[0]-c3b_com[0])**2 + np.abs(c3a_com[1]-c3b_com[1])**2 ) **0.5

    ### Angle between c3 centers must be 30 degrees
    ## 30, 60 degrees
    ## 0.523599, 1.5708
    angle_to_c3a = np.arctan( c3a_com[1]/c3a_com[0] )
    # print np.degrees(angle_to_c3a), 'np.degrees(angle_to_c3a)'
    angle_correction = float(np.degrees(angle_to_c3a - 0.523599))

    # print angle_correction,'angle_correction'
    rotz(c3a, -1*angle_correction)
    rotz(c3b, -1*angle_correction)

    ### one of c3 centers must be along y-axis
    c3a_com = com(c3a)
    c3b_com = com(c3b)        
    # print 'c3_dist', c3_dist
    # disp_to_c3a = Vec(0.0, float(c3_dist), 0.0) - c3a_com
    # disp_to_c3b = Vec(0.0, float(c3_dist), 0.0) - c3b_com

    if c3a_com.tuple()[1] > c3b_com.tuple()[1]:
        # print 'A'
        displacement = (Vec(0.0, float(c3_dist), 0.0) - c3a_com).tuple()
    else:
        # print 'B'
        displacement = (Vec(0.0, float(c3_dist), 0.0) - c3b_com).tuple()
    displacement = Vec([displacement[0],displacement[1],0.0])
    
    trans(c3a, displacement)
    trans(c3b, displacement)      

    # print 'c3_dist', c3_dist
    unit_cell = c3_dist * 1.73205080756887729352744634150587236694280525381038062805580
    # print 'unit_cell', unit_cell
    CRYST1 = 'CRYST1{0}{0}  999.000  90.00  90.00 120.00 P 6           2'.format( str(unit_cell.round(3)).rjust(9) )
    print CRYST1



