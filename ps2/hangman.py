import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    return random.choice(wordlist)

# -----------------------------------
# HANGMAN
# -----------------------------------

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        
    return True



def get_guessed_word(secret_word, letters_guessed):
    word=[]
    for letter in secret_word:
        if letter in letters_guessed:
            word.append(letter)
        else:
            word.append('_')
    return ''.join(word)



def get_available_letters(letters_guessed):
    available_letter=[]
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letter.append(letter)
    
    return "".join(available_letter)
    
    

def hangman(secret_word):

    print(f"""Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have 3 warnings left.""")
    
    vowels='aeiou'
    guess_number=6
    guessed_letters=[]
    warning_number=3

    while guess_number > 0:
      print(f"""------------\nYou have {guess_number} guesses left.\nAvailable letters: {get_available_letters(guessed_letters)}""")
      
      letter_guess=input('Please guess a letter: ')

      # letter format is incorrect
      if not str.isalpha(str.lower(letter_guess)):
          if warning_number > 0:
            warning_number-=1
          else:
            guess_number-=1

          print(f'Oops! That is not a valid letter. You have {warning_number} warnings left: {get_guessed_word(secret_word,guessed_letters)}')
          continue

      if letter_guess in guessed_letters:
          if warning_number > 0:
            warning_number-=1
          else:
            guess_number-=1

          print(f"Oops! You've already guessed that letter. You have {warning_number} warnings left: {get_guessed_word(secret_word,guessed_letters)}")
          continue

      # letter format is correct
      guessed_letters.append(letter_guess)

      if letter_guess in secret_word:
          print(f'Good guess: {get_guessed_word(secret_word,guessed_letters)}')
        
      if letter_guess not in secret_word:
          if letter_guess in vowels:
              guess_number-=2
          else:
              guess_number-=1
        
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,guessed_letters)}")
            
      if is_word_guessed(secret_word,guessed_letters):
          print(f"""Congratulations, you won!\nYour total score for this game is: {len(get_available_letters(guessed_letters))*len(set(secret_word))} """)
          break
    
    if guess_number < 1:
        print(f"""------------\nSorry, you ran out of guesses. The word was {secret_word}.""")


# -----------------------------------
# HINTS
# -----------------------------------

def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i]!='_':
            if my_word[i]!=other_word[i]:
                return False
        elif other_word[i] in my_word:
            return False
    
    return True



def show_possible_matches(my_word):
    word_found=False
    for word in wordlist:
        if match_with_gaps(my_word,word):
            word_found=True
            print(word,end=" ")

    if word_found:
        print()
    else:
        print('No matches found')



def hangman_with_hints(secret_word):

    print(f"""Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have 3 warnings left.""")
    
    vowels='aeiou'
    guess_number=6
    guessed_letters=[]
    warning_number=3

    while guess_number > 0:
      print(f"""------------\nYou have {guess_number} guesses left.\nAvailable letters: {get_available_letters(guessed_letters)}""")
      
      letter_guess=input('Please guess a letter: ')

      # hint
      if letter_guess == '*':
          show_possible_matches(get_guessed_word(secret_word,guessed_letters))
          continue

      # letter format is incorrect
      if not str.isalpha(str.lower(letter_guess)):
          if warning_number > 0:
            warning_number-=1
          else:
            guess_number-=1

          print(f'Oops! That is not a valid letter. You have {warning_number} warnings left: {get_guessed_word(secret_word,guessed_letters)}')
          continue

      if letter_guess in guessed_letters:
          if warning_number > 0:
            warning_number-=1
          else:
            guess_number-=1

          print(f"Oops! You've already guessed that letter. You have {warning_number} warnings left: {get_guessed_word(secret_word,guessed_letters)}")
          continue

      # letter format is correct
      guessed_letters.append(letter_guess)

      if letter_guess in secret_word:
          print(f'Good guess: {get_guessed_word(secret_word,guessed_letters)}')
        
      if letter_guess not in secret_word:
          if letter_guess in vowels:
              guess_number-=2
          else:
              guess_number-=1
        
          print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,guessed_letters)}")
            
      if is_word_guessed(secret_word,guessed_letters):
          print(f"""Congratulations, you won!\nYour total score for this game is: {len(get_available_letters(guessed_letters))*len(set(secret_word))} """)
          break
    
    if guess_number < 1:
        print(f"""------------\nSorry, you ran out of guesses. The word was {secret_word}.""")


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
