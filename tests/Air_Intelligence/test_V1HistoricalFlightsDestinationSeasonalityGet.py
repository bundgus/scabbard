from scabbard import get_client
from datetime import datetime, timedelta


def test__v1_historical_flights_destination_seasonality_get():
    client = get_client()

    seasonality = client.Air_Intelligence\
        .V1HistoricalFlightsDestinationSeasonalityGet(destination='DFW')\
        .result()
    assert 'DFW' == seasonality['DestinationLocation']
