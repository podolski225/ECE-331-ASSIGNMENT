import speech_recognition as sr
import random
import time

# A PROJECT TO CREATE A SPEECH TO TEXT GAME#
print('let play a little speech to text game')
TEXT=["groundnut","peanut","strawberry","sugar"]
GUESS=random.choice(TEXT)
guess=1
r=sr.Recognizer()
print("pick a word from 'groundnut, peanut, strawberry,sugar'")
print('note:you have three guesses!!!')
while guess < 4:
    print(f"Guess {guess}")
    guess+=1
    file_name=input("Enter the filename:")
    my_audio=sr.AudioFile(file_name)
    with my_audio as source:
        audio=r.record(source)
    try:
        if GUESS == r.recognize_google(audio):
            print("Correct!,you are right ")
            break
        else:
            print("try again")
            continue
    except:
        print("an error occured")
else:
    print("you have reached the maximum amount of guesses!")
    print("good bye!")
    print(f"i was thinking of {GUESS}")

        




