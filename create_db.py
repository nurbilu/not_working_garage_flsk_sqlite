import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('cars.db')
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
# Create a table named 'cars' with columns: model, year, color
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        color TEXT NOT NULL
    )
''')

# Insert some sample data
# cursor.execute("INSERT INTO cars (model, year, color) VALUES (?, ?, ?)", ('Toyota Camry', 2022, 'a'))
# cursor.execute("INSERT INTO cars (model, year, color) VALUES (?, ?, ?)", ('Honda Accord', 2021, 'b'))
cursor.execute("INSERT INTO cars (model, year, color) VALUES (?, ?, ?)", ('BMW 112', 2006, 'red'))
cursor.execute("INSERT INTO cars (model, year, color) VALUES (?, ?, ?)", ('Honda Civic', 1997, 'blue'))


# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")
