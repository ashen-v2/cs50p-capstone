from fastapi.testclient import TestClient
from http import HTTPStatus
from project import create_app

app = create_app()
client = TestClient(app)


def test_root():
    response = client.get("/api")
    assert response.status_code == HTTPStatus.OK

def test_get_playlists():
    response = client.get("/api/playlists")
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0]["playlist_id"] == "PLhQjrBD2T381ntVU8FtSBx_N3WZCYOZvE"
    assert response.json()[0]["playlist_name"] == "CS50 Fair 2024 at Yale"

def test_get_videos():
    response = client.get("/api/videos")
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0]["video_id"] == "Ew5Dcmccf5w"
    assert response.json()[0]["title"] == "AI Powered Pivot Camera - CS50 Fair 2024 at Yale"
    assert response.json()[0]["url"] == "https://www.youtube.com/watch?v=Ew5Dcmccf5w"

def test_get_transcripts():
    response = client.get("api/videos/Ew5Dcmccf5w")
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0]["start_time"] == 0
    assert response.json()[0]["text"] == "ELIZABETH: Hi."

    response = client.get("api/videos/notavidid")
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_get_transcripts_by_name():
    response = client.get("api/videotitle/AI Powered Pivot Camera - CS50 Fair 2024 at Yale")
    assert response.status_code == HTTPStatus.OK
    assert response.json()[0]["start_time"] == 0
    assert response.json()[0]["text"] == "ELIZABETH: Hi."

    response = client.get("api/videos/notavideotitle")
    assert response.status_code == HTTPStatus.NOT_FOUND