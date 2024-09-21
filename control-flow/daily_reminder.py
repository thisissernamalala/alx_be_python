task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""
if time_bound == 'yes':
    reminder = f"Reminder: {task}' is a" 
else:
    reminder = f"Note: {task}' is a"

match priority:
    case 'high':
        reminder += " high priority task"
    case 'medium':
        reminder += " medium priority task"
    case 'low':
        reminder += " low priority task"

if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."


print(reminder)