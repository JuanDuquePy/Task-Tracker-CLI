# Task Tracker CLI

Command line tool designed to manage and track tasks. tasks. Users will be able
to add, update and delete tasks as well as view a list of these tasks a list of
these tasks according to their status (all, done, progress).

Solution [Task Tracker](https://github.com/JuanDuquePy/Task-Tracker-CLI) challenge [Roadmap.sh](https://roadmap.sh/projects/task-tracker)

## Python version

It was built with Python version 3.12.3

## How to use

| comando               | Description                                           |
| --------------------- | ----------------------------------------------------- |
| -c or --create        | Creates the json where the tasks will be stored          |
| -a or --add           | Add a task                                      |
| -upd or --update      | Update an existing task                      |
| -del or --delete      | Delete a task                                    |
| -l or --list          | List all task                                |
| -ld or --listDone     | List the tasks done                          |
| -lt or listTodo       | List the tasks todo                            |
| -lp or --listProgress | List the tasks progress                    |
| -id or --id           | Used to identify a task with a specific ID |

### Example of use

create the json to store the tasks in case it does not exist

`python task-cli.py -c`

How to add a new task

Only three parameters should be sent here: title, status and description in
that order.

```bash
python task-cli.py -a "title" "desciption" "status"
```

To list all tasks or only by their status.

```bash
python task.py -l
python task.py -ld
python task.py -lt
python task.py -lp
```

Delete task

To delete a task you must use -id together with -del, the -id serves to
identify the task. identify the task.

> [!TIP]

I recommend that if you don't remember the id of your task list them all so that you can be sure of the id of the task you want to delete.
be sure of the id of the task you want to delete.

```bash
python task.py -del -id <id task>
```

Update task

At the moment to update a task you must enter the three parameters
(in the same order as shown in the example).

```bash
python task.py -id <id task> -upd "title" "description" "status" 
```


## Project

Project Task Tracker URL:

