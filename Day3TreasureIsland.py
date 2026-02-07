print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/_____/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choose=str(input("Choose L for Left and R for Right: "))

if choose=='L':
    print("You have safely reached to next point")
    action=str(input("Do you want to Swim S or Wait W"))
    if action=='W':
        print("You have safely reached to next point")
        door=str(input("Which door do you Want to choose Red R, Yellow Y, Blue B"))
        if door=='Y':
            print("The treasure is found!!! You have WON!!!")
        elif door=='R':
            print("You have been burnt with fire!!!")
        elif door=='B':
            print("The beasts have eaten you alive")
        else:
            print("The treasure is NOT found!!! Game Over!!!")
    elif action=='S':
        print("You have been eaten by Sharks")
    else:
        print("Game Over")

elif choose=='R':
    print("Fallen into the hole!!! Game Over!!! ")
else:
    print("Game Over")

