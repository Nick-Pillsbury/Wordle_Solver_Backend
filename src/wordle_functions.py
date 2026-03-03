from math import log2
from collections import Counter



# Struct to hold board data
class BoardState:
    def __init__(self, green = None, yellow = None, gray = None):
        self.green: dict[str, list[int]] = green or {}
        self.yellow: dict[str, list[int]] = yellow or {}
        self.gray: set[str] = gray or set()



# Checks if a word is valid for current board state
# Takes a word
# Returns a true false bool
def is_valid_word(board: BoardState, word: str) -> bool:
    # green letters
    for letter, positions in board.green.items():
        # present
        if letter not in word:
            return False
        # in Correct Possitions
        for position in positions:
            if word[position] != letter:
                return False
    # yellow letters
    for letter, positions in board.yellow.items():
        # present
        if letter not in word:
            return False
        # banned position
        for position in positions:
            if word[position] == letter:
                return False
    # Check for gray letters (not present in the word)
    for letter in board.gray:
        if letter in word:
            return False
    return True



# Fucntion to reduces a word list to only possible words for the current board state
# Takes in a list of words to check
# Returns a list of possible words
def find_possible_words(board: BoardState, word_list: list[str]) -> list[str]:
    possible_words = []
    for word in word_list:
        if is_valid_word(board, word):
            possible_words.append(word)
    return possible_words



# Function to load all words into memory
# Takes a file path
# Returns a list words
def load_word_list(filepath: str) -> list[str]:
    words = []
    with open(filepath) as f:
        for word in f:
            word = word.strip()
            if word and word.isalpha() and len(word) == 5:
                words.append(word.lower())
    return words



# Function to determine the resulting pattern of a guess to a potential solution
    # What pattern would I get, if this was my guess and this was the solution?
    # Pattern symbols:
    #    'G' = green
    #    'Y' = yellow
    #    '.' = gray
    # Example:
    #    Guess: allee
    #    Solution: apple
    #    Result: GY..G
# Takes two words
# Returns the resulting pattern
def get_pattern(guess: str, solution: str) -> str:
    pattern = ['.'] * 5
    
    # Count letters in solution
    solution_counts = Counter(solution)
    
    # First pass: Mark Greens
    for i in range(5):
        if guess[i] == solution[i]:
            pattern[i] = 'G'
            solution_counts[guess[i]] -= 1
    
    # Second pass: Mark Yellows if not already marked green
    for i in range(5):
        if pattern[i] == '.':
            if solution_counts[guess[i]] > 0:
                pattern[i] = 'Y'
                solution_counts[guess[i]] -= 1
    
    return ''.join(pattern)



# Compute expected information gain of a guess, where possible words are possible solutions
    # Calculate the unique number of patterns for this guess compared to possible words
    # Use shannon entropy to calculate the information gain of a guess
# Takes a guess and all possible words for current board state
# Returns a entropy score of the guess
def entropy_score(guess: str, possible_words: list[str]) -> float:
    patterns = [get_pattern(guess, sol) for sol in possible_words]
    counts = Counter(patterns)
    total = len(possible_words)
    
    # Shannon entropy
    score = 0
    for count in counts.values():
        percent = count/total
        if percent > 0:
            score -= percent * log2(percent)
    return score



# Finds the guess with the highest entropy.
# Calcualte the entropy score for each possible word and take the max
# Takes a list of all words
# Returns the guess with the highest entropy
def best_entropy_guess(board: BoardState, all_words: list[str]) -> str | None:
    possible_words = find_possible_words(board, all_words)
    
    if not possible_words:
        return None
    
    # small set only consider valid candidates
    if len(possible_words) <= 5:
        candidates = possible_words
    # large set can use all_words for infomation gain and word elimination
    else:
        candidates = all_words
    
    scores = [(entropy_score(word, possible_words), word) for word in candidates]
    if not scores:
        return None
    
    return max(scores)[1]


def best_entropy_guesses(board: BoardState, all_words: list[str]) -> list[str] | None:
    possible_words = find_possible_words(board, all_words)
    
    if not possible_words:
        return None
    
    # small set only consider valid candidates
    if len(possible_words) <= 5:
        candidates = possible_words
    # large set can use all_words for infomation gain and word elimination
    else:
        candidates = all_words
    
    scores = [(entropy_score(word, possible_words), word) for word in candidates]
    if not scores:
        return None
    
    return scores