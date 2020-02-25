from pyphoton import Photon

client = Photon()
location = client.query('berlin', limit=1)
print (location.city)
print (location.latitude)
print (location.longitude)
feature = client.query('Colosseum', limit=1)
