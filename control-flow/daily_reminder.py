task = input("Enter your task description:")
task_priority = input("Enter the task's priority (high, medium, low):")
time_bound = input("Is it time-bound? (yes or no):")
match task_priority:
    case "high":
        reminder = f"The task '{task}' is of high priority task"
    case "medium":
        reminder = f"The task '{task}' is of medium priority task"
    case "low":
        reminder = f"The task '{task}' is of low priority task"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
if time_bound == "no":
    reminder += " doesn't requires immediate attention today!"
print(f"Reminder: {reminder}")
