from scabbard import get_client
from datetime import datetime, timedelta


def test__v1_historical_shop_flights_fares_get():
    client = get_client()

    departuredate = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    returndate = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    forecast = client.Air_Intelligence\
        .V1HistoricalShopFlightsFaresGet(origin='JFK',
                                         destination='LAX',
                                         departuredate=departuredate,
                                         returndate=returndate,
                                         pointofsalecountry='US'
                                         )\
        .result()
    assert 'JFK' == forecast['OriginLocation']
