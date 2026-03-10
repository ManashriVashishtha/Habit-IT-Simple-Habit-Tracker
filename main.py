""" 
================================================
Importing necessary libraries and connections
================================================
"""
#This block is to import python <> SQL connector.
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="Manashri",
    password="Fitall2@",
    database="habit_tracker"
)

cursor = connection.cursor()

#This block is to import datetime module from python
#It will be used for saving Date in "Habit_log" table
from datetime import date
today = date.today()

"""
================================================
================================================
"""


'''
________________________________________________
            Defining functions 
_____________________v___________________________
'''
#Defining Show_Habits function----------
#It will fetch the habits listed in "Habit" table in Habit_tracker database.
def show_habits():
    cursor.execute("SELECT * FROM habit")
    results = cursor.fetchall()
    print("Available Habits:")
    for row in results:
        print(row[0], "-",row[1])

#Defining log_hours() function----------
#It will let the user enter the hours spent for a habit
def log_hours():
    show_habits() # Show habits before logging hours

    log_choice= input("Enter the Number of the Habit to log: ") #Will be 1,2,3 etc
    log_choice = int(log_choice)
    hours_spent = input("Enter the hours spent on this habit today: ") # will be _ _. _ hours format
    hours_spent = float(hours_spent)

    # Get next Sno
    cursor.execute("SELECT IFNULL(MAX(Sno), 0) + 1 FROM habit_logs")
    next_sno = cursor.fetchone()[0]

    # checking for duplicate entry for same habit on same date
    cursor.execute("SELECT *FROM habit_logs WHERE habit_id = %s AND date = %s", (log_choice, today))
    check= cursor.fetchone()

    if check is None:# No prexisting log on same date.(duplicate)
        cursor.execute("Insert into habit_logs (sno,habit_id, date, hours) values (%s,%s,%s,%s)", (next_sno,log_choice, today, hours_spent))
        connection.commit()
        print("Hours logged successfully")
    else: #if duplicate row exists, well BAD LUCK!
        print("You have already logged this today")


 


#running just for funsies
log_hours()


