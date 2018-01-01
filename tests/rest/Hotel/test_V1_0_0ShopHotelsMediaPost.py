from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_media_post():
    client = get_client()

    j = json.loads('''{
                      "GetHotelMediaRQ":{
                        "HotelRefs":{
                          "HotelRef":[
                            {
                              "HotelCode":"62580",
                              "CodeContext":"Sabre",
                              "ImageRef":{
                                "MaxImages":"1",
                                "Images":{
                                  "Image":[
                                    {
                                      "Type":"THUMBNAIL"
                                    }
                                  ]
                                },
                                "Categories":{
                                  "Category":[
                                    {
                                      "Code":1
                                    }
                                  ]
                                },
                                "AdditionalInfo":{
                                  "Info":[
                                    {
                                      "Type":"CAPTION",
                                      "content":true
                                    }
                                  ]
                                },
                                "Languages":{
                                  "Language":[
                                    {
                                      "Code":"EN"
                                    }
                                  ]
                                }
                              }
                            }
                          ]
                        }
                      }
                    }''')

    media = client.Hotel\
        .V1_0_0ShopHotelsMediaPost(gethotelsmediarequest=j)\
        .result()

    assert 29 == len(media['GetHotelMediaRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
