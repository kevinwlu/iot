import sys
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
coordinates = sys.argv[1]
location = geolocator.reverse(coordinates)
print(location.address)
print((location.latitude, location.longitude))
#print(location.raw)
