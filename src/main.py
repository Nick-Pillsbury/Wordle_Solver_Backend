from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from wordle_functions import load_word_list, BoardState, best_entropy_guess, best_entropy_guesses


# Load words into memory
all_words = load_word_list("../files/words.txt")


# HTTP request model
class HttpBoardState(BaseModel):
    green: dict[str, list[int]] = {}
    yellow: dict[str, list[int]] = {}
    gray: list[str] = []


# Create FastApi App
app = FastAPI() 


# FastAPI enpoint to get next best guess
# If first guess, use precalculated guess
    # Takes in board State
    # Returns next best guess
@app.post("/next_guess")
def next_guess(json_board: HttpBoardState):
    global all_words
    
    # Convert http board state to backend board struct
    board = BoardState(
        green = json_board.green,
        yellow = json_board.yellow,
        gray = set(json_board.gray)
    )
    
    if not board.green and not board.yellow and not board.gray:
        return {"guess": "tares"}
    
    guess = best_entropy_guess(board, all_words)
    if guess == None:
        raise HTTPException(status_code=400, detail="No valid words remaining or no valid word found")
    
    return {"guess": guess}




# FastAPI enpoint to get next best guess
# If first guess, use precalculated guess
    # Takes in board State
    # Returns next best guess
@app.post("/all_next_guesses")
def next_guess(json_board: HttpBoardState):
    global all_words
    
    # Convert http board state to backend board struct
    board = BoardState(
        green = json_board.green,
        yellow = json_board.yellow,
        gray = set(json_board.gray)
    )
    
    if not board.green and not board.yellow and not board.gray:
        return {"guess": "tares"}
    
    guesses = best_entropy_guesses(board, all_words)
    if guesses == None:
        raise HTTPException(status_code=400, detail="No valid words remaining or no valid word found")
    
    return {"guesses": guesses}