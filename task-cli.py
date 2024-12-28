import argparse
import json

parser = argparse.ArgumentParser(
    prog="Task Tracker",
    description="CLI manager to add, update and list tasks, stored in a JSON file.",
    epilog="Developed by Juan Duque",
)
# Create database
parser.add_argument("-c", "--create", help="create database json", type=str)
# Adding a new task
parser.add_argument("-a", "--add", help="Adicciona una tarea", type=str)
# Updating and deleting task
parser.add_argument("-upd", "--update", help="Actualiza una tarea", type=str)
parser.add_argument("-del", "--delete", help="Elimina una tarea", action="store_true")
# Marking a task as in progress or done
parser.add_argument("-p", "--progress", help="Tarea en progreso", type=str)
parser.add_argument("-d", "--done", help="Tarea en realizada", type=str)
# Listing all task
parser.add_argument("-l", "--list", help="Listar las tareas", action="store_true")
# Listing task by status
parser.add_argument("-ld", "--list-done", help="Listar las tareas done")
parser.add_argument("-lt", "--list-todo", help="Listar las tareas todo")
parser.add_argument("-lp", "--list-progress", help="Listar las tareas progress")
# Search
parser.add_argument("-id", "--id", help="ID de la tarea", type=str)


def create_json(task_information, name):
    with open(name, "w") as database:
        json.dump(task_information, database)


def add():
    database = {
        "id": 2,
        "title": "prueba",
        "description": "prueba del json",
        "status": "Done",
        "createIn": "11-1-2021",
        "updateAt": "12-2-2021",
    }

    return database


taks_information = add()


def update():
    pass


def delete(id):
    with open("prueba.json", "r") as database:
        leer = json.load(database)
    for i in leer:
        p = i
    if leer[id] == leer[p]:
        del leer[id]

    with open("prueba.json", "w") as file:
        json.dump(leer, file, indent=4)


def list():
    with open("prueba.json", "r") as database:
        leer = json.load(database)

    for i in leer:
        print(i)
        for a in leer[i]:
            print(a, leer[i][a])


if __name__ == "__main__":
    args = parser.parse_args()

    if args.create:
        create_json(taks_information, args.create)
    elif args.add:
        add()
    elif args.update:
        update()
    elif args.delete:
        delete(args.id)
    elif args.list:
        list()
    else:
        print("The option does not exist if you need help: -h or --help")
