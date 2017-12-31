from scabbard import get_client


def test__v1_lists_utilities_geoservices_autocomplete_get():
    client = get_client()

    geo = client.Utility\
        .V1ListsUtilitiesGeoservicesAutocompleteGet(query='Dall')\
        .result()

    assert 0 < geo['Response']['grouped']['category:CITY']['doclist']['numFound']
