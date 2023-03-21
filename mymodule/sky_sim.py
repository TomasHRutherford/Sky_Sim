# Determine Andromeda location in ra/dec degrees
import random
import math
import argparse
# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'
NSRC = 1_000_000

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

def gen_pos(NSRC, ra, dec):
    """
    Generates the positions of stars around the centre of Andromeda,
    with a maximum of 1 degree offset in x and y.
    """
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return ras, decs

def save_file(ras, decs):
    """
    Saves our star positions as a csv file.
    """
    f = open('catalog.csv','w')
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.  

    Hours/degrees/seconds values are taken from wikipedia.

    Returns
    -------
    ra:float  
    &emsp;    The position of the centre of Andromeda on the sky in Right Ascension, given in degrees.  
    dec:float  
    &emsp;    The position of the centre of Andromeda on the sky in Declination, given in degrees.  
    """
    # from wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'

    d, m, s = andromeda_dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = andromeda_ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    return ra,dec

if __name__ == "__main__":
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    
    ras, decs = gen_pos(NSRC,ra,dec)
    # now write these to a csv file for use by my other program
    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")



