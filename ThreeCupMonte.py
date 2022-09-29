# Three Cup Monte Game
#we are importing the randome for getting random suffel list elements.
import random

#creating a list to use in the whole game.
mylist=["","O",""]

#creating a function for checking the prediction of player is true or false.
def game(nameOfList):
     guss=int(input("chose between 0 , 1 and 2: "))

    #we are using to check the the number choosen by the user is in between 0 to 2.
     while guss not in [0,1,2]:
          guss=int(input("chose between 0 , 1 and 2:"))
     random.shuffle(mylist)
     print(mylist)
     if mylist[guss]=="O":
          print(mylist)
          print("you won ")
          end_count()
          #calling end_count() function 

     else:
          print("you loss")
          end_count()
          #calling end_count () function

 #creating a function for checking that player want to play the game or want to exit         
def end_count():
     end_con=int(input("enter 1 to play again and 0 to exit: "))
     while end_con not in [0,1]:
          end_con=int(input("enter 1 to play again and 0 to exit: "))
     if end_con==0:
          pritn("Thanks For Playing Now You'r exit")
     else:
          print("you decided to continue playing game" )
          game(mylist)


game(mylist)
