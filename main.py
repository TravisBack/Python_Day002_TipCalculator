print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? ")) / 100.0
people = float(input("How many people to split the bill? "))

portion = round((total + (total * percentage)) / people, 2)

print(f"Each person should pay: ${portion}")