user_prompt="enter a todo:"
todos=[]

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index,todo in enumerate(todos):
                print(f"{index+1} - {todo}")
        case "edit":
            number = input("Enter number of todo to edit:")
            number = int(number)
            todos[number - 1] = input("new todo: ")

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # todos.__setitem__(number-1, input("new todo: "))
        case "complete":
            number = input("Enter number of todo to complete:")
            todos.pop(int(number) - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "exit":
            break

print("Done!")

a = "I am a string" \
    "on my " \
    "own"

print(a)