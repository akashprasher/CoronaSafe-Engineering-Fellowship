# importing sys for getting argument
import sys
# Importing Function/Method Required from ./actions.py[required to run this file]
from actions import help_cmd, add, list_todo, delete_todo, done_todo, report

# checking number of arguments
length_argument = len(sys.argv)

# 1 cmd ./todo help
if length_argument == 1 or sys.argv[1] == 'help':
    help_cmd()

# 2 cmd ./todo add arg1 ...
elif sys.argv[1] == 'add':
    add(sys.argv)

# 3 cmd ./todo ls
elif sys.argv[1] == 'ls':
    list_todo()

# 4 cmd ./todo del arg1 ...
elif sys.argv[1] == 'del':
    if len(sys.argv) > 2:
        delete_todo(int(sys.argv[2]))
    else:
        print('Error: Missing NUMBER for deleting todo.')

# 5 cmd ./todo done arg1...
elif sys.argv[1] == 'done':
    if len(sys.argv) > 2:
        done_todo(int(sys.argv[2]))
    else:
        print('Error: Missing NUMBER for marking todo as done.')

# 6 cmd ./todo report
elif sys.argv[1] == 'report':
    report()
