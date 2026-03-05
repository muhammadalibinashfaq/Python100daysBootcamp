import random
guess=random.randint(1,100)
print(f"Hey, The number is {guess}")

is_True=True
life=5
while is_True:
    num=int(input("The number guess: "))
    if num==guess:
        is_True=False
        print("Yea boiii")
    elif num>guess:
        print("Too High")
        life -= 1
        print(f"Life's: {life}")

    else:
        print("Too Low")
        life -= 1
        print(f"Life's: {life}")
    if life==0:
        print("You Lost!!!")

        print(f"The number is {guess}")
        is_True=False




