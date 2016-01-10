import sys
from geopy.geocoders import Nominatim
geolocator = Nominatim()
address = sys.argv[1]
location = geolocator.geocode(address)
print(location.address)
print((location.latitude, location.longitude))
#print(location.raw)