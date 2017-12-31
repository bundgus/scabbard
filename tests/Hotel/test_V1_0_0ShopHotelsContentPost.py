from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_content_post():
    client = get_client()

    j = json.loads('''{
                        "GetHotelContentRQ": {
                            "SearchCriteria": {
                                "HotelRefs": {
                                    "HotelRef": [{
                                        "HotelCode": "1"
                                    }, {
                                        "HotelCode": "1100"
                                    }]
                                },
                                "DescriptiveInfoRef": {
                                    "PropertyInfo": true,
                                    "LocationInfo": true,
                                    "Amenities": true,
                                    "Descriptions": {
                                        "Description": [{
                                            "Type": "Dining"
                                        }, {
                                            "Type": "Alerts"
                                        }]
                                    },
                                    "Airports": true,
                                    "AcceptedCreditCards": true
                                },
                                "ImageRef": {
                                    "MaxImages": "10"
                                }
                            }
                        }
                    }''')

    content = client.Hotel\
        .V1_0_0ShopHotelsContentPost(gethotelcontentrequest=j,
                                     mode='content'
                                     )\
        .result()

    assert 29 == len(content['GetHotelContentRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
