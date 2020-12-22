# File Containg Required Method/Function for todo.py

import os
from os import path
from datetime import date

# 1 - Function Help - Show Commands


def help_cmd():
    print("Usage :-")
    print("$ ./todo add \"todo item\"  # Add a new todo")
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')

# 2 Adding New Todo -- ./todo add arg1 arg2


def add(todo_add):
    # Writing in todo.txt
    todo_size = len(todo_add)
    if todo_size > 2:
        f = open("todo.txt", "a")
        for i in range(2, todo_size):
            f.write(todo_add[i] + "\n")
            print('Added todo: \"' + todo_add[i] + '\"')  # acknowledgement
        f.close()
    else:
        print('Error: Missing todo string. Nothing added!')  # error

# 3 List all todos -- ./todo ls


def list_todo():
    if path.exists("todo.txt"):  # checking for the todo file
        todo_file = open("todo.txt", "r")
        file_content = todo_file.read()
        final_list = file_content.split("\n")
        number_of_lines = len(final_list) - 1
        final_list.reverse()
        index_inverse = number_of_lines
        # loop for printing all todo exists in todo.txt
        for i in range(1, number_of_lines + 1):
            print("[" + str(index_inverse) + "] " + final_list[i])
            index_inverse -= 1
        todo_file.close
    else:
        print('There are no pending todos!')  # error

# 4 Delete Todo


def delete_todo(del_number):
    # Getting Todos
    todo_file = open("todo.txt", "r")
    file_content = todo_file.read()
    final_list = file_content.split("\n")
    todo_file.close

    # Deleting Todo
    if len(final_list) > del_number > 0:
        todo_file = open("todo.txt", "w")
        for todo in final_list:
            if todo != str(final_list[del_number - 1]):
                if todo == '':
                    continue
                else:
                    todo_file.write(todo + "\n")
        print('Deleted todo #' + str(del_number))  # acknowledgement
        todo_file.close
    else:
        print('Error: todo #' + str(del_number) +
              ' does not exist. Nothing deleted.')  # error

# 5 Done todo and shifting to done.txt from todo.txt


def done_todo(done_number):
    # Getting Todos
    todo_file = open("todo.txt", "r+")
    file_content = todo_file.read()
    final_list = file_content.split("\n")
    todo_file.close

    # Done Todo
    if len(final_list) > done_number > 0:
        today = date.today()
        done_file = open("done.txt", "a")
        done_file.write("x " + str(today.strftime("%Y-%m-%d")) +
                        " " + str(final_list[done_number - 1]) + "\n")
        print('Marked todo #' + str(done_number) +
              ' as done.')  # acknowledgement
        done_file.close
        todo_file = open("todo.txt", "w")
        for todo in final_list:
            if todo != str(final_list[done_number - 1]):
                if todo == '':
                    continue
                else:
                    todo_file.write(todo + "\n")
        print('Deleted todo #' + str(done_number))  # acknowledgement
        todo_file.close
    else:
        print('Error: todo #' + str(done_number) + ' does not exist.')  # error

# 6 Telly Report


def report():
    # Getting Remainning Todo
    today = date.today()
    todo_file = open("todo.txt", "r+")
    file_content = todo_file.read()
    pending = file_content.split("\n")
    todo_file.close
    # Getting Completed Todo
    todo_file = open("done.txt", "r+")
    file_content = todo_file.read()
    completed = file_content.split("\n")
    todo_file.close
    # Printing Report as per format
    print(str(today.strftime("%Y-%m-%d")) + " Pending : " +
          str(len(pending) - 1) + " Completed : " + str(len(completed) - 1))
