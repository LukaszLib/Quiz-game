while True:

    print("Welcome to the quiz game")

    playing = input("Do you want to play? ")

    if playing.lower() == "yes":
        print(" Great! Let's start with your first question")
    else:
        print(" Too bad. See you when you change your mind")
        break

    score = 0

    answer = input("How many planets are in the solar system? ")
    if answer.lower() == "8" or answer.lower() == "eight":
        print(" Great! lets move on to the next question")
        score += 1
    else:
        print(" Incorrect")

    answer = input("Was George Washington the first president of the USA? ")
    if answer.lower() == "yes":
        print(" Great! lets move on to the next question")
        score += 1
    else:
        print(" Incorrect")

    answer = input("What is the capital of Germany? ")
    if answer.lower() == "berlin" or answer.lower() == "berlin":
        print(" Great! lets move on to the next question")
        score += 1
    else:
        print(" Incorrect")

    answer = input("Who painted the Mona Lisa? ")
    if answer.lower() == "leonardo da vinci" or answer.lower() == "da vinci":
        print(" Great! lets move on to the next question")
        score += 1
    else:
        print(" Incorrect")

    print(" Congrats! You have achieved " + str(score) + " out of 4!" )
    print(" That is " + str((score/4) * 100) + "% Accuracy!" )

    #at the end, ask the player if he wants to try again or terminate the program
    play_again = input(' Do you want to play again? (Yes/No) ')
    if play_again.lower() == 'no':
        break

Test change