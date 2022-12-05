import sqlite3
from datetime import datetime

connection = sqlite3.connect("schema.db")
cursor = connection.cursor()

### Creates table:
# def create_schema():

#     with open("schema.sql") as sql_queries:
#         queries = sql_queries.read()
#         cursor.executescript(queries)

#     connection.commit()


# create_schema()
# # CREATES User
# def create_person():

#     insert_query = "INSERT INTO User (first_name, last_name, phone_number, email, password, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?)"
#     while True:
#         name = input("Name: ")

#         if name == "":
#             continue
#         else:
#             break
#     while True:
#         last_name = input("Last Name: ")

#         if last_name == "":
#             continue
#         else:
#             break
#     phone = input("Phone number: ")
#     email = input("Email:")
#     pass_word = input("Password:")
#     date_created = datetime.now()
#     hire_date = input("Enter Date User was Hired:")
#     while True:  # This determines weather user is a manager.
#         user_input = input("Is user a manager?(y/n) ")

#         if user_input.lower() == "y":
#             user_type = True
#         elif user_input.lower() == "n":
#             user_type = False
#         else:
#             print("Invalid option")
#             continue
#         break

#     insert_values = (
#         name,
#         last_name,
#         phone,
#         email,
#         pass_word,
#         date_created,
#         hire_date,
#         user_type,
#     )

#     cursor.execute(insert_query, insert_values)
#     connection.commit()


# create_person()

# # //// Creating a competency to be tested
# def create_compotencies():

#     insert_query = "INSERT INTO Competencies (name, date_created) VALUES (?,?)"
#     name = input(" Enter the Name of the Competency Test: ")
#     date_created = input("Enter the date the course was created: ")
#     insert_value1 = [name, date_created]

#     cursor.execute(insert_query, insert_value1)
#     connection.commit()


# create_compotencies()

# ##//// creating an assessment for a competency


# def create_assessment():

#     insert_query = "INSERT INTO Assessments (comp_id, assessment_name, verbal_interview, assessment_date_created) VALUES (?,?,?,?)"
#     comp_id = input(
#         "Please enter the comp_id that you wish to test for this assessment: "
#     )
#     assessment_name = input(" Enter the Name of the Competency Test: ")
#     verbal_interview = input(
#         "Has a verbal interview taken place? 0 for True, 1 for No: "
#     )
#     assessment_date_created = input("Enter the date the course was created: ")
#     insert_value2 = [
#         comp_id,
#         assessment_name,
#         verbal_interview,
#         assessment_date_created,
#     ]

#     cursor.execute(insert_query, insert_value2)
#     connection.commit()


# create_assessment()


# def create_assessment_result():

#     insert_query = "INSERT INTO Assessments_results (user_id, assessment_id, score, date_taken, manager_id) VALUES (?,?,?,?,?)"
#     user_id = input("Please enter the User number you would like to add results for: ")
#     assessment_id = input(
#         "Please enter the assessment ID that you would like to enter a score for: "
#     )
#     assessment_score = input(" Enter the score of the individual 0-4: ")
#     assessment_date_taken = datetime.now()
#     manager_id = input(
#         "Please enter the ID number for the Manager that is overseeing this assessment: "
#     )
#     insert_value2 = [
#         user_id,
#         assessment_id,
#         assessment_score,
#         assessment_date_taken,
#         manager_id,
#     ]

#     cursor.execute(insert_query, insert_value2)
#     connection.commit()


# create_assessment_result()


# #/////////////////////////// VIEW USERS
# def view_users(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM User WHERE first_name LIKE ?", (where,)
#         ).fetchall()
#     else:

#         rows = cursor.execute("SELECT * FROM User").fetchall()
#         headers = [
#             "person_id",
#             "first_name",
#             "last_name",
#             "phone",
#             "email",
#             "password",
#             "date_created",
#             "hire_date",
#             "user_type",
#             "active",
#         ]
#         print(
#             f"{headers[0]:20}{headers[1]:25}{headers[2]:30}{headers[3]:25}{headers[4]:30}{headers[5]:15}{headers[6]:30}{headers[7]:15}{headers[8]:15}{headers[9]:15}"
#         )
#         for row in rows:
#             print(
#                 f"{row[0]:<20}{row[1]:25}{str(row[2]):30}{str(row[3]):25}{str(row[4]):30}{str(row[5]):15}{str(row[6]):30}{str(row[7]):15}{str(row[8]):15}{str(row[9]):15}"
#             )


# view_users()

##//////////////////////////////////// Update - User
# def edit_user():
#     view_users()

#     headers = ["first_name", "last_name", "phone", "email", "password", "active"]

#     print("Choose one of the following: ")
#     for index, header in enumerate(headers):
#         print(f"{index}: {header}")

#     user_choice = int(input())
#     field_name = headers[user_choice]

#     update_query = f"UPDATE user SET {field_name}=? WHERE user_id LIKE ?"
#     new_value = input(f"New {field_name}: ")
#     cust_id = input("Customer ID: ")

#     values = (new_value, cust_id)

#     cursor.execute(update_query, values)
#     connection.commit()


# edit_user()
# /////////////////////////////// View Competency
# def view_competency(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM Competencies WHERE comp_id LIKE ?", (where,)
#         ).fetchall()
#     else:

#         rows = cursor.execute("SELECT * FROM Competencies").fetchall()
#         headers = [
#             "comp_id",
#             "name",
#             "date_created",
#         ]
#         print(f"{headers[0]:20}{headers[1]:25}{headers[2]:30}")
#         for row in rows:
#             print(f"{row[0]:<20}{row[1]:25}{str(row[2]):30}")


# view_competency()

# #/////////////////////////////////// Edit Competency
# def edit_competency():
#     view_competency()

#     headers = [
#         "comp_id",
#         "name",
#         "date_created",
#     ]

#     print("Choose one of the following: ")
#     for index, header in enumerate(headers):
#         print(f"{index}: {header}")

#     user_choice = int(input())
#     field_name = headers[user_choice]

#     update_query = f"UPDATE Competencies SET {field_name}=? WHERE comp_id LIKE ?"
#     new_value = input(f"New {field_name}: ")
#     comp_id = input("Comp ID: ")

#     values = (new_value, comp_id)

#     cursor.execute(update_query, values)
#     connection.commit()


# edit_competency()
##//////////////////// VIEW ASSESSMENTS
# def view_assessment(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM Assessments WHERE first_name LIKE ?", (where,)
#         ).fetchall()
#     else:

#         rows = cursor.execute("SELECT * FROM Assessments").fetchall()
#         headers = [
#             "assessment_id",
#             "comp_id",
#             "assessment_name",
#             "verbal_interview",
#             "assessment_date",
#             "active",
#         ]
#         print(
#             f"{headers[0]:20}{headers[1]:25}{headers[2]:30}{headers[3]:25}{headers[4]:30}{headers[5]:15}"
#         )
#         for row in rows:
#             print(
#                 f"{row[0]:<20}{row[1]:<25}{str(row[2]):30}{str(row[3]):25}{str(row[4]):30}{str(row[5]):15}"
#             )


# //////////////////////// EDIT ASSESSMENT
# def edit_assessment():
#     view_assessment()

#     headers = [
#         "assessment_id",
#         "comp_id",
#         "assessment_name",
#         "verbal_interview",
#         "assessment_date",
#         "active",
#     ]

#     print("Choose one of the following: ")
#     for index, header in enumerate(headers):
#         print(f"{index}: {header}")

#     user_choice = int(input())
#     field_name = headers[user_choice]

#     update_query = f"UPDATE Assessments SET {field_name}=? WHERE assessment_id LIKE ?"
#     new_value = input(f"New {field_name}: ")
#     assessment_id = input("Assessment ID: ")

#     values = (new_value, assessment_id)

#     cursor.execute(update_query, values)
#     connection.commit()


# edit_assessment()
# //////////////// View Assessment Results
def view_assessment_results(where=None):
    if where:
        where = f"%{where}%"
        rows = cursor.execute(
            "SELECT * FROM Assessments_Results WHERE result_id LIKE ?", (where,)
        ).fetchall()
    else:

        rows = cursor.execute("SELECT * FROM Assessments_Results").fetchall()
        headers = [
            "result_id",
            "user_id",
            "assessment_id",
            "score",
            "date_taken",
            "manager_id",
            "active",
        ]
        print(
            f"{headers[0]:20}{headers[1]:25}{headers[2]:30}{headers[3]:25}{headers[4]:30}{headers[5]:15}{headers[6]:15}"
        )
        for row in rows:
            print(
                f"{row[0]:<20}{row[1]:<25}{str(row[2]):30}{str(row[3]):25}{str(row[4]):30}{str(row[5]):15}{str(row[6]):15}"
            )


view_assessment_results()


# def edit_assessment_results():
#     view_assessment_results()

#     headers = [
#         "result_id",
#         "user_id",
#         "assessment_id",
#         "score",
#         "date_taken",
#         "manager_id",
#         "active",
#     ]

#     print("Choose one of the following: ")
#     for index, header in enumerate(headers):
#         print(f"{index}: {header}")

#     user_choice = int(input())
#     field_name = headers[user_choice]

#     update_query = (
#         f"UPDATE Assessments_Results SET {field_name}=? WHERE result_id LIKE ?"
#     )
#     new_value = input(f"New {field_name}: ")
#     assessment_id = input("Result ID: ")

#     values = (new_value, assessment_id)

#     cursor.execute(update_query, values)
#     connection.commit()


# edit_assessment_results()
##//////////////Deactivate Assessment Result
# def deactivate_result():
#     view_assessment_results(where=None)
#     query = input("Which Result_ ID would you like to remove?:")
#     update_query = (
#         "UPDATE Assessments_Results SET active = 0 WHERE assessment_id LIKE ?"
#     )

#     value = [query]

#     cursor.execute(update_query, value)
#     connection.commit()


# deactivate_result()
