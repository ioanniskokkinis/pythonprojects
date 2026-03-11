print("Welcome to Task Manager")

# 1. Ορίζουμε τη λίστα ΕΞΩ από το loop
tasks = [] 

# 2. Παίρνουμε την πρώτη επιλογή
choice = input("\nPlease insert a number (1-4): ")

while choice != '4':
    if choice == '1':
        n = input("Enter the new task: ")
        tasks.append(n)
        print("Task added!")
        
    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
    elif choice == '3':
        index = int(input("Which task number is completed? "))
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")

    choice = input("\nWhat's next? (1-4): ")

print("Bye user!")