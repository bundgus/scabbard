from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_description_post():
    client = get_client()

    j = json.loads('''{
                        "GetHotelDescriptiveInfoRQ": {
                            "HotelRefs": {
                                "HotelRef": [{
                                    "HotelCode": "11111"
                                }]
                            },
                            "DescriptiveInfoRef": {
                                "PropertyInfo": true,
                                "LocationInfo": true,
                                "Amenities": true,
                                "Descriptions": {
                                    "Description": [{
                                        "Type": "Dining"
                                    }]
                                },
                                "Airports": true,
                                "AcceptedCreditCards": true
                            }
                        }
                    }''')

    description = client.Hotel\
        .V1_0_0ShopHotelsDescriptionPost(gethoteldescriptionrequest=j,
                                         mode='description'
                                         )\
        .result()

    assert 29 == len(description['GetHotelDescriptiveInfoRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
