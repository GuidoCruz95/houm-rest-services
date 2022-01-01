import pytest

from curl_access import curl_functions

test_data = {
    "houmers": [
        {
            "id": 1001,
            "name": "Jose",
            "last_name": "maria cardenas",
            "current_location": "-33.387451296071845, -70.61456199591032"
        }, {
            "id": 1002,
            "name": "Daniela",
            "last_name": "Perez Ovando",
            "current_location": "-33.38896955808164, -70.61746647304639"
        }
    ],
    "places": [
        {
            "id": 2001,
            "owner": "Unknown",
            "name": "Houm office",
            "description": "Main Houm office",
            "location": "-33.387451296071845, -70.61456199591032"
        }
    ],
    "visitors": [
        {
            "id": 3001,
            "name": "Luis",
            "last_name": "Zeballos Mamani",
            "current_location": "-33.387451296071845, -70.61456199591032"
        }
    ],
    "visited": [
        {
            "houmer": 1001,
            "place": 2001,
            "visitor": 3001,
            "started_at": "2018-05-03 08:00:00",
            "completed_at": "2018-05-03 11:00:00"
        },
        {
            "houmer": 1001,
            "place": 2002,
            "visitor": 3002,
            "started_at": "2018-05-20 08:00:00",
            "completed_at": "2018-05-20 18:00:00"
        },
        {
            "houmer": 1001,
            "place": 2003,
            "visitor": 3003,
            "started_at": "2020-08-08 10:00:00",
            "completed_at": "2020-08-08 21:00:00"
        },
        {
            "houmer": 1001,
            "place": 2002,
            "visitor": 3003,
            "started_at": "2020-08-08 22:00:00",
            "completed_at": "2020-08-08 23:00:00"
        },
    ]
}


class TestCurlFunctions:

    @pytest.mark.parametrize(
        "function, data, expected",
        [
            (curl_functions.get_houms, {"places": []}, 0),
            (curl_functions.get_houms, test_data, 2),
            (curl_functions.get_houms, {}, 0),

            (curl_functions.get_visitors, {"places": []}, 0),
            (curl_functions.get_visitors, test_data, 1),
            (curl_functions.get_visitors, {}, 0),

            (curl_functions.get_places, {"places": []}, 0),
            (curl_functions.get_places, test_data, 1),
            (curl_functions.get_places, {}, 0),
        ]
    )
    def test_get_items(self, function, data, expected):
        curl_functions.data = data
        assert len(function()) == expected

    @pytest.mark.parametrize(
        "function, data, identifier, expected",
        [
            (curl_functions.get_houm, {"places": []}, 1001, None),
            (
                    curl_functions.get_houm,
                    test_data,
                    1002,
                    {
                        'id': 1002,
                        'name': 'Daniela',
                        'last_name': 'Perez Ovando',
                        'current_location': '-33.38896955808164, -70.61746647304639'
                    }
            ),
            (curl_functions.get_houm, {}, 1001, None),

            (curl_functions.get_place, {"places": []}, 2001, None),
            (
                    curl_functions.get_place,
                    test_data,
                    2001,
                    {
                        "id": 2001,
                        "owner": "Unknown",
                        "name": "Houm office",
                        "description": "Main Houm office",
                        "location": "-33.387451296071845, -70.61456199591032"
                    }
            ),
            (curl_functions.get_place, {}, 2001, None),

            (curl_functions.get_visitor, {"places": []}, 3001, None),
            (
                    curl_functions.get_visitor,
                    test_data,
                    3001,
                    {
                        "id": 3001,
                        "name": "Luis",
                        "last_name": "Zeballos Mamani",
                        "current_location": "-33.387451296071845, -70.61456199591032"
                    }
            ),
            (curl_functions.get_visitor, {}, 3001, None),
        ]
    )
    def test_get_items_by_identifier(self, function, data, identifier, expected):
        curl_functions.data = data
        assert function(identifier) == expected

    @pytest.mark.parametrize(
        "houmer_id, date, data, expected",
        [
            (1001, '', {}, []),
            (1001, '2020-08-08', test_data,
             [
                 {
                     "houmer": 1001,
                     "place": {
                         "id": 2003,
                         "owner": "Unknown",
                         "name": "Clinica Davila",
                         "description": "Private hospital",
                         "location": "-33.42553775053651, -70.64813859320215"
                     },
                     "visitor": 3003,
                     "started_at": "2020-08-08 10:00:00",
                     "completed_at": "2020-08-08 21:00:00",
                     "spent_time": "11:00:00"
                 },
                 {
                     "houmer": 1001,
                     "place": {
                         "id": 2002,
                         "owner": "Unknown",
                         "name": "Plaza Norte",
                         "description": "Commercial Center",
                         "location": "-33.38896955808164, -70.61746647304639"
                     },
                     "visitor": 3003,
                     "started_at": "2020-08-08 22:00:00",
                     "completed_at": "2020-08-08 23:00:00",
                     "spent_time": "1:00:00"
                 }
             ]
             )
        ]
    )
    def test_visited_places_by_houmer(self, houmer_id, date, data, expected):
        places = {"places": [
            {
                "id": 2001,
                "owner": "Unknown",
                "name": "Houm office",
                "description": "Main Houm office",
                "location": "-33.387451296071845, -70.61456199591032"
            },
            {
                "id": 2002,
                "owner": "Unknown",
                "name": "Plaza Norte",
                "description": "Commercial Center",
                "location": "-33.38896955808164, -70.61746647304639"
            },
            {
                "id": 2003,
                "owner": "Unknown",
                "name": "Clinica Davila",
                "description": "Private hospital",
                "location": "-33.42553775053651, -70.64813859320215"
            }
        ]}
        data.update(places)
        curl_functions.data = data
        res = curl_functions.get_visited_places_by_houmer(houmer_id, date)
        assert expected == res
