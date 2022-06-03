import random
print("This is a Guessing Game")
number=random.randint(1,9)
print(number)
chances = 0 
while (chances<5):
    yourNumber=int(input("Enter your number :-- "))
    if (yourNumber == number):
        print("you won")
    elif(yourNumber < number):
        print("you are too close to the number , enter a higher number than : ", yourNumber)
    else:
        print("you are too close to the number , enter a less number than : ", yourNumber)
    chances += 1 
    
if(chances == 5):
    print("you loose , the number is cd : " , number)   