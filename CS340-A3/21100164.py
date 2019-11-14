#
# Written by: Matloob Altaf 
#
#Front end is written in PyInquirer
#
import PyInquirer
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from examples import custom_style_2
# Maximum capacity of the both tables as given in the assignment
cap = 11
hash_1 = [None]*cap
hash_2 = [None]*cap
loop = True

# Functions

# Hash function one as given in the assignment
def hashFunc_1(input):
    global cap
    return input%cap
# Hash function two as given in the assignment
def hashFunc_2(input):
    global cap
    return (input//cap)%cap
# Serch in hash table one
def search_1(input):
    global hash_1
    global hash_2
    i = hashFunc_1(input)
    if(hash_1[i] == input):
        return i
    else:
        return None
# Search in hash table two
def search_2(input):
    global hash_1
    global hash_2
    i = hashFunc_2(input)
    if(hash_2[i] == input):
        return i
    else:
        return None
# General Search function
def search(input):
#    i = search_1(input)
    if(search_1(input) != None):
        print(input, " present in the tabe1[", search_1(input), "]")
        return
    elif(search_2(input) != None):
        print(input, " present in the tabe2[", search_2(input), "]")
        return
    else:
        print(input, " not found.")
        return
# Print 
def printTables():
    print("Table 1")
    for keys in hash_1:
        if( keys == None):
            print("Empty", end = ("    "))
        else:
            print(keys, end = "   ")
    print("\n\n")
    print("Table 2")
    for keys in hash_2:
        if( keys == None):
            print("Empty", end= "    ")
        else:
            print(keys, end = "   ")
    print()
# Delete function to remove an entry
def delete(input):
    global cap
    global hash_1
    global hash_2
    if(search_1(input) != None):
        hash_1[search_1(input)] = None
        print(input, " Delated Successfullty")
        return
    elif(search_2(input) != None):
        hash_2[search_2(input)] = None
        print(input, " Delated Successfullty")
        return
    else:
        print(input, " not found")
        return
# Function to change hash function
def rehashing(input):
    global cap
    global hash_1
    global hash_2
    cap = cap*2
    prevHash_1 = hash_1
    hash_1 = [None]*cap
    for keys in prevHash_1:
        if(keys != None):
            insert(keys)
    prevHash_2 = hash_2
    hash_2 = [None]*cap
    for keys in prevHash_2:
        if(keys != None):
            insert(keys)
# Insert function to insert entries
def insert(input, c = 0, flag = 0):
    global cap
    global hash_1
    global hash_2
    if(c == cap):
        print("Cycle found for ", input)
        print("Rehashing...")
        rehashing(input)
    if(flag == 0):
        i = hashFunc_1(input)
        if(hash_1[i] != None):
            prevValue = hash_1[i]
            hash_1[i] = input
            c = c+1
            insert(prevValue, c, 1)
        else:
            hash_1[hashFunc_1(input)] = input
    elif (flag == 1):
        i = hashFunc_2(input)
        if(hash_2[i] != None):
            prevValue = hash_2[i]
            hash_2[i] = input
            c = c+1
            insert(prevValue, c, 0)
        else:
            hash_2[hashFunc_2(input)] = input
#
# This is the main// Front end 
#
class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
while (loop):
    questions00 =[
            {
                'type': 'list',
                'name': 'user',
                'message': 'What do you want to do?',
                'choices': ['Add a value in Hash Tables','Search a value in Hash Tables','Delete a value from Hash Tables', 'Print Hash Tables', 'Exit'],
            }
        ] 
    answers00 = prompt(questions00, style=custom_style_2)
    if answers00['user'] == 'Search a value in Hash Tables':
        questions01 =[
            {
                'type': 'input',
                'name': 'key',
                'message': 'Enter the value you want to search: ',
                'validate': NumberValidator
            }
        ]
        answers01 = prompt(questions01, style=custom_style_2)
        search(int(answers01['key']))
    elif answers00['user'] == 'Add a value in Hash Tables':
        questions01 =[
            {
                'type': 'input',
                'name': 'key',
                'message': 'Enter the value you want to add: ',
                'validate': NumberValidator
            }
        ]
        answers01 = prompt(questions01, style=custom_style_2)
        insert(int(answers01['key']))
        print(answers01['key'], " added successfully")
    elif answers00['user'] == 'Delete a value from Hash Tables':
        questions01 =[
            {
                'type': 'input',
                'name': 'key',
                'message': 'Enter the value you want to delete: ',
                'validate': NumberValidator
            }
        ]
        answers01 = prompt(questions01, style=custom_style_2)
        delete(int(answers01['key']))
    elif answers00['user'] == 'Print Hash Tables':
        printTables()
    elif answers00['user'] == 'Exit':
        loop = False