from scabbard import get_client


def test__v1_lists_supported_shop_flights_originsdestinations_get():
    client = get_client()

    # Africa,Asia Pacific,Europe,Latin America,Middle East,North America
    origins_destinations = (
        client.Air_Utility
        .V1ListsSupportedShopFlightsOriginsdestinationsGet(
            origincountry='US',
            destinationcountry='US',
            originregion='North America',
            destinationregion='North America',
            pointofsalecountry='US'
        )
        .result()
    )

    # entry for country=AE and region=Middle East should be DXB
    destination_airport_code = (origins_destinations['OriginDestinationLocations'][0]
                                                    ['DestinationLocation']['AirportCode'])
    assert 'MCO' == destination_airport_code
