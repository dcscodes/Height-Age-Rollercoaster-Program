# Greeting/start of program.
print("Welcome to the rollercoaster!")

# Asks user for their height.
height = int(input("What is your height in cm?\n"))
# Initializes bull variable.
bill = 0

# Program continues if users height meets requirement, continues to ask them their age and depending on said age, bill variable is increased appropriately.
if height >= 120:
  print("You can ride the rollercoaster!")
  
  age = int(input("What is your age?\n"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
    
  # Asks user if they want a picture taken for an extra $3, if yes, bill variable increased by 3.  
  photoOption = input("Would you like a photo taken for an extra $3?\n'y' = yes 'n' = no\n")
  if photoOption == "y":
    bill += 3
    print(f"You'll be able to pick up your photo after exiting the ride! Your bill is ${bill}.")
    
  # Gives user their final bill/total.
  print(f"Your final bill is ${bill}")
  
# If users entered height falls under required height limit, program closes.
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")