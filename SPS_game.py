import random
list=["rock","paper","scissor"]
score=100
i=0
while(i<5):
    r=random.choice(list)
    g=input("\n\nEnter: [rock, paper, scissor]\n")
    if(g==r):
        print("We guessed the same thing,",g)
    elif((r=="rock")and(g=="paper")):
        print("You win")
        print("I gussed",r)
    elif((r=="rock")and(g=="scissor")):
        print("You lost")
        score-=20
        print("I gussed",r)
    elif((r=="paper")and(g=="rock")):
        print("You lost")
        score-=20
        print("I gussed",r)
    elif((r=="paper")and(g=="scissor")):
        print("You win")
        print("I gussed",r)
    elif((r=="scissor")and(g=="rock")):
        print("You win")
        print("I gussed",r)
    elif((r=="scissor")and(g=="paper")):
        print("You lost")
        score-=20
        print("I gussed",r)
    else:
        print("Enter proper input as rock,paper,scissor")
    pass
    i+=1
print("\nyour score:",score,"out of 100")
