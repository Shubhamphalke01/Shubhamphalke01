# /love calculator/
import random
import math

input("what is your name : ")
input("what is their name : ")

loveScore=random.randrange(0,100)
loveScore=math.floor(loveScore)

if loveScore > 70:

    print(f'your love score is {loveScore}"%" you love each other, your love is true')
    


elif loveScore > 30 and loveScore <= 70:

    print(f'love score is {loveScore}"%"')

elif loveScore <= 30:

    print(f'your love score is {loveScore}"%" you both go together like oil and water')


