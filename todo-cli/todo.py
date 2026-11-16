import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Title cannot be empty.")


def get_index(tasks, action):
    show_tasks(tasks)
    try:
        num = int(input(f"Task number to {action}: "))
        if 1 <= num <= len(tasks):
            return num - 1
    except ValueError:
        pass
    print("Invalid task number.")
    return None


def complete_task(tasks):
    if not tasks:
        return print("Nothing to complete.")
    i = get_index(tasks, "complete")
    if i is not None:
        tasks[i]["done"] = True
        save_tasks(tasks)
        print("Marked as done.")


def delete_task(tasks):
    if not tasks:
        return print("Nothing to delete.")
    i = get_index(tasks, "delete")
    if i is not None:
        removed = tasks.pop(i)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    menu = """
=== TO-DO LIST ===
1. View tasks
2. Add task
3. Complete task
4. Delete task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()