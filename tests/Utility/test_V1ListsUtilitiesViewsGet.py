from scabbard import get_client


def test__v1_lists_utilities_views_get():
    client = get_client()

    views = client.Utility\
        .V1ListsUtilitiesViewsGet()\
        .result()

    assert 0 < len(views['Views'])
