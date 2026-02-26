'''
1 for snake
-1 for water 
0 for gun
'''
import random

computer=random.choice([1,-1,0])
yourChoice=input('Enter your choice(s for snake,w for water and g for gun): ')
yourDict={"s":1,"w":-1,"g":0}
you=yourDict[yourChoice]

reverseDict={1:'Snake',-1:'Water',0:'Gun'}
print(f'You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}')

if(computer==you):
    print("It is a draw.")
# elif(computer==-1 and you==1): #computer-you = -2
#     print("You win!")

# elif(computer==-1 and you==0):#computer-you = -1
#     print("You lose!")

# elif(computer==1 and you==-1):#computer-you = 2
#     print("You lose!")

# elif(computer==1 and you==0):#computer-you = 1
#     print("You win!")

# elif(computer==0 and you==-1):#computer-you = 1
#     print("You win!")

# elif(computer==0 and you==1):#computer-you =  -1
#     print("You lose!")

# you lose when comp-you=-1 and 2 and win when comp-you is 1 and -2 as per the pattern so below code
# based on that logic

elif((computer-you)==-1 or(computer-you)==2):
    print("You lose!")

elif((computer-you)==1 or(computer-you)==-2):
    print("You win!")
else: 
    print('Something went wrong!!')