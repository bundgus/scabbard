from scabbard.access_token import get_token


def test__get_token():
    token = get_token()
    assert isinstance(token, str)
    assert 316 == len(token)
