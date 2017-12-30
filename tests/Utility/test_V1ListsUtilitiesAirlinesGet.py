from scabbard import get_client


def test__v1_lists_utilities_airlines_get():
    client = get_client()

    airline = client.Utility\
        .V1ListsUtilitiesAirlinesGet(airlinecode='B6')\
        .result()
    assert 'Jetblue Airways Corporation' == airline['AirlineInfo'][0]['AirlineName']
