#Creating And Editing A Phone Book Joseph Rydberg 12/2/2024
import sqlite3

#Creates Database And Runs All Functions Asks For Actions
def main():

    connection = sqlite3.connect("phonebook")
    cursor = connection.cursor()

    add_phone_book(cursor)
    read_phone_book(cursor)

    while True:
        a = input("What action would you like for Phone Book r: read, w: write, d: delete, x: cancel")
        if a == "r":
            read_phone_book(cursor)
            continue
        elif a == "w":
            phone_book(cursor)
            continue
        elif a == "d":
            delete_lines(cursor, connection)
            continue
        elif a == "x":
            break
        else:
            print("Not an Option")
            continue

#Creates Database File Or Overwrites It
def add_phone_book(cursor):
    cursor.execute('DROP TABLE IF EXISTS phonebook')
    cursor.execute('CREATE TABLE phonebook (Name TEXT, Number INTEGER)')

#Allows Input For
def phone_book(cursor):
    phone_numbers = []
    while True:
        phone_numbers.append((str(input("Name")), int(input("Insert Phone Number"))))
        if input("Add another number? enter y") != "y":
            break
        else:
            continue


    for row in phone_numbers:
        cursor.execute('''INSERT INTO phonebook (Name, Number) VALUES (?, ?)''', (row[0], row[1]))

def read_phone_book(cursor):
    cursor.execute('SELECT * FROM phonebook')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}')

def delete_lines(cursor, connection):
    de = input("Enter name for deletion")
    connection.execute('''DELETE FROM phonebook WHERE Name=?''', (de,))
    connection.commit()
    read_phone_book(cursor)

main()