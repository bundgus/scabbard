from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_list_post():
    client = get_client()

    j = json.loads('''{
                        "GetHotelListRQ": {
                            "SearchCriteria": {
                                "IncludedFeatures": true, 
                                "HotelRefs": {
                                    "HotelRef": [
                                        {
                                            "HotelCode": "7521"
                                        }, 
                                        {
                                            "HotelCode": "22390"
                                        }, 
                                        {
                                            "HotelCode": "22570"
                                        }
                                    ]
                                }
                            }
                        }
                    }''')

    list = client.Hotel\
        .V1_0_0ShopHotelsListPost(gethotelslistrequest=j,
                                  mode='list'
                                  )\
        .result()

    assert 29 == len(list['GetHotelListRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
