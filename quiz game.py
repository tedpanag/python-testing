print("Welcome to my geography quiz")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print ("Ok! Lets play :D") 

anwser = input ("In what continent does Greece belong to? ")
if anwser.lower() == "europe":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

anwser = input ("In what continent does Japan belong to? ")
if anwser.lower() == "asia":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

anwser = input ("In what continent does Egypt belong to? ")
if anwser.lower() == "africa":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

anwser = input ("In what continent does USA belong to? ")
if anwser.lower() == "america":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

print ("You got" + str(score) + "questions correct")
print ("You got" + str((score/ 4 ) * 100) + "%.")

anwser = input ("Did you like the quiz? ")
if anwser.lower() == "yes":
    print ("thanks!")
else:
    print ("sad")