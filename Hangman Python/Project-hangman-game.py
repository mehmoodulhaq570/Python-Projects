import random
import string

WORDLIST_FILENAME = "D:\Kashif Data\Hangman Game 1\words.txt"

def load_words():
 
    print("Loading word list from file...")
  
    inFile = open(WORDLIST_FILENAME, 'r')
  
    line = inFile.readline()
  
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
      if (char in letters_guessed) == False:
        guessed = False
        break
      else:
        guessed = True
    return guessed

def get_guessed_word(secret_word, letters_guessed):
  
    correct_letters = [] 
    guessed_string = ""  
    
    for item in letters_guessed:
      if item in secret_word:
        correct_letters.append(item)
    
    for char in secret_word:
      if char in correct_letters:
        guessed_string += char
      else:
        guessed_string += "_ "
    
    return guessed_string

def get_available_letters(letters_guessed):
    letters = string.ascii_lowercase
    unguessed = ""
    for char in letters:
      if char not in letters_guessed:
        unguessed += char
    return unguessed

def check_warnings(warnings_remaining, user_guess, duplicate_guesses, display):
  warnings_remaining -= 1
  
  if not user_guess.isalpha(): 
    print('That is not a valid letter. You have ' + str(warnings_remaining) + ' warnings left: ' + display)
  elif user_guess in duplicate_guesses:
    print('You have already guessed that letter. You have ' + str(warnings_remaining) + ' warnings left. ' + display)
  print('-----------------')
  return warnings_remaining

def check_guesses(guesses_remaining, user_guess, duplicate_guesses, display):
  guesses_remaining -= 1
  if not user_guess.isalpha():
    print(" That is not a valid letter. You have no warnings left  " + display)
  elif user_guess in duplicate_guesses: 
    print(' You\'ve already guessed that letter. You have no warnings left : ' + display)
  else:
    print(' That letter is not in my word: ' + display)
  print('-----------------')
  return guesses_remaining

def hangman(secret_word):
  
  letters_guessed = []
  duplicate_guesses = [] 
  guesses_remaining = 6
  warnings_remaining = 3
  
  display = '_ ' * len(secret_word)
  
  unique_letters = ''
  for letter in secret_word:
    if letter not in unique_letters:
      unique_letters += letter
  print('Welcome to the game Hangman!')
  print("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
  print('You have ' + str(warnings_remaining) + ' warnings left.')
  print('*****************')

  while True: 
    letters_left = get_available_letters(letters_guessed)
    print('You have ' + str(guesses_remaining) + ' guesses left.')
    print('Available letters: ' + letters_left)
    user_guess = (input('Please guess a letter: ')).lower()
    if not user_guess.isalpha():
      
      if warnings_remaining > 0:
        warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
      elif guesses_remaining > 1: 
        guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
      else: 
        print('You ran out of guesses. The word was ' + secret_word + '.')
        break
    else:
      if user_guess not in letters_guessed:
        letters_guessed.append(user_guess)
      game_over = is_word_guessed(secret_word, letters_guessed)
      
      if game_over:
        print('Good guess: ' + display)
        print('******************')
        print('Congratulations, you won!')
        total_score = guesses_remaining*len(unique_letters)
        print('Your total score for this game is: ' + str(total_score))
        break
      
      elif user_guess in duplicate_guesses:
        if warnings_remaining > 0: 
          warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
        elif guesses_remaining > 1:
          guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
 
      elif (not (user_guess in duplicate_guesses)) and user_guess in secret_word:
        display = get_guessed_word(secret_word, letters_guessed)
        print('Good guess: ' + display)
        print('******************')
      
      elif user_guess not in secret_word:
        if user_guess in ['a', 'e', 'i', 'o', 'u'] and guesses_remaining > 1:
          guesses_remaining = guesses_remaining - 1
          guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
        elif guesses_remaining > 1:
          guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
        else:
          print('Oops! That letter is not in my word: ' + display)
          print('******************')
          print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
          break
    duplicate_guesses.append(user_guess)
    print(duplicate_guesses)

secret_word = choose_word(wordlist)
hangman(secret_word)