import random
list=["Mango","Banana","Kiwi","Apple","Orange","Pineapple","Watermelon","Date","Fig","Muskmelon","Guava","Grapes","Papaya","Cherry"]
fruit_name=random.choice(list)
print(fruit_name)
i=0
point=100
while(i<5):
    guess=input("Guess any fruit name: ")
    if guess==fruit_name:
        print("You Won!")
        break
    else:
        if(i==0):
            print("Hint1: Fruit name starts with: ", fruit_name[0])
        elif(i==1):
            print("Hint2: Length of fruit name is ",len(fruit_name)," letters.")
        elif(i==2):
            b=fruit_name[0]+"_"*(len(fruit_name)-2)+fruit_name[-1]
            print("Hint4: It could be: ",b)
        elif(i==3):
            c=fruit_name[0]+fruit_name[1]+"_"*(len(fruit_name)-2)+fruit_name[-1]
            print("Hint5: Abe Anpadh kaheen ke...",c)
        else:
            print("Ja ghar ja tu....",fruit_name,"ye hai.")
    i+=1
    point-=20
print("Score: ",point)