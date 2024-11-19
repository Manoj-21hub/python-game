def word_chain_game():
    """
    Play the Word Chain Game where each word must start with the last letter of the previous word.
    Players take turns inputting words. The game ends when a player can't think of a word.
    """
    print("Welcome to the Word Chain Game!")
    
    word_list = []  # To store the words played so far.
    previous_word = ""  # Initially, no word has been played.
    
    while True:
        if previous_word:
            print(f"The last word was: {previous_word}")
        
        # Player 1's turn to input a word
        word = input("Enter a word (or 'quit' to stop the game): ").lower()
        
        if word == "quit":
            print("Game over. Thanks for playing!")
            break
        
        # If there is a previous word, check if the current word starts with the last letter of the previous word
        if previous_word and word[0] != previous_word[-1]:
            print(f"Invalid! The word must start with the letter '{previous_word[-1]}'. Try again.")
            continue
        
        # Check if the word has already been used
        if word in word_list:
            print("You've already used this word. Try a new one.")
            continue
        
        # Add the word to the list and set it as the previous word for the next round
        word_list.append(word)
        previous_word = word
        
        print(f"Good job! '{word}' is a valid word.")
        print(f"Words used so far: {', '.join(word_list)}\n")
        
        # Optional: Limit the number of turns or add other conditions for ending the game (e.g., timer)