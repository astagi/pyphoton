import json
import requests

from .errors import PhotonException
from .models import Location, Point


class Photon:

    def __init__(
            self,
            host='https://photon.komoot.io',
            language='en'
    ):
        self._host = host.strip('/')
        self._language = language

    def _execute_query(
                self,
                endpoint,
                q=None,
                limit=None,
                lat=None,
                lon=None,
                lang=None,
                location_bias_scale=None,
                osm_tag=None,
                bbox=None
    ):
        params = locals().items()
        query_parameters = [
            '{0}={1}'.format(k, v) for k, v in params if v and k not in ('self', 'endpoint', 'osm_tag', 'bbox')
        ]
        if osm_tag:
            if not isinstance(osm_tag, (list, set, tuple)):
                osm_tag = [osm_tag]
            for osm_tag_el in osm_tag:
                query_parameters.append('osm_tag={0}'.format(osm_tag_el))
        if bbox:
            if isinstance(bbox, (list, set, tuple)):
                bbox = ','.join(map(str, bbox))
            query_parameters.append('bbox={0}'.format(bbox))
        parameters_query = '&'.join(query_parameters)
        response = requests.get("{0}/{1}/?{2}".format(
            self._host, endpoint, parameters_query
        ))
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
            location['geometry']['coordinates'][1],
            location['geometry']['coordinates'][0]
        )
        setattr(new_location, '_point', location_point)
        for property_name, property_value in location['properties'].items():
            if property_name == 'extent':
                extent_from = Point(
                    property_value[1],
                    property_value[0]
                )
                extent_to = Point(
                    property_value[3],
                    property_value[2]
                )
                setattr(new_location, 'extent_from', extent_from)
                setattr(new_location, 'extent_to', extent_to)
            else:
                setattr(new_location, property_name, property_value)
        return new_location

    def query(
                self,
                query,
                limit=None,
                latitude=None,
                longitude=None,
                location_bias_scale=None,
                osm_tags=None,
                bbox=None,
                language=None,
    ):
        if not language:
            language = self._language
        resp = self._execute_query('api', query, limit, latitude, longitude, language, location_bias_scale, osm_tags, bbox)
        return self._transform_locations_from_resp(resp, limit)

    def reverse(
                self,
                latitude=None,
                longitude=None,
                limit=None,
                language=None,
    ):
        if not language:
            language = self._language
        resp = self._execute_query('reverse', limit=limit, lat=latitude, lon=longitude, lang=language)
        return self._transform_locations_from_resp(resp, limit)

    def _transform_locations_from_resp(self, resp, limit):
        if limit == 1 and len(resp['features']):
            return self._transform_location(resp['features'][0])
        transformed_locations = []
        for location in resp['features']:
            transformed_locations.append(self._transform_location(location))
        return transformed_locations
