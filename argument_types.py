# positional argument
def result(name,roll_no,marks):
    print("Name: ",name,"\nRoll number: ",roll_no,"\nPercentage: ",round(sum(marks)/len(marks),2))
result("Sarim",1704,[94,89,92,87,88,97])
'''
we cannot change the position of arguments while calling a function.
'''

# keyworded argument
def result(name,roll_no,marks):
    print("\nName: ",name,"\nRoll number: ",roll_no,"\nPercentage: ",round(sum(marks)/len(marks),2))
result(roll_no=624,marks=[94,89,92,87,88,97],name="Abdullah")
'''
we can assign keywords to the functions while calling,
we can change the position of arguments by using keywords,
note: The keywords should match the actual argument (parameter) names
'''

# arbitrary argument
def area_of_circle(name,*marks):
    total=sum(marks)
    print("\n",name,"\n",marks,"\n","Total_Marks= ",total)
area_of_circle("Circle",23,55,76,87,90)

# keyworded arbitrary argument
def KAA(intro,**data):
    print("\n",intro)
    print(data)
KAA("Keyworded Arbitrary Arguments stores as a dictionary",name="Sarim",roll_no=812,marks=872,percentage=93.47)