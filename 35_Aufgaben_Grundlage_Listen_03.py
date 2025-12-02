todo = []


while True:
    benutzereingabe = input("Bitte gib zu erledigende Aufgaben ein: ")
    if benutzereingabe != "fertig":
        todo.append(benutzereingabe)
    
    else:
        for i in range(len(todo)):
            print(f"{i + 1}. {todo[i]}")
        break