from scabbard import get_client
import json


def test__v1_lists_utilities_geocode_locations_post():
    client = get_client()

    j = json.loads('''[{
                        "GeoCodeRQ": {
                            "PlaceById": {
                                "Id": "DFW",
                                "BrowseCategory": {
                                    "name": "AIR"
                                }
                            }
                        }
                    }]'''
                   )

    geographic_information = client.Utility\
        .V1ListsUtilitiesGeocodeLocationsPost(geocoderequest=j)\
        .result()
    assert 'DFW' == geographic_information['Results'][0]['GeoCodeRS']['Place'][0]['Id']
