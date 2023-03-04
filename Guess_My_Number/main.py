import random

# Set secret number
secret_number = random.randint(1,99)
print("I'm thinking of a number between 1 and 99")
guess = ""

#print(secret_number)

# Ask the user to guess
while guess != secret_number:
  guess = (input("Enter a guess: "))
  
  if guess.isdecimal() == True:
    
    # Check to see if the guess is <, >, or = secret number
    if guess.isdecimal() > secret_number:
      print("Your guess is too high")
      
    elif guess.isdecimal() < secret_number:
      print("Your guess is too low")
      
    else:
      # Print the right message
      print(f"Congrats! The number was {secret_number}")
    
  else:
    print("that's not a number")

