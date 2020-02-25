import json
import requests

from .errors import PhotonException
from .location import Location
from .point import Point


class Photon:

    def __init__(
            self,
            host='https://photon.komoot.de',
            language='en'
    ):
        self._host = host.strip('/')
        self._language = language

    def _execute_query(self, q, limit, lat, lon, lang):
        params = locals().items()
        parameters_query = '&'.join(
            [
                '{0}={1}'.format(k, v) for k, v in params if v and k != 'self'
            ]
        )
        response = requests.get("{0}/api/?{1}".format(self._host, parameters_query))
        if response.status_code != 200:
            try:
                json_response = response.json()
            except json.decoder.JSONDecodeError:
                json_response = {'message': 'Error ' + str(response.status_code)}
            raise PhotonException(json_response['message'].capitalize())
        return response.json()

    def _transform_location(self, location):
        new_location = Location()
        location_point = Point(
            location['geometry']['coordinates'][0],
            location['geometry']['coordinates'][1]
        )
        setattr(new_location, '_point', location_point)
        for property_name, property_value in location['properties'].items():
            if property_name == 'extent':
                extent_from = Point(
                    property_value[0],
                    property_value[1]
                )
                extent_to = Point(
                    property_value[2],
                    property_value[3]
                )
                setattr(new_location, 'extent_from', extent_from)
                setattr(new_location, 'extent_to', extent_to)
            else:
                setattr(new_location, property_name, property_value)
        return new_location

    def query(self, query, limit=None, latitude=None, longitude=None, language=None):
        if not language:
            language = self._language
        resp = self._execute_query(query, limit, latitude, longitude, language)
        if limit == 1 and len(resp['features']):
            return self._transform_location(resp['features'][0])
        transformed_locations = []
        for location in resp['features']:
            transformed_locations.append(self._transform_location(location))
        return transformed_locations
