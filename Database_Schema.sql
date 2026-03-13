--Create Database
CREATE DATABASE habit_tracker;
-- Creating the table that stores the list of habits
USE habit_tracker;
CREATE TABLE habit (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
-- Creating the table that stores the logs of all habits acc. to their ID
CREATE TABLE habit_logs (
    sno INT PRIMARY KEY,
    habit_id INT NOT NULL,
    date DATE NOT NULL,
    hours DECIMAL(4,1) NOT NULL,

    FOREIGN KEY (habit_id) REFERENCES habit(id),
    UNIQUE (habit_id, date)
);

--Sample habits
INSERT INTO habit VALUES
(1, 'Workout'),
(2, 'Study'),
(3, 'Reading');

--Sample logs
INSERT INTO habit_logs (sno, habit_id, date, hours) VALUES
(1,1,'2026-03-13',3.5)
(2,3,'2026-03-13',0.5)
(3,2,'2026-03-13',4)

