#Step 1 ####MY_CODE
import random
import hangman_art as ha
import hangman_words as hw

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)
lives = 6
stages_start = -1
end = False

print(ha.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create Blanks:
display = []
for i in range(0, word_length):
  display.append("_")
  
while end == False:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already guessed {guess}")
    
    for i in range(0, word_length):
      if guess == chosen_word[i]:
        display[i] = guess

    if guess not in chosen_word:
      print(f"{guess} is not in the word. You lose a life ")
      lives -= 1
      if lives == 0:
        end = True
        print("You lost!")   
        
    print(f"{' '.join(display)}")

    if "_" not in display:
      end = True
      print("You Win!")

    print(ha.stages[lives])