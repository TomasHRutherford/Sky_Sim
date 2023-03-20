# Determine Andromeda location in ra/dec degrees
import random
import math
# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.
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

def gen_pos(nrsrc, ra, dec):
    ras = []
    decs = []
    for i in range(nsrc):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return ras, decs

def save_file(ras, decs):
    f = open('catalog.csv','w')
    print("id,ra,dec", file=f)
    for i in range(nsrc):
        print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

ra, dec = get_radec()

nsrc = 1_000_000
ras, decs = gen_pos(nsrc, ra, dec)
save_file(ras, decs)
