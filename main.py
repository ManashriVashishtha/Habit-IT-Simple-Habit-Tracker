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
    password="*******",
    database="habit_tracker"
)

cursor = connection.cursor()

#This block is to import datetime module from python
#It will be used for saving Date in "Habit_log" table
from datetime import date
today = date.today()


"""================================================
================================================"""


'''________________________________________________
            Defining functions 
_____________________v___________________________'''

#Defining Show_Habits function---------------------------------
#It will fetch the habits listed in "Habit" table in Habit_tracker database.
def show_habits():
    cursor.execute("SELECT * FROM habit")
    results = cursor.fetchall()
    print("Available Habits:")
    for row in results:
        print(row[0], "-",row[1])

#Defining new_habit() function---------------------------------
#It will let the user enter a new habit
def new_habit():
    habit_name= input("Enter the name of the new habit: ") # will be in text format
    cursor.execute("SELECT IFNULL(MAX(id), 0) + 1 FROM habit")
    next_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO habit (id, name) VALUES (%s, %s)", (next_id, habit_name))
    connection.commit()
    print("New habit added successfully")

#Defining show_logs() function----------------------------------
#It will show the logs of hours spent for each habit on each date.
def show_logs():
    show_habits() # Show habits before showing logs

    show_log_habit= input("Enter the IDNumber of the Habit to show logs: ") #Will be 1,2,3 etc
    show_log_habit = int(show_log_habit)
    cursor.execute("SELECT date, hours FROM habit_logs WHERE habit_id = %s", (show_log_habit,))
    results = cursor.fetchall()
    print("Logs for Habit ID", show_log_habit)
    for row in results:
        print(" ")
        print("Date:", row[0], "|  Hours:", row[1])

#Defining log_hours() function---------------------------------
#It will let the user enter the hours spent for a habit
def log_hours():
    show_habits() # Show habits before logging hours

    log_choice= input("Enter the IDNumber of the Habit to log: ") #Will be 1,2,3 etc
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

#Defining delete_logs() function----------------------------------
#It will delete selected logs. Select habit then all logs shown. then you can select the date of log to be deleted.
def delete_logs():
    show_habits() # Show habits before showing logs
    delete_log_habit= input("Enter the IDNumber from which to delete logs: ") #Will be 1,2,3 etc    
    delete_log_habit= int(delete_log_habit)
    print("Here are current logs for Habit ID", delete_log_habit)
    cursor.execute("SELECT date, hours FROM habit_logs WHERE habit_id = %s", (delete_log_habit,))
    results = cursor.fetchall()
    for row in results:
        print(" ")
        print("Date:", row[0], "|  Hours:", row[1])

    delete_log_date= input("Enter the date of log to be deleted (YYYY-MM-DD): ") # will be in YYYY-MM-DD format
   
    cursor.execute("DELETE FROM habit_logs WHERE habit_id = %s AND date = %s", (delete_log_habit, delete_log_date))
    connection.commit()
    print("log succesfully deleted")

