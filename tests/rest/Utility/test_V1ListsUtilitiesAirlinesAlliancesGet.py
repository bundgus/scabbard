from scabbard import get_client


def test__v1_lists_utilities_airlines_alliances_get():
    client = get_client()

    alliances = client.Utility\
        .V1ListsUtilitiesAirlinesAlliancesGet(alliancecode='*S')\
        .result()
    assert 'SkyTeam' == alliances['AllianceInfo'][0]['AllianceName']
