print("Welcome to my KBC quiz!.")

if input("Do you want to play the quiz?(Yes / No)  ") == "yes":
    print("Lets start the quiz")
    print("All the best 👍.Do well 😎")
else:
    print("Thanks for participating.")  
    quit()  

score = 0    

answer = input("Which planet is known as  the Red Planet? ")  
if  answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

answer = input("What is the largest ocean on Earth? ") 
if  answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  

answer = input("What is the name of the first computer mouse? ") 
if  answer.lower() == "the logarithmic mouse":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What is the name of the first personal computer? ") 
if  answer.lower() == "atlair 8800":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")  
      
answer = input("What is the name of the first web browser? ")
if  answer.lower() == "mosaic":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) +"%")


  


 
   