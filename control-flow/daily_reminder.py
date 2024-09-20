task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

prefix = ""
if time_bound == 'yes':
    prefix = "Reminder" 
else:
    prefix = "Note"

match priority:
    case 'high':
        reminder = f"{prefix}: '{task}' is a high priority task"
    case 'medium':
        reminder = f"{prefix}: '{task}' is a medium priority task"
    case 'low':
        reminder = f"{prefix}: '{task}' is a low priority task"

if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."


print(reminder)