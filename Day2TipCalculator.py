print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
discount=tip/100
discount1=bill*discount
discount2=bill+discount1

print(discount)
people = int(input("How many people to split the bill? "))
split= discount2/people
f_split=round(split,2)
print(f_split)

