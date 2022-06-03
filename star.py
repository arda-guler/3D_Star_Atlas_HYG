class star:
    def __init__(self, hyg, hip, hd, hr, gl, bf, proper, ra, dec, dist,
                 pmra, pmdec, rv, mag, absmag, spect, ci, x, y, z, vx, vy, vz,
                 rarad, decrad, pmrarad, prdecrad, bayer, flam, con, comp,
                 comp_primary, base, lum, var, var_min, var_max):

        self.hyg = hyg
        self.hip = hip
        self.hd = hd
        self.hr = hr
        self.gl = gl
        self.bf = bf
        self.ra = ra
        self.dec = dec
        self.proper = proper
        self.dist = dist
        self.pmra = pmra
        self.pmdec = pmdec
        self.rv = rv
        self.mag = mag
        self.absmag = absmag
        self.spect = spect
        self.ci = ci
        self.x = x
        self.y = y
        self.z = z
        self.pos = [x, y, z]
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.vel = [vx, vy, vz]
        self.rarad = rarad
        self.decrad = decrad
        self.skypos = [rarad, decrad]
        self.pmrarad = pmrarad
        self.prdecrad = prdecrad
        self.skyvel = [pmrarad, prdecrad]
        self.bayer = bayer
        self.flam = flam
        self.con = con
        self.comp = comp
        self.comp_primary = comp_primary
        self.base = base
        self.lum = lum
        self.var = var
        self.var_min = var_min
        self.var_max = var_max
        self.var_range = [var_min, var_max]

