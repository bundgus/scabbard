from scabbard import get_client
from datetime import datetime, timedelta


def test__v1_historical_flights_fares_get():
    client = get_client()

    earliestdeparturedate = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    latestdeparturedate = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    forecast = client.Air_Intelligence\
        .V1HistoricalFlightsFaresGet(origin='JFK',
                                     destination='LAX',
                                     earliestdeparturedate=earliestdeparturedate,
                                     latestdeparturedate=latestdeparturedate,
                                     lengthofstay=4
                                     )\
        .result()
    assert 'JFK' == forecast['OriginLocation']
