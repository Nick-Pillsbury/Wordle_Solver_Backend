import requests


class HttpBoardState:
    def __init__(self, green=None, yellow=None, gray=None):
        self.data: dict = {
            "green": green or {},      # dict[str, list[int]]
            "yellow": yellow or {},    # dict[str, list[int]]
            "gray": gray or []         # list[str]
        }


BASE_URL = "http://127.0.0.1:8000/next_guess"


# ---------------------------
# Test 1: First Move
# ---------------------------
print("Test 1: First Move")
test1_board = HttpBoardState()
response1 = requests.post(url=BASE_URL, json=test1_board.data)
print("Status:", response1.status_code)
print("Body:", response1.json())
print()


# ---------------------------
# Test 2: Error Case
# All letters marked gray → no possible words
# ---------------------------
print("Test 2: Error Case")
test2_board = HttpBoardState(
    gray=list("abcdefghijklmnopqrstuvwxyz")
)

response2 = requests.post(url=BASE_URL, json=test2_board.data)
print("Status:", response2.status_code)
if response2.status_code == 400:
    print("Error:", response2.json())
else:
    print("Body:", response2.json())
print()


# ---------------------------
# Test 3: Normal Case
# ---------------------------
print("Test 3: Normal Case")
test3_board = HttpBoardState(
    green={"c": [0]},
    yellow={"r": [2]},
    gray=["x", "z", "y", "p", "g", "w", "l", "s"]
)
response3 = requests.post(url=BASE_URL, json=test3_board.data)
print("Status:", response3.status_code)
print("Body:", response3.json())
print()