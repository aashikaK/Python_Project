'''
1 for snake
-1 for water 
0 for gun
'''
computer=-1
yourChoice=input('Enter your choice(s for snake,w for water and g for gun): ')
yourDict={"s":1,"w":-1,"g":0}
you=yourDict[yourChoice]

elif(computer==-1 and you==1):
    print("You win!")

elif(computer==-1 and you==0):
    print("You lose!")

elif(computer==1 and you==-1):
    print("You lose!")

elif(computer==1 and you==0):
    print("You win!")

elif(computer==0 and you==-1):
    print("You win!")

elif(computer==0 and you==1):
    print("You lose!")

else: 
    print('Something went wrong!!')