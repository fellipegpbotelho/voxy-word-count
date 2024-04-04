import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_count_words_return_validation_error():
    response = client.post("/words/count")

    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"


def test_count_words_return_200_status_code():
    response = client.post("/words/count", json={
        "text": "text"
    })

    assert response.status_code == 200


@pytest.mark.parametrize(
    "text,expected_count",
    [
        ("text", 1),
        ("short text to be counted", 5),
        ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consectetur finibus fringilla. Quisque lacinia a ante sed convallis. Phasellus nec diam euismod, accumsan magna et, dignissim est. Vivamus quis vehicula mauris. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras ultrices semper nisi ut sodales. Sed.", 50),
    ]
)
def test_count_words_return_count(text, expected_count):
    response = client.post("/words/count", json={
        "text": text,
    })

    assert response.json().get("count") == expected_count
