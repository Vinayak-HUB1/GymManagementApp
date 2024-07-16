import sqlite3
import uuid
from datetime import date
from datetime import datetime,timedelta
current_date = date.today()
def create_table(gym_name):
    # Connect to SQLite database (will create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {gym_name} (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        age INTEGER,
                        ADMISSION_DATE DATE NOT NULL,
                        EXPIRY_DATE DATE NOT NULL,
                        Period INTEGER NOT NULL
                    )''')

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

def insert_user(name, password,age,Period):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    #calculate expiry date
    expiry_date = current_date + timedelta(days=Period)

    # Insert data into the table
    cursor.execute('''INSERT INTO users (name, password,age,admission_date,EXPIRY_DATE,Period) VALUES (?,?,?,?,?,?)''', (name, password,age,current_date,expiry_date,Period))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()



def get_time_period(username, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        expiry_date = cursor.execute('''SELECT EXPIRY_DATE FROM users WHERE name = ? AND password = ?''', (username, password))
        for i in expiry_date:
            date = i[-1] 
            date = datetime.strptime(date, '%Y-%m-%d').date()
            remaining_days = int((date-current_date).days)
            return remaining_days
    except Exception as e:
        return "invalid credentials."


def get_count():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM users''')

    # Fetch the result (it will be a tuple)
    count = cursor.fetchone()[0]
    return count


# create_table()
# insert_user("vinayak",1234,30,90)
# get_time_period('vinayak',1234)