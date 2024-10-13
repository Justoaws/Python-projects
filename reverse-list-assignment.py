# Practice reversing a list and transferring its elements into a new list using loops.
# Write a Python program that works with the list called laura_things containing 
# the following items:

laura_things = ["sewing machine", "scissor", "cutting mat", "television"]

laura_things_reserved = []

laura_things_reserved.append("television")
laura_things_reserved.append("cutting mat")
laura_things_reserved.append("scissor")
laura_things_reserved.append("sewing machine")

print(f"the new order of {laura_things} is this : \n{laura_things_reserved}")

for thing in laura_things_reserved:
    print(thing)

print("The list has been successfully reversed!")
      
      