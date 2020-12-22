#!/usr/bin/env python
import sys
from datetime import date

# Methods

def help():
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')

# Adding New Todo
def add(todo_add):
    # Writing in todo.txt
    f = open("todo.txt", "a")
    f.write(todo_add + "\n")
    f.close()

    # Writing in done.txt
    today = date.today()
    w = open("done.txt", "a")
    w.write("x " + str(today.strftime("%Y-%m-%d")) + " " + todo_add + "\n")
    w.close()

def list_todo():
    lines_exists = 0
    todo_file = open("todo.txt","r")
    file_content = todo_file.read()
    final_list = file_content.split("\n")
    for i in final_list: 
        if i: 
            lines_exists += 1
    for i in final_list:
        if lines_exists >= 1:
            print("[" + str(lines_exists) + "] " + i)
            lines_exists -= 1

# 0. Default - No Args
if len(sys.argv) < 2:
    help()

# 1. Help
elif sys.argv[1] == 'help':
    help()

# 2. List all pending todos
elif sys.argv[1] == 'ls':
    list_todo()

# 3. Add a new todo
elif sys.argv[1] == 'add':
    if len(sys.argv) == 3:
        add(sys.argv[2])
    else:
        print("Error: Missing todo string. Nothing added!")

# 4. Delete a todo item
elif sys.argv[1] == 'del':
    print('Delete number: ' + sys.argv[2])

# 5. Mark a todo item as completed
elif sys.argv[1] == 'done':
    print('Done number: ' + sys.argv[2])

# 6. Generate a report
elif sys.argv[1] == 'report':
    print('Generating Report...')