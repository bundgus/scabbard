from scabbard import get_client
from datetime import datetime, timedelta


def test__v1_historical_flights_destination_seasonality_get():
    client = get_client()

    departuredate = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    returndate = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    seasonality = client.Air_Intelligence\
        .V1HistoricalFlightsDestinationSeasonalityGet(destination='DFW')\
        .result()
    assert 'DFW' == seasonality['DestinationLocation']
