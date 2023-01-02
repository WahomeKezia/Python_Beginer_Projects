# this is a sample madlib that I will used for my game of madibs
" Declaring My Variables "
verb1= input("Verb: ")
verb2= input("Enter verb: ")
noun1= input("Enter Noun: ")
noun2= input("Enter Noun: ")
noun3= input("Enter Noun: ")

global madlib

madlib = f" Once You have taken the {verb1} ,\n You will, {verb2}\n" \
         f" Gaze towards the {noun1}, you will know that \n That is where your {noun2} will feel at {noun3} "

print(madlib)

