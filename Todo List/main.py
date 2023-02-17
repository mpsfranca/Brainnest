from database import Database

def main():
    db = Database.Database()

    while True:
        inp = input("""Welcome to the ToDo app, select an option:\n1) Add new todo\n2) List todos\n3) Remove a todo\n4) Exit\n""")
        if inp not in ["1","2","3","4"]:
            print("Invalid Option")
            continue
        else:
            match(inp):
                case "1":
                    task = input("What is the task?\n")
                    db.add_todo(task)
                case "2":
                    db.print_items()
                case "3":
                    db.print_items()
                    id = input("Enter the id of the todo to be deleted\n")
                    db.remove_todo(id)
                case "4":
                    break

main()