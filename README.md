# AirBnB Clone - Python Language

## Introduction
This repository contains our team's first project, which involves creating a clone of the AirBnB website using the Python language. The project is implemented in a team of two, with Marc Pourias and Christophe Ngan as members.

## Project Description
The goal of this project is to develop a command-line interface that manages AirBnB objects. This is the initial step towards building a full web application. The project focuses on the following concepts:

* Python packages
* AirBnB clone

## Background Context
Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.

The first step of the project involves creating a command interpreter that handles the initialization, serialization, and deserialization of AirBnB objects. The command interpreter will allow users to perform various operations on the objects, such as creating, retrieving, updating, and deleting.

## Concepts Covered
During this project, we have gained experience in the following areas:

* Python packages
* Object serialization and deserialization
* Command-line interface development
* Data storage and retrieval

## Getting Started
To use the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Run the console.py script.
3. In the interactive mode, you can enter various commands to manage AirBnB objects.
4. Use the help command to get a list of available commands and their usage.

## Command Examples
The following are examples of commands you can use in the console:

* `update <class name> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and id by adding or updating an attribute.
    - Example: `update User 1234-1234-1234 email "example@email.com"`

* `help <command>`: Provides information and usage instructions for a specific command.
    - Example: `help create`

* `quit`: Exits the console.
    - Example: `quit`

* `EOF`: Exits the console (can be used by pressing Ctrl + D).
    - Example: `Press Ctrl + D to exit`

* `create <class name>`: Creates a new instance of the specified class and saves it.
    - Example: create BaseModel

* `show <class name> <id>`: Prints the string representation of an instance based on the class name and id.
    - Example: `show User 1234-1234-1234`

* `destroy <class name> <id>`: Deletes an instance based on the class name and id.
    - Example: `destroy Place 5678-5678-5678`

* `all or all <class name>`: Prints the string representation of all instances or all instances of a specific class.
    - Example: `all or all State`

Our shell should work like this in interactive mode:
```
sirothpech@LAPTOP-NAVGPF15:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
sirothpech@LAPTOP-NAVGPF15:~/holbertonschool-AirBnB_clone$
```
But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

## File Structure
The repository has the following structure:

```
.
├── models              # Directory containing the model classes.
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine
│       ├── __init__.py
│       └── file_storage.py
├── tests               # Directory containing unit tests for the project.
│   └── test_models
|       ├── __init__.py
│       ├── test_base_model.py
│       ├── test_user.py
│       ├── test_state.py
│       ├── test_city.py
│       ├── test_amenity.py
│       ├── test_place.py
│       ├── test_review.py
│       └── test_engine
│           ├── __init__.py
│           └── test_file_storage.py
├── console.py          # Entry point of the command interpreter.
├── README.md           # Detailed description of the project and instructions.
└── AUTHORS             # List of contributors to the repository.
```

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and python3 -c 'print(`__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Tests Cases
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* You have to use the unittest module
* All your test files should be python files (extension: `.py`)
* All your test files and folders should start with `test_`
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Authors
This project was realized Marc Pourias (@MarcP70) and Christophe Ngan (@Sirothpech)
