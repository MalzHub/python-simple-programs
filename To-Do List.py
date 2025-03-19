tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    print("\nOptions: [add] [remove] [exit]")
    choice = input("What would you like to do? ").strip().lower()

    if choice == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "remove":
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
    elif choice == "exit":
        break
    else:
        print("Invalid choice!")
