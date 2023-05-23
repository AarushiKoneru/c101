import random

response=str(input("To roll dice type y "))

while(response=="y"):
    no = random.randint(1,6)

    if(no==1):
        print("⚀, (1)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")
    
    elif(no==2):
        print("⚁, (2)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")

    elif(no==3):
        print("⚂, (3)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")


    elif(no==4):
        print("⚃, (4)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")

    elif(no==5):
        print("⚄, (5)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")

    elif(no==6):
        print("⚅, (6)")
        response = str(input("Roll dice again? y for continue, n for exit "))
        if (response=="n"):
            print("End of turn")


           
    