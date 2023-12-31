# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    first_component=0
    for letter in word.lower():
        if letter != '*':
            first_component+=SCRABBLE_LETTER_VALUES[letter]
    
    second_component = 7*len(word) - 3*(n-len(word))
    if second_component < 1:
        second_component=1

    return first_component*second_component

#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    for x in hand.keys():
        if x in VOWELS:
            hand['*']=1
            del hand[x]
            break
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    updated_hand=hand.copy()
    for letter in word.lower():
        if letter in updated_hand:
            updated_hand[letter]-=1
            if updated_hand[letter]==0:
                del(updated_hand[letter])
    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    # check letter inclusion
    new_hand={}
    for letter in hand.keys():
        new_hand[letter]=hand[letter]+1

    letter_included=True
    for letter in word.lower():
        if letter not in update_hand(new_hand,word).keys():
            letter_included=False

    # check word inclusion
    word_included=(word.lower() in word_list)
    if word.find('*') != -1:
        for vowel in VOWELS:
            original_word=word.replace('*',vowel).lower()
            if original_word in word_list:
                word_included=True
    
    return word_included and letter_included

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    return len(hand)

def play_hand(hand, word_list):
    total_score=0
    updated_hand=hand.copy()

    while len(updated_hand)>0:
        print(f"Current Hand: ",end='')
        display_hand(updated_hand)
        word=input('Enter word, or "!!" to indicate that you are finished: ')
        
        if word == "!!":
            break

        if is_valid_word(word,updated_hand,word_list):
            score=get_word_score(word,calculate_handlen(updated_hand))
            total_score+=score
            print(f"'{word}' earned {score} points. Total: {total_score} points")
        else:
            print('That is not a valid word. Please choose another word.')

        print()
        updated_hand=update_hand(updated_hand,word)

    if len(updated_hand)<1:
        print('Ran out of letters')

    return total_score

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

#
# Problem #6: Playing a game
# 
def substitute_hand(hand, letter):
    if letter not in hand.keys():
        return hand

    random_letter=random.choice("".join(SCRABBLE_LETTER_VALUES.keys()))
    while random_letter in hand.keys():
        random_letter=random.choice("".join(SCRABBLE_LETTER_VALUES.keys()))

    new_hand=hand.copy()
    new_hand[random_letter]=new_hand.pop(letter)

    return new_hand
       
    
def play_game(word_list):
    hands_n=int(input("Enter total number of hands: "))
    prev_score=0
    total_score=0
    replay=False
    replayed=False
    substituted=False

    hand_turn=0
    while hand_turn < hands_n:
        # deal hand
        if not replayed:
            hand=deal_hand(HAND_SIZE)

        print(f'Current hand:',end=' ')
        display_hand(hand)

        # substitute
        if (not substituted and not replay):
            if input('Would you like to substitute a letter? (no/yes): ') == 'yes':
                letter_to_replace=input('Which letter would you like to replace: ')
                hand=substitute_hand(hand,letter_to_replace)
                substituted=True

        # play
        hand_score=play_hand(hand, word_list)
        print(f'Total score for this hand: {hand_score}')
        print('---------------------')

        if not replay:
            replay = input('Would you like to replay the hand? (no/yes): ')=='yes'
            if replay:
                prev_score=hand_score
                replayed=True
                hand_turn-=1

        if prev_score==0:
            total_score+=hand_score
        elif prev_score!=hand_score:
            total_score+=max(prev_score,hand_score)
            prev_score=0

        hand_turn+=1

    print(f'Total score over all hands: {total_score}')



if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)