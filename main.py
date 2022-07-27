#importing modules for random selection and hangman
import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

#Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6. printing logos setting gameover to flase
print(logo)
end_of_game = False
lives = 6

#choosing a random word from the hangman word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks spaces and assing "_" to the chosen word
display = []
for _ in range(word_length):
    display += "_"
#giving user a random word  as  a hint 
hint_guess = random.choice(chosen_word)
for position in range(word_length):
    letter = chosen_word[position]
    if letter == hint_guess:
      display[position] = letter
      print(f"{' '.join(display)}")


#starting the game
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()  #clearing the screen
    if guess in display:
        print(f"You have already guessed this letter {guess}")

        #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You Lose one life")
    if lives == 0:
      print("You lose.")
      end_of_game = True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters. check if win.
    if "_" not in display:
        print("You win.")
        end_of_game = True

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
