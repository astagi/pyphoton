import pytest

from pyphoton import Photon
from pyphoton.errors import PhotonException


def test_client_simple_request(requests_mock):

    client = Photon()
    expected_json = {
        "features": [
            {
                "geometry": {
                    "coordinates": [
                        13.3888599,
                        52.5170365
                    ],
                    "type": "Point"
                },
                "type": "Feature",
                "properties": {
                    "osm_id": 240109189,
                    "osm_type": "N",
                    "country": "Germany",
                    "osm_key": "place",
                    "city": "Berlin",
                    "osm_value": "city",
                    "postcode": "10117",
                    "name": "Berlin",
                    "state": "Berlin"
                }
            }
        ],
        "type": "FeatureCollection"
    }
    requests_mock.get('https://photon.komoot.de/api/?q=berlin&limit=1&lang=en', json=expected_json)
    location = client.query('berlin', limit=1)

    assert location.longitude == 13.3888599
    assert location.latitude == 52.5170365
    assert location.osm_id == 240109189
    assert location.city == "Berlin"
    assert str(location) == "Berlin\n(52.5170365, 13.3888599)\ncity: Berlin\npostcode: 10117\nstate: Berlin\nosm_id: 240109189\nosm_type: N\nosm_key: place\nosm_value: city"


def test_client_simple_request_with_extent(requests_mock):

    client = Photon()
    expected_json = {
        "features": [
            {
                "geometry": {
                    "coordinates": [
                        12.493087103595503,
                        41.8902614
                    ],
                    "type": "Point"
                },
                "type": "Feature",
                "properties": {
                    "osm_id": 1834818,
                    "osm_type": "R",
                    "extent": [
                        12.4913001,
                        41.8909127,
                        12.4934472,
                        41.8896078
                    ],
                    "country": "Italy",
                    "osm_key": "tourism",
                    "city": "Rome",
                    "street": "Piazza del Colosseo",
                    "osm_value": "attraction",
                    "postcode": "00184",
                    "name": "Colosseum",
                    "state": "Lazio"
                }
            }
        ],
        "type": "FeatureCollection"
    }
    requests_mock.get('https://photon.komoot.de/api/?q=Colosseum&limit=1&lang=en', json=expected_json)
    location = client.query('Colosseum', limit=1)

    assert location.longitude == 12.493087103595503
    assert location.latitude == 41.8902614
    assert location.extent_from.longitude == 12.4913001
    assert location.extent_from.latitude == 41.8909127
    assert location.extent_to.longitude == 12.4934472
    assert location.extent_to.latitude == 41.8896078



def test_client_simple_request_with_no_limits(requests_mock):

    client = Photon()
    expected_json = {
        "features": [
            {
                "geometry": {
                    "coordinates": [
                        13.3888599,
                        52.5170365
                    ],
                    "type": "Point"
                },
                "type": "Feature",
                "properties": {
                    "osm_id": 240109189,
                    "osm_type": "N",
                    "country": "Germany",
                    "osm_key": "place",
                    "city": "Berlin",
                    "osm_value": "city",
                    "postcode": "10117",
                    "name": "Berlin",
                    "state": "Berlin"
                }
            },
            {
                "geometry": {
                    "coordinates": [
                        12.493087103595503,
                        41.8902614
                    ],
                    "type": "Point"
                },
                "type": "Feature",
                "properties": {
                    "osm_id": 1834818,
                    "osm_type": "R",
                    "extent": [
                        12.4913001,
                        41.8909127,
                        12.4934472,
                        41.8896078
                    ],
                    "country": "Italy",
                    "osm_key": "tourism",
                    "city": "Rome",
                    "street": "Piazza del Colosseo",
                    "osm_value": "attraction",
                    "postcode": "00184",
                    "name": "Berlin Colosseum",
                    "state": "Lazio"
                }
            }
        ],
        "type": "FeatureCollection"
    }
    requests_mock.get('https://photon.komoot.de/api/?q=berlin&lang=en', json=expected_json)
    locations = client.query('berlin')

    assert locations[0].longitude == 13.3888599
    assert locations[0].latitude == 52.5170365
    assert locations[0].name == "Berlin"
    assert str(locations[0]._point) == "(52.5170365, 13.3888599)"

    assert locations[1].longitude == 12.493087103595503
    assert locations[1].latitude == 41.8902614
    assert locations[1].name == 'Berlin Colosseum'


def test_errors(requests_mock):

    client = Photon()
    requests_mock.get(
        'https://photon.komoot.de/api/?q=berlin&limit=1&lang=en',
        json={'message' : "missing search term 'q': /?q=berlin"},
        status_code=400
    )
    with pytest.raises(PhotonException):
        location = client.query('berlin', limit=1)


    requests_mock.get(
        'https://photon.komoot.de/api/?q=berlin&limit=1&lang=en',
        status_code=500
    )
    with pytest.raises(PhotonException):
        location = client.query('berlin', limit=1)
