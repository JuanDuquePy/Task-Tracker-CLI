from os import path
import argparse
import json
import datetime
import sys

parser = argparse.ArgumentParser(
    prog="Task Tracker",
    description="CLI manager to add, update and list tasks, stored in a JSON file.",
    epilog="Developed by Juan Duque",
)
# Create database
parser.add_argument("-c", "--create", help="create database json", action="store_true")
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


def create_json():
    """Create an empty JSON file named 'task.json' to store task data.

    The function checks if the file already exists. If it does not exist, it
    creates it with an initial content of an empty list (`[]`). In case the
    file is already present, it informs the user that it is not necessary to
    create it again.

    """
    try:
        if path.isfile("task.json") != True:
            with open("task.json", "w") as database:
                json.dump([], database)
        else:
            print("It already exists, there is no need to create a new database.")
    except OSError:
        print(f"System error when creating the file | {OSError}.")
    except Exception:
        print(f"An unexpected error occurred | {Exception}.")


def add(task):
    """Receives a list of three strings representing the data of a task to be
    added to a dictionary. to be added to a dictionary.

    Args:
        task (list): List with string elements.

    List parameters:
        title: (str): Task title.
        description (str): Task description.
        status (str): Task status (todo, done, progress)

    """
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
    if not path.isfile("task.json"):
        error_message = (
            "The database does not exist, you must create one to"
            "add a task.\nTo create one you can use -c or -create "
        )

        print(error_message)
        sys.exit()

    try:
        # Cargar tareas existentes
        with open("task.json", "r") as database:
            existing_taks = json.load(database)
        # Asignar un ID único basado en el número de elemntos existentes
        new_task["id"] = len(existing_taks) + 1
        # Agregamos la tarea nueva a la lista.
        existing_taks.append(new_task)
        # Guardar las tareas actualizadas en la BD
        with open("task.json", "w") as database:
            json.dump(existing_taks, database, indent=4)

        print(f"tarea '{title}' añadida con exito")
    except json.JSONDecodeError as e:
        print(
            "Error reading the database. verify that the json file is in the"
            f"correct format. {e}"
        )
    except Exception as e:
        print(f"An unexpected error occurred | {e}")


def update(task_id: int, updates):
    """Updates the values of a task in the JSON file based on its ID.

    Args:
        task_id (int): ID of the task to be updated.
        updates (_type_): A list containing the new task values:
            - title: (str): New task title.
            - description (str): New task description.
            - status (str): New task status (todo, done, progress)

    """
    title, description, status = updates
    try:
        with open("task.json", "r") as database:
            read = json.load(database)
        for task in read:
            if task["id"] == int(task_id):
                print(task["title"])
                task["title"] = title
                task["description"] = description
                task["status"] = status
                task["updateAt"] = datetime.datetime.now().strftime("%d-%m-%Y")
                break
            else:
                print("The task was not found")
        with open("task.json", "w") as database:
            json.dump(read, database, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON | {e}")
    except KeyError as e:
        print(f"Error | {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def delete(id):
    """Delete a task from the JSON file by its ID.

    Args:
        id (int): Task id
    """
    with open("task.json", "r") as database:
        read = json.load(database)
    for i, diccionario in enumerate(read, start=1):
        id_diccionario = i
        id_tarea = diccionario["id"]
    try:
        if id_tarea == id:
            borrar = id_diccionario - 1
            read.pop(borrar)
            print(f"The taks with id: {i} was deleted")
        else:
            print("The task does not exist")
    except FileNotFoundError as e:
        print(f"File not found | {e}")

    with open("task.json", "w") as file:
        json.dump(read, file, indent=4)


def list():
    """It reads the file 'task.json', loads its content and displays each task
    with its respective information.
    """
    try:
        with open("task.json", "r") as database:
            data = json.load(database)
        for i in data:
            print("-" * 10 + " TASK " + "-" * 10)
            for a in i:
                print(f"{a} : {i[a]}")
    except FileNotFoundError as e:
        print(f"Error: The file 'task.json' was not found. | {e}")
    except json.JSONDecodeError:
        print(f"Error: The content of the file is not a valid JSON. | {e}")
    except Exception as e:
        print(f"An unexpected error occurred. | {e}")


def list_todo(todo):
    """It reads the file 'task.json', loads its content and displays each task
    with its respective information.
    """
    try:
        with open("task.json", "r") as database:
            data = json.load(database)
        for i in data:
            if i["status"] == todo:
                print(i)
    except FileNotFoundError as e:
        print(f"Error: The file 'task.json' was not found. | {e}")
    except json.JSONDecodeError:
        print(f"Error: The content of the file is not a valid JSON. | {e}")
    except Exception as e:
        print(f"An unexpected error occurred. | {e}")


def list_done(done):
    """It reads the file 'task.json', loads its content and displays each task
    with its respective information.
    """
    try:
        with open("task.json", "r") as database:
            data = json.load(database)

        for i in data:
            if i["status"] == done:
                print(i)
    except FileNotFoundError as e:
        print(f"Error: The file 'task.json' was not found. | {e}")
    except json.JSONDecodeError:
        print(f"Error: The content of the file is not a valid JSON. | {e}")
    except Exception as e:
        print(f"An unexpected error occurred. | {e}")


def list_progress(progress):
    """It reads the file 'task.json', loads its content and displays each task
    with its respective information.
    """
    try:
        with open("task.json", "r") as database:
            data = json.load(database)
        for i in data:
            if i["status"] == progress:
                print(i)
    except FileNotFoundError as e:
        print(f"Error: The file 'task.json' was not found. | {e}")
    except json.JSONDecodeError:
        print(f"Error: The content of the file is not a valid JSON. | {e}")
    except Exception as e:
        print(f"An unexpected error occurred. | {e}")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.create:
        create_json()
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
