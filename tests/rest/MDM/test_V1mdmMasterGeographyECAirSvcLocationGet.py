from scabbard import get_client


def test__v1_mdm_master_geography_ec_air_svc_location_get():
    client = get_client()

    locations = client.MDM \
        .V1_mdmMasterGeographyECAirSvcLocationGet() \
        .result()
    print(locations)
    #assert 'Jetblue Airways Corporation' == airline['AirlineInfo'][0]['AirlineName']