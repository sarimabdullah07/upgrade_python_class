import random
hidden_num=random.randint(1,100)
print(hidden_num)
score=100

for i in range(5):
    guess=int(input("Guess a number between 1 to 100: "))
    if guess==hidden_num:
        print("You Guessed a right number.")
        print("score: ",score)
    elif guess<hidden_num:
        pass

