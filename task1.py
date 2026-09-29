tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append([task, "Pending"])
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task[0], "-", task[1])

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task[0], "-", task[1])

            task_number = int(input("Enter task number to update: "))

            if 1 <= task_number <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_number - 1][0] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task[0], "-", task[1])

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Deleted:", deleted_task[0])
            else:
                print("Invalid task number!")

    # Mark Task as Completed
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task[0], "-", task[1])

            task_number = int(input("Enter task number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1][1] = "Completed"
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")