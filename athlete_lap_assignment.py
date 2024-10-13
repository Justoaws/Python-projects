# Write a python program that uses a list of four U.S. women atheltes who have completed 
# in the 400 meters at the Olympics. Your program should do the following :

athletes = ["Allyson Felix" , "Sanya Richards-Ross" , "Shaunae Miller-Uibo" , "Phyllis Francis"]

for athlete in range (len(athletes)):
    # print(f"{athletes[athlete]}: {athlete}")
    print(f"Lap {athlete + 1}:{athletes[athlete]} has completed their lap")

print("All athletes have completed their laps") 


