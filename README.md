# Wordle Solver Backend
A Python backend API for solving Wordle puzzles using an entropy-based strategy. Built with FastAPI, this service can provide the next optimal guess based on the current board state.

---

## Features
- FastAPI HTTP API for next best guess
- Entropy-based algorithm to maximize information gain

---

## Folder Structure
```
root/
├── scr/
│   ├── fastapi.py           # FastAPI app
│   ├── wordle_functions.py  # Solver functions
│   └── test_api.py          # Api test file
└── files/
    |── words.txt            # Word list
    └── requirements.txt     # Dependencies
```

---

## Running the API
uvicorn main:app --reload
- The API will be available at http://127.0.0.1:8000

---

## API Usage
Endpoint: /next-guess (POST)
Request JSON:
{
  "green": {"a": [0], "e": [4]},
  "yellow": {"r": [1]},
  "gray": ["t", "o", "s"]
}

- green: letters in the correct position
- yellow: letters present but in wrong positions
- gray: letters not present in the word

Response JSON:
{
  "guess": "arise"
}
If no valid words remain, the API returns a 400 error.

---

## Testing
- API Test located in scr/test_api.py
- Function test located in scr/test_functions.py
- Run tests with:
python scr/test_api.py
python scr/test_functions.py
