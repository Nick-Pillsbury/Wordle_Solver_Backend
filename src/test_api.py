from fastapi.testclient import TestClient
from main import app



client = TestClient(app)



# If no board state is provided, the API should return the precalculated first guess.
def test_first_move():
    response = client.post(
        "/next_guess",
        json={
            "green": {},
            "yellow": {},
            "gray": []
        }
    )
    assert response.status_code == 200
    assert response.json()["guess"] == "tares"
    print("Passed First Guess")



# If all letters are gray, no valid words should remain. The API should return HTTP 400.
def test_invalid_state_all_gray():
    response = client.post(
        "/next_guess",
        json={
            "green": {},
            "yellow": {},
            "gray": list("abcdefghijklmnopqrstuvwxyz")
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "No valid words remaining"
    print("Passed No Possible Words")



# With a valid board state, the API should still return a guess.
def test_valid_filtered_guess():
    response = client.post(
        "/next_guess",
        json={
            "green": {"c": [0]},
            "yellow": {},
            "gray": ["x", "z", "y", "p", "g", "w", "l", "s"]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "guess" in data
    assert isinstance(data["guess"], str)
    assert len(data["guess"]) == 5
    print("Passed Normal Case")



test_first_move()
test_invalid_state_all_gray()
test_valid_filtered_guess()