from mpmath import mp, apery

mp.dps=109

print([int(z) for z in list(str(apery).replace('.', ''))[:-1]]) # Indranil Ghosh, Jul 08 2017 