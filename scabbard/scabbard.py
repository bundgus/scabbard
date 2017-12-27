from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file
from scabbard.access_token import get_token


def get_client():
    access_token = "Bearer " + get_token()
    http_client = RequestsClient()
    http_client.set_api_key(
        'api.test.sabre.com', access_token,
        param_name='Authorization', param_in='header'
    )
    return SwaggerClient.from_spec(load_file('scabbard/swagger.yaml'),
                                   http_client=http_client)
