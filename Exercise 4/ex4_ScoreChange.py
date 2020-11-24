import random

score=[]
scorenew=[]

for i in range(1,21):
    score.append(str(random.randint(50,95)))
    score.append("\n")

f = open("ex4_scores.txt","w+")
f.writelines(score)
f.close()