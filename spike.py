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

print ("\n🔍 Looking for locations around Berlin with location_bias_scale=2\n")
locations = client.query('berlin', latitude=52, longitude=10, location_bias_scale=2)
for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))

print ("\n🔍 Looking for locations around Berlin that are town and villages\n")
locations = client.query('berlin', osm_tags=['place:town', 'place:village'])
for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))

print ("\n🔍 Looking for locations inside a bounding box\n")
locations = client.query('berlin', bbox=(9.5,51.5,11.5,53.5))
for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))

print ("\n🔍 Looking for locations around (52, 10) using reverse \n")
locations = client.reverse(latitude=52, longitude=10)
for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))
