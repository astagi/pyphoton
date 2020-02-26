from pyphoton import Photon
from pyphoton.errors import PhotonException


client = Photon()
location = client.query('berlin', limit=1)
print (location.city)
print (location.latitude)
print (location.longitude)
location = client.query('Colosseum', limit=1)
try:
    location = client.query('', limit=1)
except PhotonException as ex:
    print (ex)

locations = client.query('berlin', latitude=52, longitude=10, location_bias_scale=2)

for location in locations:
    print ('🌉 Location #{0}\n{1}\n'.format(location.osm_id, location))
