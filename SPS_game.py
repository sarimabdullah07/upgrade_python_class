import random
list=["stone","paper","siser"]
score=100
i=0
while(i<5):
    r=random.choice(list)
    g=input("\n\nEnter: [stone, paper, siser]\n")
    if(g==r):
        print("We guessed the same thing,",g)
    elif((r=="stone")and(g=="paper")):
        print("You win")
        print("I gussed",r)
    elif((r=="stone")and(g=="siser")):
        print("You lost")
        score-=20
        print("I gussed",r)
    elif((r=="paper")and(g=="stone")):
        print("You lost")
        score-=20
        print("I gussed",r)
    elif((r=="paper")and(g=="siser")):
        print("You win")
        print("I gussed",r)
    elif((r=="siser")and(g=="stone")):
        print("You win")
        print("I gussed",r)
    elif((r=="siser")and(g=="paper")):
        print("You lost")
        score-=20
        print("I gussed",r)
    else:
        print("Enter proper input as stone,paper,siser")
    pass
    i+=1
print("\nyour score:",score,"out of 100")
