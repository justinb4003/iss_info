import requests
from tletools import TLE
from sgp4.api import Satrec

tleurl = 'https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle'

rawtle = requests.get(tleurl).text
tle_lines = rawtle.strip().splitlines()
sat = Satrec.twoline2rv(tle_lines[1], tle_lines[2])
print((sat.alta * sat.radiusearthkm), (sat.altp * sat.radiusearthkm))
