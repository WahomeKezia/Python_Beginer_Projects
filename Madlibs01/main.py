from Madlibs01 import DeadPoets ,sogno_De_Volare
import random

#print("Hey There , Welcome to madlib "
     ## "Below are some of the most inspiring poems , "
     # "make your Guess and Make it exciting!!")


if __name__ == '__main__':
    m = random.choice( [ DeadPoets ,sogno_De_Volare])
    m.madlib()

