""" Test for `api` package """
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from hexatron.api import app


@pytest.fixture
def client():
    return TestClient(app)


@patch("hexatron.api.to_hexadecimal")
def test_assert_to_hexadecimal_called(mock, client):
    number = 1
    client.get(f"/to_hexadecimal/{number}")
    mock.assert_called_with(number)


@pytest.mark.parametrize(
    "test_case, expected_hexadecimal_string",
    [
        (0, "0"),
        (-1, "-1"),
        (0, "0"),
        (21, "15"),
    ],
)
def test_to_hexadecimal_endpoint_with_valid_input(client, test_case, expected_hexadecimal_string):
    response = client.get(f"/to_hexadecimal/{test_case}")
    assert response.status_code == 200
    assert response.json() == expected_hexadecimal_string


@pytest.mark.parametrize(
    "test_case, expected_response, status_code",
    [
        (
            "test",
            {
                "detail": [
                    {
                        "loc": ["path", "number"],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer",
                    }
                ]
            },
            422,
        ),
        ("", {"detail": "Not Found"}, 404),
        (
            "2.5",
            {
                "detail": [
                    {
                        "loc": ["path", "number"],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer",
                    }
                ]
            },
            422,
        ),
    ],
)
def test_to_hexadecimal_endpoint_with_invalid_input(client, test_case, expected_response, status_code):
    response = client.get(f"/to_hexadecimal/{test_case}")
    assert response.status_code == status_code
    assert response.json() == expected_response
