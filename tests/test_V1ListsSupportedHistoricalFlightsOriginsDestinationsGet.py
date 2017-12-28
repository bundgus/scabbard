from scabbard import get_client


def test__v1_lists_supported_historical_flights_origins_destinations_get():
    client = get_client()

    # Africa,Asia Pacific,Europe,Latin America,Middle East,North America
    origins_destinations = (
        client.Air_Utility
            .V1ListsSupportedHistoricalFlightsOriginsDestinationsGet(
            origincountry='US',
            destinationcountry='US',
            originregion='North America',
            destinationregion='North America'
        )
            .result()
    )

    # entry for country=AE and region=Middle East should be DXB
    destination_airport_code = (origins_destinations['OriginDestinationLocations'][0]
    ['DestinationLocation']['AirportCode'])
    assert 'ATL' == destination_airport_code
