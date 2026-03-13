#this is the code for number guessing game with proper explanation 
import random #random library is used to generate random numbers

number=random.randint(1,100) #generating random number between 1 and 100

guess=None #initially guess is set to null

attempts=0 #initially attempts is set to 0

while guess !=number: #used to check if guess is correct or not 
    guess=int(input("enter your guess:")) #taking input from user and converting it to integer
    attempts+=1 #incrementing attempts by 1

    if guess>number:print("too high") #if guess is greater than number then it will print too high
     # in the above statement I have used short hand if statement and print too high       

    elif guess<number: print("too low") #if guess is less than number then it will print too low
     # in the above statement I have used short hand elif statement and print too low      
     
    else: #if guess is equal to number then it will print congratulations and attempts taken
        print("congratulations! you guessed the number in",attempts,"attempts")