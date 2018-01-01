from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_image_post():
    client = get_client()

    j = json.loads('''{
                      "GetHotelImageRQ": {
                        "HotelRefs": {
                          "HotelRef": [
                            {
                              "HotelCode": "1276",
                              "CodeContext": "Sabre"
                            }
                          ]
                        },
                        "ImageRef": {
                          "Type": "THUMBNAIL",
                          "CategoryCode": 3,
                          "LanguageCode": "EN"
                        }
                      }
                    }''')

    image = client.Hotel\
        .V1_0_0ShopHotelsImagePost(gethotelimagerequest=j,
                                   mode='image'
                                   )\
        .result()

    assert 29 == len(image['GetHotelImageRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
