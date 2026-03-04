from wordle_functions import BoardState, is_valid_word, find_possible_words, get_pattern, entropy_score, best_entropy_guess, best_entropy_guesses



def run_tests():
    print("Running simple tests...\n")

    # ---------------------------
    # Test 1: is_valid_word
    # ---------------------------
    board = BoardState(
        green={'a': [0]},
        yellow={'l': [1]},
        gray={'z'}
    )

    print("Test is_valid_word:")
    print("Expected: True     apple ->", is_valid_word(board, "apple"))
    print("Expected: False    zebra ->", is_valid_word(board, "zebra")) 
    print("Expected: False    alarm ->", is_valid_word(board, "alarm"))
    print()


    # ---------------------------
    # Test 2: find_possible_words
    # ---------------------------
    words = ["apple", "angle", "amble", "zebra"]
    possible = find_possible_words(board, words)

    print("Test find_possible_words:")
    print("Words:", words)
    print("Expected:    Possible words:", possible)
    print()


    # ---------------------------
    # Test 3: get_pattern
    # ---------------------------
    print("Test get_pattern:")
    print("Guess: allee, Solution: apple")
    print("Expected: GY..G     Pattern:", get_pattern("allee", "apple"))
    print()


    # ---------------------------
    # Test 4: entropy_score
    # ---------------------------
    possible_words = ["apple", "hello", "ample", "zzzzz"]
    score = entropy_score("zzzzz", possible_words)
    score2 = entropy_score("apple", possible_words)
    print("Test entropy_score:")
    print("Words:", possible_words)
    print("Expexted: Low value    Entropy score for 'zzzzz':", score)
    print("Expexted: High value    Entropy score for 'apple':", score2)
    print()


    # ---------------------------
    # Test 5: best_entropy_guess
    # ---------------------------
    empty_board = BoardState()
    guess = best_entropy_guess(empty_board, possible_words)
    print("Test best_entropy_guess:")
    print("Words:", possible_words)
    print("Best guess:", guess)
    print()
    
    
    # ---------------------------
    # Test 5: best_entropy_guesses
    # ---------------------------
    empty_board = BoardState()
    guesses = best_entropy_guesses(empty_board, possible_words)
    print("Test best_entropy_guess:")
    print("Words:", possible_words)
    print("Ranked guesses:", guesses)
    print()
    


if __name__ == "__main__":
    run_tests()