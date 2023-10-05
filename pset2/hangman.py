# Problem Set 2, hangman.py
# Name: peebeejay
# Collaborators:
# Time spent: 8h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Marker when end of letters_guess [] is reached
    letters_guessed.append('end')
    
    for s_letter in secret_word:
        for g_letter in letters_guessed:       
            if s_letter == g_letter:
                break # terminate inner FOR loop, move to next s_letter
            # if no match after comparing with all g_letter(s)
            elif g_letter == 'end':
                return False
        # else move to next g_letter; compare with current s_letter
    
    return True


# Test
"""
secret_word = 'apple'
letters_guessed = ['e','a','b','p','l']
print("First Guess:", is_word_guessed(secret_word, letters_guessed))
  
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print("First Guess:", is_word_guessed(secret_word, letters_guessed))

letters_guessed = ['a', 'p', 'p', 'l', 'e']
print("Second Guess:",is_word_guessed(secret_word, letters_guessed))

letters_guessed = ['p', 'a', 'p', 'l', 'e']
print("Third Guess:",is_word_guessed(secret_word, letters_guessed))

letters_guessed = ['d', 'p', 'p', 'l', 'e']
print("Fourth Guess:",is_word_guessed(secret_word, letters_guessed))
"""
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces
    that represents which letters in secret_word have been guessed so far.
    '''
    # str to store letters and _`space`
    word = ''
    # iterate through secret_word
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += '_ '
    return word

# Test   
"""secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))"""


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # empty str to concatenate all letters not guessed
    available_letters = ''
    alphabets = string.ascii_lowercase
    for alphabet in alphabets:
        if alphabet not in letters_guessed:
            available_letters += alphabet
    return available_letters

# Test  
"""letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
print (get_available_letters(letters_guessed))"""
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # is_word_guessed(secret_word, letters_guessed) returns True / False
    # get_guessed_word(secret_word, letters_guessed) returns 'a_ p_ le'
    # get_available_letters(letters_guessed) returns letters not guessed yet
    
    guesses_remaining = 6
    warnings_remaining = 3
    total_score = 0 # guesses remaining * number unique letters in secret word
    vowels = 'aeiou'
    
    print("Welcome to the game Hangman!")
    
    
    word_count = 0
    for letter in secret_word:
        word_count += 1
    # count unique letters
    unique_letters = set(secret_word)
    unique_count = len(unique_letters)
    letters_guessed = []
    
    print("I am thinking of a word that is {} letters long.".format(word_count))
    print("You have {} warnings left.".format(warnings_remaining))
    print("-------------")
    
    # before each guess, display to user 
    while True:
        print("You have {} guesses left.".format(guesses_remaining))
        
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess_word = (input("Please guess a letter: ")).lower()

        # check user input is an alphabet
        if not guess_word.isalpha():
            warnings_remaining -= 1
            if warnings_remaining >= 0:    
                print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings_remaining), get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
        
        # check user has not already guessed this letter
        elif guess_word not in get_available_letters(letters_guessed):
            warnings_remaining -= 1
            if warnings_remaining >= 0:
                print("Oops! You've already guessed that letter. You have {} warnings left:".format(warnings_remaining), get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
                
        elif guess_word in secret_word:
            letters_guessed.append(guess_word)
            print(letters_guessed)
            
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            
        else:
            letters_guessed.append(guess_word)
            # consonant and not in secret_word
            if guess_word not in vowels:
                guesses_remaining -= 1
            # vowel and not in secret_word
            else:
                guesses_remaining -= 2        
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        
        print("-------------")
        
        # game termination
        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
            break
        elif '_ ' not in get_guessed_word(secret_word, letters_guessed):
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score = guesses_remaining * unique_count
                print("Congratulations, you won!")
                print("Your total score for this game is:", total_score)
                print("-------------")
                break
  
# test     
#secret_word = 'tact'
#hangman(secret_word) 


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    # check if both words are same length
    my_word = my_word.replace(" ","") # remove whitespaces; my_word.strip() does not remove the spaces in middle of str; "a _ _ ple".strip() remains the same
    if len(other_word) != len(my_word):
        return False
    
    # check if guessed letter in my_word matches corresponding letter in other_word
    for i in range(len(my_word)):
        if my_word[i] == '_':
            if other_word[i] in my_word: # hidden letter cannot be words already revealed
                return False
            else: 
                continue
        elif my_word[i] != other_word[i]:
            return False
    return True

#test 
"""print(match_with_gaps("te_ t", "tact"))
print(match_with_gaps("a_ ple", "apple"))
print(match_with_gaps("a_ _ le", "apple"))"""


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    word_matched = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print (word + "")
            word_matched += 1
    if word_matched == 0:
        print("No matches found")
#test
"""show_possible_matches("t_ _ t")
show_possible_matches("abbbb_ ")
show_possible_matches("a_ pl_ ")"""

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    total_score = 0 # guesses remaining * number unique letters in secret word
    vowels = 'aeiou'
    
    print("Welcome to the game Hangman!")
    
    
    word_count = 0
    for letter in secret_word:
        word_count += 1
    # count unique letters
    unique_letters = set(secret_word)
    unique_count = len(unique_letters)
    letters_guessed = []
    
    print("I am thinking of a word that is {} letters long.".format(word_count))
    print("You have {} warnings left.".format(warnings_remaining))
    print("-------------")
    
    # before each guess, display to user 
    while True:
        print("You have {} guesses left.".format(guesses_remaining))
        
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess_word = (input("Please guess a letter: ")).lower()
        # modification (hangman with hint)
        if guess_word == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        # check user input is an alphabet
        elif not guess_word.isalpha():
            warnings_remaining -= 1
            if warnings_remaining >= 0:    
                print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings_remaining), get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
        
        # check user has not already guessed this letter
        elif guess_word not in get_available_letters(letters_guessed):
            warnings_remaining -= 1
            if warnings_remaining >= 0:
                print("Oops! You've already guessed that letter. You have {} warnings left:".format(warnings_remaining), get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
                
        elif guess_word in secret_word:
            letters_guessed.append(guess_word)
            #print(letters_guessed)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            
        else:
            letters_guessed.append(guess_word)
            # consonant and not in secret_word
            if guess_word not in vowels:
                guesses_remaining -= 1
            # vowel and not in secret_word
            else:
                guesses_remaining -= 2        
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        
        print("-------------")
        
        # game termination
        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
            break
        elif '_ ' not in get_guessed_word(secret_word, letters_guessed):
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score = guesses_remaining * unique_count
                print("Congratulations, you won!")
                print("Your total score for this game is:", total_score)
                print("-------------")
                break
  

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
