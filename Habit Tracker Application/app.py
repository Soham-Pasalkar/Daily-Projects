import json
from datetime import date

today = str(date.today()) #str because json cannot store date objects
file = open("habits.json", "r") #reads raw text (string format) and stores it as file object
habits = json.load(file) #converts string data to json format

habit = input("Habit Name : ").strip().lower()

if habit in habits:
    if today not in habits[habit]:
        habits[habit].append(today)
else:
    habits[habit] = [today]

file = open("habits.json","w") 
json.dump(habits,file,indent=4) #writes to json file

print("Habit Tracked Successfully!")
file.close()