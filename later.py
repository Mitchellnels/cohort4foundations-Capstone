# def view_assessment_res(where=None):
#     if where:
#         where = f"%{where}%"
#         rows = cursor.execute(
#             "SELECT * FROM Assessments_Results WHERE first_name LIKE ?", (where,)
#         ).fetchall()
#     else:

#         rows = cursor.execute("SELECT * FROM Assessments_Results").fetchall()
#         headers = [
#             "result_id",
#             "user_id",
#             "assessment_id",
#             "score",
#             "date_taken",
#             "manager_id",
#             "active",
#         ]

#         print(
#             f"{headers[0]:15}{headers[1]:25}{headers[2]:30}{headers[3]:35}{headers[4]:10}{headers[5]:15}{headers[6]:13}"
#         )
#         for row in rows:
#             # row[4] is state in hour result set. instead of a where clause we can use conditionals in python directly.
#             print(
#                 f"{row[0]:<15}{row[1]:25}{str(row[2]):30}{str(row[3]):35}{str(row[4]):10}{str(row[5]):15}{str(row[6]):13}"
#             )


# view_assessment_res(where=None)
