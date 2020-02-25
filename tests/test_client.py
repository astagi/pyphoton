
def test_client_simple_request(requests_mock):
    from pyphoton import Photon

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

    assert location.latitude == 13.3888599
    assert location.longitude == 52.5170365
    assert location.osm_id == 240109189
    assert location.city == "Berlin"


def test_client_simple_request_with_extent(requests_mock):
    from pyphoton import Photon

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

    assert location.latitude == 12.493087103595503
    assert location.longitude == 41.8902614
    assert location.extent_from.latitude == 12.4913001
    assert location.extent_from.longitude == 41.8909127
    assert location.extent_to.latitude == 12.4934472
    assert location.extent_to.longitude == 41.8896078



def test_client_simple_request_with_no_limits(requests_mock):
    from pyphoton import Photon

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

    assert locations[0].latitude == 13.3888599
    assert locations[0].longitude == 52.5170365
    assert locations[0].name == "Berlin"

    assert locations[1].latitude == 12.493087103595503
    assert locations[1].longitude == 41.8902614
    assert locations[1].name == 'Berlin Colosseum'
