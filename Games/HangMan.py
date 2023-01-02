# In this hangman , you are to answer capital cities of countries
# i have imported a file with
# capital cities and my program will read from the files.
import random
import string

from words import words
# print(words
#       )

def get_valid_word(words):
      word = random.choice(words)
      while '_' in word  or '' in word:
            word = random.choice(words)
      return word

def hangman():
      word = random.choice(words)
      word_letters = set(word) #letters in the word
      alphabet =set(string.ascii_uppercase)
      used_letters = set()

      # getting user input

      while len(word_letters) > 0:
            print("you have used these letters: ","".join(used_letters))

            # the current word eg , E_T
            word_list =[letter if letter in used_letters else '_' for letter in word]
            print("current word" ,"" .join(word_list))

            user_letter = input("Guess a letter:").upper()
            if user_letter in alphabet - used_letters:
                  used_letters.add(user_letter)
                  if user_letter in word_letters:
                        word_letters.remove(user_letter)

            elif user_letter in used_letters:
                  print("You have already used that character . Please try again  ")
            else:
                  print("Invalid character.Please try again ")

hangman()




# user_input =input("type something:")
# print(user_input)


