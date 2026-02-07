import random

rand_num=random.randint(0,2)

user=int(input("Rock '0', Paper '1', Scissors '2'"))

print("User")
if user==0:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    print(rock)

elif user==1:
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    print(paper)

else:
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    print(scissors)

print("Computer")
if rand_num==0:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    print(rock)

elif rand_num==1:
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    print(paper)

else:
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    print(scissors)

if user==0 and rand_num==0 or user==1 and rand_num==1 or user==2 and rand_num==2:
    print("Draw")
elif user==0 and rand_num==2 or user==1 and rand_num==0 or user==2 and rand_num==1:
    print("You have won.")
else:
    print("You have lost")

