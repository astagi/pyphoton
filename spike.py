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

