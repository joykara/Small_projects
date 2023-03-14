# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments

from time import sleep


questions = [
  "QUESTION 1: \n Who wrote 'Harry Potter'?",
  "QUESTION 2: \n George Orwell wrote this book, which is often considered a statement on government oversight.",
  "QUESTION 3: \n Which famous book is sub-titled 'The Modern Prometheus'?",
  "QUESTION 4: \n Which of the following is the world's best-selling book?",
  "QUESTION 5: \n 'Green Eggs And Ham' is a book by which author?",
  "QUESTION 6: \n Which famous spy novelist wrote the childrens' story 'Chitty-Chitty-Bang-Bang'?",
  "QUESTION 7: \n How many Harry Potter books are there?",
  "QUESTION 8: \n What's Harry Potter's dad's name?",
  "QUESTION 9: \n Who was the author of the 1954 novel, 'Lord of the Flies'?",
  "QUESTION 10: \n What is the title of the first Sherlock Holmes book by Arthur Conan Doyle?"
]

diff_questions = [
  "QUESTION 11: \n What was the name of the Mysterious Island, in Jules Verne's 'The Mysterious Island'?",
  "QUESTION 12: \n Who wrote the children's story 'The Little Match Girl'?",
  "QUESTION 13: \n The title of Adolf Hitler's autobiography 'Mein Kampf' is what when translated to English?",
  "QUESTION 14: \n Which of the following was the author of 'Username Evie'?",
  "QUESTION 15: \n In Terry Pratchett's Discworld novel 'Wyrd Sisters', which of these are not one of the three main witches?"
]

player = input("What is your name?")
sleep(1)  #delay execution of the next code

print(f"Hello {player}! Welcome to the world of books!")
sleep(2)
print("Let's explore how vast your knowledge in books is by taking this short quiz!📚")
sleep(2)
print("There are two levels of difficultyvin the game, Easy and Hard. If you make it past the easy round then look forward for the next level.")
sleep(5)

print("Ready?... Start!")
sleep(2)

correct_answers = []  #append values of total correct answers
qns = 15

while qns > 0:
    for question in questions:
        print(question)  #print each question in the list

        #Easy level
        if question == questions[0]:
            choices = ["1. J.R.R. Tolkien ",
                    "2. Terry Pratchett ",
                    "3. J.K. Rowling ",
                    "4. Daniel Radcliffe "]
            print(choices)    #list the choices
            answer = input("Answer: ")
            valid_answer = answer.isnumeric()
            if valid_answer:
                if answer == 3 :
                    print("Correct! Well done. \n")
                    correct_answers.append(1)  #append value to the no. of correct answers
                else:
                    print(f"Incorrect! The answer is {choices[2]} \n")
                    sleep(1)
            else:
                print("Incorrect! The answer must be a number. \n")
                continue

        elif question == questions[1]:
            choices = ["1. 1984 ",
                    "2. The Old Man and the Sea",
                    "3. Catcher and the Rye",
                    "4. To Kill a Mockingbird"]
            print(choices)
            answer = input("Answer: ")
            if answer == 1 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[0]}. \n")
                sleep(1)

        elif question == questions[2]:
            choices = ["1. Dracula ",
                    "2. The Strange Case of Dr. Jekyll and Mr. Hyde ",
                    "3. The Legend of Sleepy Hollow ",
                    "4. Frankenstein "]
            print(choices)
            answer = input("Answer: ")
            if answer == 4 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[3]}. \n")

        elif question == questions[3]:
            choices = ["1. The Little Prince ",
                    "2. The Lord of the Rings ",
                    "3. Harry Potter and the Philosopher's Stone ",
                    "4. The Da Vinci Code "]
            print(choices)
            answer = input("Answer: ")
            if answer == 2 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[1]}. \n")

        elif question == questions[4]:
            choices = ["1. Beatrix Potter ",
                    "2. Roald Dahl ",
                    "3. Dr. Seuss ",
                    "4. A.A. Milne "]
            print(choices)
            answer = input("Answer: ")
            if answer == 3 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[2]}. \n")

        elif question == questions[5]:
            choices = ["1. Ian Fleming ",
                    "2. Joseph Conrad ",
                    "3. John Buchan ",
                    "4. Graham Greene "]
            print(choices)
            answer = input("Answer: ")
            if answer == 1 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[0]}. \n")

        elif question == questions[6]:
            choices = ["1. 8 ",
                    "2. 5 ",
                    "3. 6 ",
                    "4. 7 "]
            print(choices)
            answer = input("Answer: ")
            if answer == 4 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[3]}. \n")

        elif question == questions[7]:
            choices = ["1. Joey Potter ",
                    "2. James Potter ",
                    "3. Frank Potter ",
                    "4. Hairy Potter "]
            print(choices)
            answer = input("Answer: ")
            if answer == 2 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[1]}. \n")

        elif question == questions[8]:
            choices = ["1. F. Scott Fitzgerald ",
                    "2. Stephen King ",
                    "3. William Golding ",
                    "4. Hunter Fox "]
            print(choices)
            answer = input("Answer: ")
            if answer == 3 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[2]}. \n")

        elif question == questions[9]:
            choices = ["1. A Case of Identity ",
                    "2. A Study in Scarlet ",
                    "3. The Sign of the Four ",
                    "4. The Doings of Raffles Haw "]
            print(choices)
            answer = input("Answer: ")
            if answer == 2 :
                print("Correct! Well done. \n")
                correct_answers.append(1)
            else:
                print(f"Incorrect! The answer is {choices[1]}. \n")
    break

#only proceed to next level if correct answers is >= 9
# using the len() which returns the number
# of elements in the list
if len(correct_answers) >= 9:
    print(f"Congratulations🎉🎊!You are a Bookworm! \nYou scored {len(correct_answers)} out of 10.")
    print("Would you like to go to the next level?\n")
    next_level = int(input("Press 1. for YES or Press 0. for NO \n"))
    if next_level == 1:
        for diff_question in diff_questions:
            print(diff_question)
            if diff_question == diff_questions[0]:
                choices = ["1. Lincoln Island ",
                        "2. Vulcania Island ",
                        "3. Prometheus Island ",
                        "4. Neptune Island "]
                print(choices)
                answer = input("Answer: ")
                if answer == 1 :
                    print("Correct! Well done. \n")
                    correct_answers.append(0)
                else:
                    print(f"Incorrect! The answer is {choices[1]}. \n")

            elif diff_question == diff_questions[1]:
                choices = ["1. Charles Dickens ",
                        "2. Hans Christian Andersen ",
                        "3. Lewis Carroll ",
                        "4. Oscar Wilde "]
                print(choices)
                answer = input("Answer: ")
                if answer == 2 :
                    print("Correct! Well done. \n")
                    correct_answers.append(1)
                else:
                    print(f"Incorrect! The answer is {choices[1]}. \n")

            elif diff_question == diff_questions[2]:
                choices = ["1. My Hatred ",
                        "2. My Sadness ",
                        "3. My Desire ",
                        "4. My Struggle "]
                print(choices)
                answer = input("Answer: ")
                if answer == 4 :
                    print("Correct! Well done. \n")
                    correct_answers.append(1)
                else:
                    print(f"Incorrect! The answer is {choices[3]}. \n")

            elif diff_question == diff_questions[3]:
                choices = ["1. Joe Sugg ",
                        "2. Zoe Sugg ",
                        "3. Joe Weller ",
                        "4. Alfie Deyes "]
                print(choices)
                answer = input("Answer: ")
                if answer == 1 :
                    print("Correct! Well done. \n")
                    correct_answers.append(1)
                else:
                    print(f"Incorrect! The answer is {choices[0]}. \n")

            elif diff_question == diff_questions[4]:
                choices = ["1. Granny Weatherwax ",
                        "2. Nanny Ogg ",
                        "3. Winny Hathersham ",
                        "4. Magrat Garlick "]
                print(choices)
                answer = input("Answer: ")
                if answer == 3 :
                    print("Correct! Well done. \n")
                    correct_answers.append(1)
                else:
                    print(f"Incorrect! The answer is {choices[2]}. \n")

        print(f"Congratulations on making it through both levels🎉🎊!You are a Bookworm! \nYou scored {len(correct_answers)} out of 15.")
        print("Thankyou for playing the game my fellow nerd!")
    else:
        print("Thankyou for playing the game my fellow nerd!")

else:
    print(f"Congratulations🎉 \nYou scored {len(correct_answers)} out of 10.")
    print("Thankyou for playing the game!")
        