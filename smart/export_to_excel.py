import pandas as pd
import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sownd@05",
    database="complaint_db"
)


# fetches complaint data fom complaint table
query = """
SELECT id, employee_name, employee_email, department, problem,
ticket_id, status, complaint_date, resolve_date
FROM complaints
"""


# read data into pandas df - data frame 
df = pd.read_sql(query, db)

# create reports folder if not exists
os.makedirs("reports", exist_ok=True)

file_path = "reports/complaints_report.xlsx"
df.to_excel(file_path, index=False)

print("Excel file created successfully:", file_path)
