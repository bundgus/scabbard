from scabbard import get_client
import json
import datetime


def test__v2_4_0_shop_cars_post():
    client = get_client()

    today = datetime.datetime.now()
    pickup_datetime = (today + datetime.timedelta(days=10)).strftime("%m-%dT%H:%M")
    return_datetime = (today + datetime.timedelta(days=11)).strftime("%m-%dT%H:%M")


    j = json.loads('''{
                            "OTA_VehAvailRateRQ": {
                              "VehAvailRQCore": {
                                "QueryType": "Shop",
                                "VehRentalCore": {
                                  "PickUpDateTime": "''' + pickup_datetime + '''",
                                  "ReturnDateTime": "''' + return_datetime + '''",
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


