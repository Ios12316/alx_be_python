task = input("Enter your task:")
priority = input("Priority (high, medium, low):")
time_bound = input("Is it time-bound? (yes or no):")
match priority:
    case "high":
        reminder = f"'{task}' is of high priority task"
    case "medium":
        reminder = f"'{task}' is of medium priority task"
    case "low":
        reminder = f"'{task}' is of low priority task"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
if time_bound == "no":
    reminder += " doesn't requires immediate attention today!"
print(f"Reminder: {reminder}")
