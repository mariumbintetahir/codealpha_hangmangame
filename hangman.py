words=["cacophony","serendipity","prudent","sagacious","charismatic"]
import random 
actual_word=random.choice(words)
length=len(actual_word)
print("HANGMAN GAME")
print("Guess the Word")
guessed=[]
count=0
wrong_attempts=0
max_attempts=6
while wrong_attempts< max_attempts and count<length:
    for letter in actual_word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()     
    alphabet=input("which alphabet u think it can be:")
    if alphabet in guessed:
        print("you already have guessed it")
        continue
    guessed.append(alphabet)
    if alphabet in  actual_word:
        print("yes u guessed it right")
        count+=actual_word.count(alphabet)
    else:
        print("oops it was wrong")
        wrong_attempts+=1
if count == length:
    print("u guessed the word correctly")
else:
    print(" oops u couldnot guessed the word")
    
print("The actual word was",actual_word)