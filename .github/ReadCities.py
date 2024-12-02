import sqlite3

def main():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Cities')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

main()