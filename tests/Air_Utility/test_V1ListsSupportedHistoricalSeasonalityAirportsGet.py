from scabbard import get_client


def test__v1_lists_supported_countries_get():
    client = get_client()

    # Africa,Asia Pacific,Europe,Latin America,Middle East,North America
    travel_seasonality_destinations = (
                 client.Air_Utility
                 .V1ListsSupportedHistoricalSeasonalityAirportsGet(
                                                                   country='AE',
                                                                   region='Middle East')
                 .result()
                 )

    # entry for country=AE and region=Middle East should be DXB
    airport_code = (travel_seasonality_destinations['DestinationLocations'][0]
                    ['DestinationLocation']['AirportCode'])
    assert 'DXB' == airport_code
