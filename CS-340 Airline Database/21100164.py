# this file creates a new database using create_db.sql


from __future__ import print_function, unicode_literals
import mysql.connector as connector
import PyInquirer
import regex
from prettytable import from_db_cursor
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_2

from random import randint
from art import *
tprint("SIAL Airline")

mydb = connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Ptg61mysql",
    db = "airline"
)
dbcursor = mydb.cursor(buffered=True)


addFlight = ("INSERT INTO Flights"
    "(f_id, f_date, f_departure_time, f_arrival_time, f_departure_airport, f_arrival_airport, f_fare)"
    "VALUES(%s,%s,%s,%s,%s,%s,%s)")

addPassenger = ("INSERT INTO Passengers"
    "(p_id, p_name,p_address,p_contact,p_nationality)"
    "VALUES(%s,%s,%s,%s,%s)")
addTicket = ("INSERT INTO Tickets (t_id, t_passenger_id, t_flight_id) Values(%s,%s,%s)")

updatePassenger = ("UPDATE Passengers SET p_name = %s, p_address = %s, p_contact = %s, p_nationality = %s WHERE p_id = %s")

updateFlight = ("UPDATE Flights SET f_date = %s, f_departure_time = %s, f_arrival_time = %s, f_departure_airport = %s, f_arrival_airport = %s, f_fare = %s WHERE f_id = %s")

deleteFlight = ("DELETE FROM Flights WHERE f_id = %s")

deleteTicket = ("DELETE FROM Tickets WHERE t_id = %s")

viewFlight = ("SELECT * FROM Flights WHERE (f_date = %s AND f_arrival_airport = %s) OR (f_date = %s AND f_departure_airport = %s)")

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

class TimeValidator(Validator):
    def validate(self, document):
        ok = regex.match('(?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid Time',
                cursor_position=len(document.text))  # Move cursor to end

class DateValidator(Validator):
    def validate(self, document):
        ok = regex.match('((?:(?:[0-2]?\\d{1})|(?:[3][01]{1}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid Date',
                cursor_position=len(document.text))  # Move cursor to end

class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end

class IATAValidator(Validator):
    def validate(self, document):
        dbcursor.execute("SELECT COUNT(a_name) FROM Airports WHERE a_iata = %s OR a_iata = %s", (document.text, document.text.upper()))
        result = dbcursor.fetchall()
        if not result[0][0]:
            raise ValidationError(
                message='Airport doesn\'t exist in database',
                cursor_position=len(document.text))  # Move cursor to end

class FlightIdValidator(Validator):
    def validate(self, document):
        dbcursor.execute("SELECT COUNT(*) FROM Flights WHERE f_id = %s", (document.text,))
        result = dbcursor.fetchall()
        if not result[0][0]:
            raise ValidationError(
                message='Flight doesn\'t exist in database',
                cursor_position=len(document.text))  # Move cursor to end

class PassengerIdValidator(Validator):
    def validate(self, document):
        dbcursor.execute("SELECT COUNT(*) FROM Passengers WHERE p_id = %s", (document.text,))
        result = dbcursor.fetchall()
        if not result[0][0]:
            raise ValidationError(
                message='Passenger doesn\'t exist in database',
                cursor_position=len(document.text))  # Move cursor to end

class TicketIdValidator(Validator):
    def validate(self, document):
        dbcursor.execute("SELECT COUNT(*) FROM Tickets WHERE t_id = %s", (document.text,))
        result = dbcursor.fetchall()
        if not result[0][0]:
            raise ValidationError(
                message='Ticket doesn\'t exist in database',
                cursor_position=len(document.text))  # Move cursor to end


questions00 = [
    {
        'type': 'input',
        'message': 'Enter your username: ',
        'name': 'username'
    },
    {
        'type': 'password',
        'message': 'Enter your password',
        'name': 'password'
    }
]
answers00 = prompt(questions00, style=custom_style_2)
if (answers00['username'] == "admin" and answers00['password'] == "adminpass"):
    bAdmin = True
    while bAdmin:
        print("Welocme ", answers00['username'])
        questions01 =[
            {
                'type': 'list',
                'name': 'Admin Menu',
                'message': 'What do you want to do?',
                'choices': ['Add a new flight record','Update details of an existing flight record','Cancel a flight record', 'View flights landing and taking off for a particular airport on that day','View every table of the database in the tabular form', 'Exit'],
            }
        ] 
        answers01 = prompt(questions01, style=custom_style_2)
        if answers01['Admin Menu'] == 'Add a new flight record':
            questions02 = [
                {
                    'type': 'input',
                    'name': 'fl_date',
                    'message': 'What\'s flight Date (Format: dd/mm/yyyy)?',
                    'validate': DateValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_departure_time',
                    'message': 'What\'s the departure time (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_arrival_time',
                    'message': 'What\'s the arrival time (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_departure_airport',
                    'message': 'What\'s the departure airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_arrival_airport',
                    'message': 'What\'s the arrival airport name (Format: IATA Code)',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_fare',
                    'message': 'What\'s the flight fare (Format: 00000)',
                    'validate': NumberValidator,
                },
            ]
            answers02 = prompt(questions02, style=custom_style_2)
            #pprint(answers02)
            dbcursor.execute("SELECT MAX(f_id) FROM Flights")
            fl_id = dbcursor.fetchall()
            dbcursor.execute(addFlight, (fl_id[0][0]+1, answers02['fl_date'],answers02['fl_departure_time'],answers02['fl_arrival_time'],answers02['fl_departure_airport'].upper(),answers02['fl_arrival_airport'].upper(),answers02['fl_fare']))
            mydb.commit()
            print("Flight data added")
        elif answers01['Admin Menu'] == 'Update details of an existing flight record':
            questions03 = [
                {
                    'type': 'input',
                    'name': 'fl_id',
                    'message': 'What\'s flight ID (Format: Integer)?',
                    'validate': FlightIdValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_date',
                    'message': 'What\'s flight Date (Format: dd/mm/yyyy)?',
                    'validate': DateValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_departure_time',
                    'message': 'What\'s the departure time (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_arrival_time',
                    'message': 'What\'s the arrival time (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_departure_airport',
                    'message': 'What\'s the departure airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_arrival_airport',
                    'message': 'What\'s the arrival airport name (Format: IATA Code)',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_fare',
                    'message': 'What\'s the flight fare (Format: 00000)',
                    'validate': NumberValidator,
                },
            ]
            answers03 = prompt(questions03, style=custom_style_2)
            dbcursor.execute(updateFlight, (answers03['fl_date'],answers03['fl_departure_time'],answers03['fl_arrival_time'],answers03['fl_departure_airport'].upper(),answers03['fl_arrival_airport'].upper(),answers03['fl_fare'],answers03['fl_id']))
            mydb.commit()
            print("Flight data updated.")
        elif answers01['Admin Menu'] == 'Cancel a flight record':
            questions04 = [
                {
                    'type': 'input',
                    'name': 'fl_id',
                    'message': 'What\'s flight ID (Format: Integer)?',
                    'validate': FlightIdValidator,
                },
            ]
            answers04 = prompt(questions04, style=custom_style_2)
            dbcursor.execute(deleteFlight, (answers04['fl_id'], ))
            mydb.commit()
            print("Flight data deleted.")
        elif answers01['Admin Menu'] == 'View flights landing and taking off for a particular airport on that day':
            questions05 = [
                {
                    'type': 'input',
                    'name': 'fl_date',
                    'message': 'What\'s Date (Format: dd/mm/yyyy)?',
                    'validate': DateValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_departure_airport',
                    'message': 'What\'s the airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
            ]
            answers05 = prompt(questions05, style=custom_style_2)
            dbcursor.execute(viewFlight, (answers05['fl_date'],answers05['fl_departure_airport'].upper(),answers05['fl_date'],answers05['fl_departure_airport'].upper()))
            x = from_db_cursor(dbcursor)
            print(x)
        elif answers01['Admin Menu'] == 'View every table of the database in the tabular form':
            print("Printing data")
            dbcursor.execute("SELECT * FROM Airports")
            x1 = from_db_cursor(dbcursor)
            print(x1)
            dbcursor.execute("SELECT * FROM Flights")
            x2 = from_db_cursor(dbcursor)
            print(x2)
            dbcursor.execute("SELECT * FROM Passengers")
            x3 = from_db_cursor(dbcursor)
            print(x3)
            dbcursor.execute("SELECT * FROM Tickets")
            x4 = from_db_cursor(dbcursor)
            print(x4)
        elif answers01['Admin Menu'] == 'Exit':
            print("Good Bye Admin")
            bAdmin = False
elif (answers00['username'] == "recepionist" and answers00['password'] == "pass"):
    bRecepionist = True
    while bRecepionist:
        print("Welocme ", answers00['username'])
        questions10 =[
            {
                'type': 'list',
                'name': 'rMenu',
                'message': 'What do you want to do?',
                'choices': ['Create a new passenger record, with the required personal details' ,'Update details of an existing passenger record','View all available flights in a particular time period','Generate ticket record for a particular passenger for a particular flight','View the cheapest flight','View flight history of a particular passenger','Cancel a particular ticket record','Exit'],
            }
        ] 
        answers10 = prompt(questions10, style=custom_style_2)
        if answers10['rMenu'] == 'Create a new passenger record, with the required personal details':
            questions11 = [
                {
                    'type': 'input',
                    'name': 'ps_name',
                    'message': 'What\'s the name of passenger',
                },
                {
                    'type': 'input',
                    'name': 'ps_address',
                    'message': 'What\'s the address of the passenger?',
                },
                {
                    'type': 'input',
                    'name': 'ps_contact',
                    'message': 'What\'s the contact number of the passenger(Format: (xxx) xxx xxxx)',
                    'validate': PhoneNumberValidator,
                },
                {
                    'type': 'input',
                    'name': 'ps_nationality',
                    'message': 'What\'s the nationality of the passenger?',
                },
            ]
            answers11 = prompt(questions11, style=custom_style_2)
            dbcursor.execute("SELECT MAX(f_id) FROM Flights")
            ps_id = dbcursor.fetchall()
            dbcursor.execute(addPassenger,(ps_id[0][0]+1, answers11['ps_name'],answers11['ps_address'],answers11['ps_contact'],answers11['ps_nationality']))
            mydb.commit()
            print("Passenger Added with id ", ps_id[0][0]+1)
        elif answers10['rMenu'] == 'Update details of an existing passenger record':
            questions12 = [
                {
                    'type': 'input',
                    'name': 'ps_id',
                    'message': 'What\'s the passenger you want to updat (Format: ID)?',
                    'validate': PassengerIdValidator,
                },
                {
                    'type': 'input',
                    'name': 'ps_name',
                    'message': 'What\'s the name of passenger',
                },
                {
                    'type': 'input',
                    'name': 'ps_address',
                    'message': 'What\'s the address of the passenger?',
                },
                {
                    'type': 'input',
                    'name': 'ps_contact',
                    'message': 'What\'s the contact number of the passenger(Format: (xxx) xxx xxxx)',
                    'validate': PhoneNumberValidator,
                },
                {
                    'type': 'input',
                    'name': 'ps_nationality',
                    'message': 'What\'s the nationality of the passenger?',
                },
            ]
            answers12 = prompt(questions12, style=custom_style_2)
            dbcursor.execute(updatePassenger,(answers12['ps_name'],answers12['ps_address'],answers12['ps_contact'],answers12['ps_nationality'], answers12['ps_id']))
            mydb.commit()
            print("Passenger record updated")
        elif answers10['rMenu'] == 'View all available flights in a particular time period':
            questions13 = [
                {
                    'type': 'input',
                    'name': 'airport',
                    'message': 'What\'s the airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_time1',
                    'message': 'Time From (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_time2',
                    'message': 'Time To (Format: hh:mm)?',
                    'validate': TimeValidator,
                },
            ]
            answers13 = prompt(questions13, style=custom_style_2)
            dbcursor.execute("SELECT * FROM Flights WHERE (f_departure_airport = %s AND (f_departure_time BETWEEN %s AND %s)) OR (f_arrival_airport = %s AND (f_arrival_time BETWEEN %s AND %s))", (answers13['airport'].upper(),answers13['fl_time1'],answers13['fl_time2'],answers13['airport'],answers13['fl_time1'],answers13['fl_time2']))
            x = from_db_cursor(dbcursor)
            print(x)
        elif answers10['rMenu'] == 'Generate ticket record for a particular passenger for a particular flight':
            questions14 = [
                {
                    'type': 'input',
                    'name': 'tk_flight',
                    'message': 'What\'s the Flight ID?',
                    'validate': FlightIdValidator,
                },
                {
                    'type': 'input',
                    'name': 'tk_passenger',
                    'message': 'What\'s the passenger ID?',
                    'validate': PassengerIdValidator,
                },
            ]
            answers14 = prompt(questions14, style=custom_style_2)
            dbcursor.execute("SELECT MAX(t_id) FROM Tickets")
            tk_id = dbcursor.fetchall()
            x = tk_id[0][0]+1
            dbcursor.execute( addTicket, ( x, answers14['tk_flight'], answers14['tk_passenger']))
            print("Ticket Record Added")
            mydb.commit()
        elif answers10['rMenu'] == 'View the cheapest flight':
            questions15 = [
                {
                    'type': 'input',
                    'name': 'fl_departure_airport',
                    'message': 'What\'s the Departure airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
                {
                    'type': 'input',
                    'name': 'fl_arrival_airport',
                    'message': 'What\'s the Arrival airport name (Format: IATA Code)?',
                    'validate': IATAValidator,
                },
            ]
            answers15 = prompt(questions15, style=custom_style_2)
            dbcursor.execute("SELECT * FROM Flights WHERE f_departure_airport = %s AND f_arrival_airport = %s ORDER BY f_fare LIMIT 1", (answers15['fl_departure_airport'].upper(),answers15['fl_arrival_airport'].upper()))
            x = from_db_cursor(dbcursor)
            print(x)
        elif answers10['rMenu'] == 'View flight history of a particular passenger':
            questions16 = [
                {
                    'type': 'input',
                    'name': 'p_id',
                    'message': 'What\'s Passenger ID (Format: Integer)?',
                    'validate': PassengerIdValidator,
                },
            ]
            answers16 = prompt(questions16, style=custom_style_2)
            dbcursor.execute("SELECT t_id, p_id, f_id, p_name, p_contact, f_arrival_time, f_departure_time, f_arrival_airport, f_departure_airport, f_fare  FROM (SELECT * FROM Tickets INNER JOIN Passengers ON Passengers.p_id = Tickets.t_passenger_id WHERE p_id = %s) AS tempTable INNER JOIN Flights ON Flights.f_id = tempTable.t_flight_id", (answers16['p_id'], ))
            x = from_db_cursor(dbcursor)
            print(x)
        elif answers10['rMenu'] == 'Cancel a particular ticket record':
            questions16 = [
                {
                    'type': 'input',
                    'name': 'tk_id',
                    'message': 'What\'s Ticket ID (Format: Integer)?',
                    'validate': TicketIdValidator,
                },
            ]
            answers16 = prompt(questions16, style=custom_style_2)
            dbcursor.execute(deleteTicket, (answers16['tk_id'], ))
            mydb.commit()
            print("Ticket data deleted.")
        elif answers10['rMenu'] == 'Exit':
            print("Good Bye Recepionist")
            bRecepionist = False
else:
    print("User Not Found: Terminating...")
    