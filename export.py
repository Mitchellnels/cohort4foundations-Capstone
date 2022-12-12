import csv
import sqlite3

connection = sqlite3.connect("schema.db")
cursor = connection.cursor()


def view_competency(where=None):
    if where:
        where = f"%{where}%"
        rows = cursor.execute(
            "SELECT * FROM Competencies WHERE comp_id LIKE ?", (where,)
        ).fetchall()
    else:

        rows = cursor.execute("SELECT * FROM Competencies").fetchall()
        headers = [
            "comp_id",
            "name",
            "date_created",
        ]
        print(f"{headers[0]:20}{headers[1]:25}{headers[2]:30}")
        for row in rows:
            print(f"{row[0]:<20}{row[1]:25}{str(row[2]):30}")


# with open("export_report.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)

#     query = "SELECT * FROM User;"

#     rows = cursor.execute(query).fetchall()
#     header = [
#         "user_id",
#         "first_name",
#         "last_name",
#         "phone",
#         "email",
#         "password",
#         "date_created",
#         "hire_date",
#         "user_type",
#     ]
#     writer.writerow(header)
#     writer.writerows(rows)

################## RESULTS FOR A SINGLE USER.
def export_results():
    view_competency()
    where = input("Which comp_id would you like to export results for?: ")
    with open("export_report.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        where = f"%{where}%"
        rows = cursor.execute(
            "SELECT * FROM Assessments_Results WHERE assessment_id LIKE ?", (where,)
        ).fetchall()

        # rr = cursor.execute(rows).fetchall()
        header = [
            "result_id",
            "user_id",
            "assessment_id",
            "score",
            "date_taken",
            "manager_id",
            "active",
        ]
        writer.writerow(header)
        writer.writerows(rows)
    with open("report2.csv", "w") as csv_2:
        writer = csv.writer(csv_2)
        headers2 = [
            "assessment_name",
            "compotency_id",
            "assessment_score",
            "user_id",
            "assessments_id",
        ]

        join = cursor.execute(
            """SELECT assessment_name, comp.comp_id, Assessments_Results.score, Assessments_Results.user_id, assessments.assessment_id FROM Assessments_Results
        JOIN Assessments ON Assessments_Results.assessment_id = Assessments.assessment_id
        JOIN Competencies comp ON Assessments.comp_id = comp.comp_id
        JOIN User ON Assessments_Results.user_id = User.user_id"""
        ).fetchall()
        writer.writerow(headers2)
        writer.writerows(join)


def import_CSV():

    insert_query = "INSERT INTO Assessments_Results (result_id,user_id,assessment_id,score,date_taken,manager_id,active) VALUES (?,?,?,?,?,?,?)"

    with open("import.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        fields = next(
            reader
        )  # Header row, WE WILL NOT USE, but this will remove it from the dataset

        for row in reader:
            cursor.execute(insert_query, row)

    connection.commit()
