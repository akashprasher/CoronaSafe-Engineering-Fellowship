# Importing Function/Method Required
import sys
from actions import help, add, list_todo, delete_todo, done_todo, report

# checking number of arguments
length_argument = len(sys.argv)

if length_argument == 1 or sys.argv[1] == 'help':
    help()

elif sys.argv[1] == 'add':
    add(sys.argv)

elif sys.argv[1] == 'ls':
    list_todo()

elif sys.argv[1] == 'del':
    if len(sys.argv) > 2:
        delete_todo(int(sys.argv[2]))
    else:
        print('Error: Missing NUMBER for deleting todo.')
        
elif sys.argv[1] == 'done':
    if len(sys.argv) > 2:
        done_todo(int(sys.argv[2]))
    else:
        print('Error: Missing NUMBER for marking todo as done.')

elif sys.argv[1] == 'report':
    report()