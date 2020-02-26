from pyphoton import Photon
from pyphoton.errors import PhotonException


client = Photon()

print ("\n🔍 Looking for Berlin..\n")

location = client.query('berlin', limit=1)
print (location)

print ("\n🔍 Looking for the Colosseum..\n")
location = client.query('Colosseum', limit=1)
print (location)

print ("\n🔍 Trying to make a bad request (empty query)..\n")
try:
    location = client.query('', limit=1)
except PhotonException as ex:
    print (ex)

print ("\n🔍 Looking for locations arount berling with location_bias_scale=2\n")
locations = client.query('berlin', latitude=52, longitude=10, location_bias_scale=2)

for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))
