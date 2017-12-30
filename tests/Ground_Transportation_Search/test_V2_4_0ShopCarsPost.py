from scabbard import get_client
import json

def test__v2_4_0_shop_cars_post():
    client = get_client()

    j = json.loads('''{
                            "OTA_VehAvailRateRQ": {
                              "VehAvailRQCore": {
                                "QueryType": "Shop",
                                "VehRentalCore": {
                                  "PickUpDateTime": "04-07T09:00",
                                  "ReturnDateTime": "04-08T11:00",
                                  "PickUpLocation": {
                                    "LocationCode": "DFW"
                                  }
                                }
                              }
                            }
                        }''')

    available_vehicles = client.Ground_Transportation_Search\
        .V2_4_0ShopCarsPost(caravailabilityrequest=j
                            )\
        .result()
    assert 5 == len(available_vehicles['OTA_VehAvailRateRS']['Version'])
    print()
    print(available_vehicles['OTA_VehAvailRateRS']['Version'])

