import random
import images as img
import words
import os

print(img.logo)
life=6
chosen_word = random.choice(words.word_list)
ls=[]
for i in chosen_word:
    ls.append('_ ')

#print(f'\nThe solution is {chosen_word}.')
endOfGame=False

while not endOfGame:
    print(img.stages[life])
    print("".join(ls))
    guess = input("\nGuess a letter: ").lower()
    os.system('cls')

    if guess in ls:
          print("You Already guessed this Letter")
          continue

    for i in range(0,len(chosen_word)):
        if guess==chosen_word[i]:
            ls[i]=guess
            
    
    if guess not in ls:
        life-=1
        print("\nIncorrect Guess!!!")
        if life==0:
          print(img.stages[0])
          print("\n😢You Loose!!\n")
          quit()


    if ls.count('_ ')==0:
        endOfGame=True
        print("".join(ls))
        print("\n🚩You Win!! Congrats🎉\n")
    
