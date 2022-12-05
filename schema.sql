CREATE TABLE IF NOT EXISTS User (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
phone_number TEXT UNIQUE,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
date_created TEXT,
hire_date TEXT,
user_type TEXT, 
active INTEGER DEFAULT 1

);

CREATE TABLE IF NOT EXISTS Competencies(
comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
date_created TEXT
);

CREATE TABLE IF NOT EXISTS Assessments(
assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
comp_id INTEGER NOT NULL,
assessment_name TEXT NOT NULL,
verbal_interview INTEGER DEFAULT 0,
assessment_date_created TEXT,
active INTEGER DEFAULT 1,
FOREIGN KEY (comp_id) REFERENCES Competencies (comp_id)
);

CREATE TABLE IF NOT EXISTS Assessments_Results(
result_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
assessment_id INTEGER NOT NULL, 
score INTEGER,
date_taken TEXT NOT NULL,
manager_id INTEGER,
active INTEGER DEFAULT 1,
FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id),
FOREIGN KEY (user_id) REFERENCES User (user_id),
FOREIGN KEY (manager_id) REFERENCES User (user_id)

);