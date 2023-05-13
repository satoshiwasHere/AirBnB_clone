PROJECT DESCRIPTION: 0x00. AirBnB CLONE - THE CONSOLE:



Airbnb clone a ready-made software that can help businesses quickly set up their own rental platform similar to Airbnb. This project has basic features and capabilities found on Airbnb.
This is the initial phase of the AirBnB clone project.

COMMAND INTERPRETER DESCRIPTION

A command interpreter is program that interprets and executes commands given by a user or a program. It reads in lines of text that the user enters and then carries out the requested commands. It is also known as a command-line interpreter or a shell.
This will serve as the interface of our application with customized limited number of commands that are tailor made for usage on the clone AirBNB site
It will serve as a frontend or user interface of our web application. 

Basic commands available are:

1. Display
2. Create
3. Update 
4. Retrieve
5. Do operations e.g count...
6. Destroy 

HOW TO START IT

To start the command interpreter, use the built-in function input(). This function takes a string argument which is the prompt displayed to the user. Input() will then wait for the user to type in a command and press enter. The command entered by the user will then be stored in a variable, which can then be used for further processing.

For example: 

command = input("Enter a command: ")

print("You entered:", command)

HOW TO USE. 

The command interpreter is available in two modes 

INTERACTIVE MODE:

In Interactive mode, the user can enter commands into the console and run them. After each command is run, the console will display a prompt (hbnb) to indicate that it is ready to accept a new command. This process can continue until the user exits or terminates the program.

Example:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

NON-INTERACTIVE:
In Non-interactive mode, the shell will be run with a command piped into it for execution, and no prompt or further input from the user will be required.

Example:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
