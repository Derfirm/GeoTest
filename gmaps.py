import googlemaps
from datetime import datetime
_gmaps = googlemaps.Client(key="api_key")

Geocoding and address
geocode_result = _gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print geocode_result
# Look up an address with reverse geocoding
reverse_geocode_result = _gmaps.reverse_geocode((40.714224, -73.961452))
print reverse_geocode_result
# Request directions via public transit
now = datetime.now()
directions_result = _gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print directions_result