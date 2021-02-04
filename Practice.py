import random

print("Put your guess here")
try:
    userInput = int(input())
except:
    userInput = 4
    print("idiot alert")


computerNumber = random.randint(1, 5)
print(f'Here is your guess: {userInput}')

if userInput == computerNumber:
    print("Wow you are actually right for once")
else: 
    print(f'You are really wrong dumbass, this is what it was: {computerNumber}')

