word=input("enter any 6 letter word ")#(asking user to enter any six letter number)
print(word)
secret=["_","_","_","_","_","_"]#(six empty space for each letter of the word)
ui=input("guess any letter from word ")#asking user to guess the letter
tries=1#no of tries 

while tries<6:#user will get 5 tries altogether
  
    if ui==word[0]:#if user gues the first letter
      secret.pop(0)#deleting the space in first index
      secret.insert(0,word[0])#adding the user guess
      print(secret)
      ui=input("gues another letter ")
   
    elif ui==word[1]:
      secret.pop(1)#removing the space in second index
      secret.insert(1,word[1])#adding the user guess of second index

      print(secret)
      ui=input("guess another letter ")
      
    elif ui==word[2]:
      secret.pop(2)
      secret.insert(2,word[2])
      print(secret)
      ui=input("gues another letter ")
      
    elif ui==word[3]:
      secret.pop(3)
      secret.insert(3,word[3])
      print(secret)
      ui=input("gues another letter ")
      

    elif ui==word[4]:
      secret.pop(4)
      secret.insert(4,word[4])
      print(secret)
      ui=input("gues another letter ")
      
    elif ui==word[5]:
      secret.pop(5)
      secret.insert(5,word[5])
      print(secret)  
      ui=input("gues another letter ")
      
    else:
      print("this letter is not in the word") 
      ui=input("gues another letter")
    tries=tries+1

ui=input("now guess the word")
if ui==word:
   print("congratulation u guess the right word")
else:
   print("sorry, try again")


   