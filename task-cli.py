from os import path
import argparse
import json
import datetime

parser = argparse.ArgumentParser(
    prog="Task Tracker",
    description="CLI manager to add, update and list tasks, stored in a JSON file.",
    epilog="Developed by Juan Duque",
)
# Create database
parser.add_argument("-c", "--create", help="create database json", type=str)
# Adding a new task
parser.add_argument(
    "-a",
    "--add",
    help="Adicciona una tarea | Necesita Title, Description and Status",
    metavar=("title", "description", "status"),
    nargs=3,
    type=str,
)
# Updating and deleting task
parser.add_argument(
    "-upd",
    "--update",
    help="Actualiza una tarea",
    metavar=("title", "description", "satatus"),
    nargs=3,
    type=str,
)
parser.add_argument("-del", "--delete", help="Elimina una tarea", action="store_true")
# Listing all task
parser.add_argument("-l", "--list", help="Listar las tareas", action="store_true")
# Listing task by status
parser.add_argument("-ld", "--listDone", help="Listar las tareas done")
parser.add_argument("-lt", "--listTodo", help="Listar las tareas todo")
parser.add_argument("-lp", "--listProgress", help="Listar las tareas progress")
# Search
parser.add_argument("-id", "--id", help="ID de la tarea", type=int)


def create_json(name: str):
    # Valida si la BD existe y si si no la crea y da una alerta
    try:
        if path.isfile(name) != True:
            if name.endswith(".json"):
                with open(name, "w") as database:
                    json.dump([], database)
            else:
                print("Debe ser un .json")
        else:
            print("Ya existe")
    except OSError:
        print(f"Error del sistema al crear el archivo {OSError}.")
    except Exception:
        print(f"Ocurrio un error inesperado {Exception}.")


def add(task):
    title, description, status = task
    new_task = {
        "id": None,
        "title": title,
        "description": description,
        "status": status,
        "createIn": datetime.datetime.now().strftime("%d-%m-%Y"),
        "updateAt": None,
    }
    # Verificamos si la BD existe
    if not path.isfile("prueba.json"):
        print("La bd de datos no existe, crea una")
        return
    try:
        # Cargar tareas existentes
        with open("prueba.json", "r") as database:
            existing_taks = json.load(database)
        # Todo: Corrergir: Validar que sea una lista (estructura esperada).
        # if not isinstance(existing_taks, (list, dict)):
        #   print("Error: La base de datos no tiene un formato válido.")
        #  return

        # Asignar un ID único basado en el número de elemntos existentes
        new_task["id"] = len(existing_taks) + 1
        # Agregamos la tarea nueva a la lista.
        existing_taks.append(new_task)
        # Guardar las tareas actualizadas en la BD
        with open("prueba.json", "w") as database:
            json.dump(existing_taks, database, indent=4)

        print(f"tarea '{title}' añadida con exito")
    except json.JSONDecodeError:
        print(
            "Error al leer la base de datos. verificar que el archivo json este en el formato adecuado"
        )
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")


def update(task_id: int, updates):
    title, description, status = updates

    with open("prueba.json", "r") as database:
        leer = json.load(database)

    for task in leer:
        if task["id"] == int(task_id):
            print(task["title"])
            task["title"] = title
            task["description"] = description
            task["status"] = status
            task["updateAt"] = datetime.datetime.now().strftime("%d-%m-%Y")
            break
        else:
            print("No se encontro la tarea")

    with open("prueba.json", "w") as file:
        json.dump(leer, file, indent=4)


def delete(id):
    with open("prueba.json", "r") as database:
        leer = json.load(database)
    for i, diccionario in enumerate(leer, start=1):
        id_diccionario = i
        id_tarea = diccionario["id"]
    if id_tarea == id:
        borrar = id_diccionario - 1
        leer.pop(borrar)
        print(f"borramos la tarea con el id: {i}")
    else:
        print("la tarea no existe")

    with open("prueba.json", "w") as file:
        json.dump(leer, file, indent=4)


def list():
    with open("prueba.json", "r") as database:
        data = json.load(database)
    for i in data:
        print("-" * 10 + " TASK " + "-" * 10)
        for a in i:
            print(f"{a} : {i[a]}")


def list_todo(todo):
    with open("prueba.json", "r") as database:
        data = json.load(database)

    for i in data:
        if i["status"] == todo:
            print(i)


def list_done(done):
    with open("prueba.json", "r") as database:
        data = json.load(database)

    for i in data:
        if i["status"] == done:
            print(i)


def list_progress(progress):
    with open("prueba.json", "r") as database:
        data = json.load(database)
    for i in data:
        if i["status"] == progress:
            print(i)


if __name__ == "__main__":
    args = parser.parse_args()

    if args.create:
        create_json(args.create)
    elif args.add:
        add(args.add)
    elif args.update:
        update(args.id, args.update)
    elif args.delete:
        delete(args.id)
    elif args.list:
        list()
    elif args.listDone:
        list_done(args.listDone)
    elif args.listTodo:
        list_todo(args.listTodo)
    elif args.listProgress:
        list_progress(args.listProgress)
    else:
        print("The option does not exist if you need help: -h or --help")
