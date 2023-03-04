import random, time

#1: Print a welcome message. Include "press Enter to start".

print("Welcome to our fastest finger game. Press Enter to proceed")

#2: use input() to wait for the user to press Enter
input()

#3: wait a random number of seconds, then print "DRAW!"
seconds = random.randint(1,10)
time.sleep(seconds)
print("Draw")

#4: Time how long it takes for the user to press Enter. Get the current time with time.time()
start = time.time()

#5: use input() to wait for the user to press Enter
input()

#6: Use time.time() again to get the time after the user pressed Enter
stop = time.time()

#7: Print how long it took
elapsed_time = stop - start

#8: Print different results, based on how long it took
print(f"The elapsed time is :{elapsed_time}")

# Used whole number because the time window on the instruction is too small.
if elapsed_time < 1.0:
 print("You pressed Enter too soon, didn't you?")

elif elapsed_time < 3.0 > 1.0:
 print ("You're the fastest draw in the west, congratulations!")

elif elapsed_time > 3.0:
  print("Too slow! Try again next time.")

else:
  print("Try again!")