#Number guessing
import random


target_number = random.randint(1,10)
attempts = 0
try:

    while True:
       guess =int(input("Enter your guess(1-10):"))
       if guess < 1 or guess > 10:
           print("Please enter a number between 1 and 10.")
           continue
       attempts += 1
       if guess == target_number:
           print(f"Congratulation! You guessed the number in {attempts}attempts!")
           break
       elif guess < target_number:
           print("Too Low! Try Again.")
       else:
           print("To High! Try Again.")    
except ValueError:
   print("Invalid input.Please enter a number between 1 and 10")




        


    


