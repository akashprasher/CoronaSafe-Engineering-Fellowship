#!/usr/bin/env python
import sys
from datetime import date

# Methods

def help():
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')

# Adding New Todo
def add(todo_add):
    today = date.today()
    # Writing in todo.txt
    f = open("./txt_todo_data/todo.txt", "a")
    f.write(todo_add + "\n")
    f.close()

    # Writing in done.txt
    w = open("./txt_todo_data/done.txt", "a")
    w.write("x " + str(today.strftime("%Y-%m-%d")) + " " + todo_add + "\n")
    w.close()

def list_todo():
    lines_exists = 0
    todo_file = open("./txt_todo_data/todo.txt","r")
    file_content = todo_file.read()
    final_list = file_content.split("\n")
    for i in final_list: 
        if i: 
            lines_exists += 1
    for i in final_list:
        if lines_exists >= 1:
            print("[" + str(lines_exists) + "] " + i)
            lines_exists -= 1

# 1. Help
if sys.argv[1] == 'help':
    help()

# 2. List all pending todos
elif sys.argv[1] == 'ls':
    list_todo()

# 3. Add a new todo
elif sys.argv[1] == 'add':
    add(sys.argv[2])

# 4. Delete a todo item
elif sys.argv[1] == 'del':
    print('Delete number: ' + sys.argv[2])

# 5. Mark a todo item as completed
elif sys.argv[1] == 'done':
    print('Done number: ' + sys.argv[2])

# 6. Generate a report
elif sys.argv[1] == 'report':
    print('Generating Report...')