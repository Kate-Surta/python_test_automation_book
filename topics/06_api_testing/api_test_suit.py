import pytest
import requests
from requests.exceptions import Timeout, RequestException
from jsonschema import validate
from unittest.mock import patch


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}


comment_schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["postId", "id", "name", "email", "body"],
}


# GET + exception handling
def test_get_comment(base_url, headers):
    try:
        response = requests.get(f"{base_url}/comments/1", headers=headers, timeout=5)
        response.raise_for_status()
        comment_data = response.json()
        print(comment_data)
        # captured = capfd.readouterr()
        # print("Captured Output:", captured.out)

        # Validate response structure using a schema with the jsonschema library.
        validate(instance=comment_data, schema=comment_schema)

        # Asserts
        assert comment_data['id'] == 1
    except Timeout as e:
        pytest.fail(f"Request timed out: {e}")
    except RequestException as e:
        pytest.fail(f"Request failed: {e}")


# POST using payload
def test_create_comment(base_url, headers):
    payload = {
        "name": "name",
        "email": "none@none.com",
        "body": "name",
        "postId": 1
    }
    response = requests.post(f"{base_url}/comments", json=payload, headers=headers)

    assert response.status_code == 201

    my_comment = response.json()
    # Validate response structure using a schema with the jsonschema library.
    validate(instance=my_comment, schema=comment_schema)

    # Verify payload within response
    assert my_comment['name'] == payload['name']
    assert my_comment['email'] == payload['email']
    assert my_comment['body'] == payload['body']
    assert my_comment['postId'] == payload['postId']

# PUT
def test_update_comment(base_url, headers):
    comment_id = 1
    updated_payload = {
        "id": comment_id,
        "name": "updated_name",
        "email": "updated_none@none.com",
        "body": "updated_body",
        "postId": 1
    }
    response = requests.put(f"{base_url}/comments/{comment_id}", json=updated_payload, headers=headers)

    assert response.status_code == 200
    comment_data = response.json()
    # Validate response structure using a schema with the jsonschema library.
    validate(instance=comment_data, schema=comment_schema)

    # Verify updates
    assert comment_data['name'] == updated_payload['name']
    assert comment_data['email'] == updated_payload['email']
    assert comment_data['body'] == updated_payload['body']


# DELETE
def test_delete_comment(base_url, headers):
    comment_id = 1
    response = requests.delete(f"{base_url}/comments/{comment_id}", headers=headers)

    assert response.status_code == 200
    # and confirming its removal using Mock.
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        check_response = requests.get(f"{base_url}/comments/{comment_id}", headers=headers)
        assert check_response.status_code == 404

# pytest main.py -s
