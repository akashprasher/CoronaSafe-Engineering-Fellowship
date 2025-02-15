# File Containg Required Method/Function for todo.py
# from actions import help_cmd, add, list_todo, delete_todo, done_todo, report
import os
import sys
from os import path
from datetime import date

# 1 - Function Help - Show Commands -- ./todo help


def help_cmd():
    usage="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(usage.encode('utf8')) # Printing using UTF-8, using print() directly giving unwated symbols as result

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
            current_todo = "[" + str(index_inverse) + "] " + final_list[i] + "\n"
            sys.stdout.buffer.write(current_todo.encode('utf8')) # Printing using UTF-8, using print() directly giving unwated symbols as result
            index_inverse -= 1
        todo_file.close
    else:
        print('There are no pending todos!')  # error

# 4 Delete Todo -- ./todo del arg1 ...


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

# 5 Done todo and shifting to done.txt from todo.txt -- ./todo done arg1 ...


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

# 6 Telly Report -- ./todo report


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
