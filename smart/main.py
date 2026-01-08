from flask import Flask, render_template, request, redirect, url_for 
# flak lib ->   web app, shoe html page, grt data,  move page
from db_config import get_connection
#            connect to mysql
from email_service import send_email
#          send mail 
from werkzeug.security import check_password_hash
#   passwords
import random, datetime, pandas as pd, matplotlib.pyplot as plt
# ticket id, today date, read data -- table formate
from email_service import send_email, send_status_update

# create flask aapp
app = Flask(__name__)


# HOME
@app.route("/") # home url
def home():
    return render_template("home.html")



# COMPLAINT FORM 
#                            show form , submit form
@app.route("/complaint", methods=["GET","POST"])
def complaint():

    # checks if user submitted the form
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        dept = request.form["dept"]
        problem = request.form["problem"]
        

        # generates ticket is 
        ticket = "Tk" + str(random.randint(1000,9999))

        # gets today date
        today = datetime.date.today()

        # connect database 
        db = get_connection()

        # create cursor
        cur = db.cursor()

        # insert complaint into db
        cur.execute("""
        INSERT INTO complaints
        (employee_name,employee_email,department,problem,
        ticket_id,status,complaint_date,sla_days)
        VALUES (%s,%s,%s,%s,%s,'OPEN',%s,7)
        """,(name,email,dept,problem,ticket,today))


        # save data and close the connection
        db.commit()
        db.close()

        
        # sent complaint confirmation mail
        send_email(email, ticket, "OPEN", problem)

        # show success page
        return render_template(
            "complaint_success.html",
            ticket=ticket,
            status="OPEN"
            )
    
    # show the complaint form page
    return render_template("complaint.html")


# STATUS FORM PAGE
@app.route("/status", methods=["GET","POST"])
def status():
    if request.method == "POST":
        name = request.form["name"].strip()
        ticket = request.form["ticket"].strip()

        # Redirect to result page with form data as query parameters
        return redirect(url_for("status_result", name=name, ticket=ticket))


    return render_template("status.html")  # just the form


# STATUS RESULT PAGE
@app.route("/status/result")
def status_result():
    name = request.args.get("name")
    ticket = request.args.get("ticket")

    db = get_connection()
    cur = db.cursor()

    cur.execute("""
        SELECT employee_name, ticket_id, problem, complaint_date, status
        FROM complaints
        WHERE employee_name=%s AND ticket_id=%s
    """, (name, ticket))

    data = cur.fetchone()
    db.close()

    return render_template("status_result.html", data=data)



# MANAGER LOGIN
@app.route("/manager", methods=["GET","POST"])
def manager():
    if request.method=="POST":
        name=request.form["name"]
        pwd=request.form["password"]

        db=get_connection()
        cur=db.cursor()
        cur.execute("SELECT password FROM manager WHERE manager_name=%s",(name,))
        row=cur.fetchone()
        db.close()

        if row and check_password_hash(row[0],pwd):
            return redirect("/dashboard")
        return "Invalid Login"

    return render_template("manager_login.html")


# MANAGER DASHBOARD
@app.route("/dashboard")
def dashboard():
    db=get_connection()
    df=pd.read_sql("SELECT * FROM complaints",db)
    db.close()

    df["status"].value_counts().plot(kind="bar")
    plt.savefig("charts/status_chart.png")
    plt.close()

    return render_template("manager_dashboard.html",data=df.values)




# ADMIN LOGIN
# Admin Login Route
@app.route("/admin_login", methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        name = request.form["name"]
        pwd = request.form["password"]

        db = get_connection()
        cur = db.cursor()
        cur.execute("SELECT password FROM admin WHERE admin_name=%s", (name,))
        row = cur.fetchone()
        db.close()

        if row and check_password_hash(row[0], pwd):
            return redirect("/admin_panel")
        return "Invalid Admin Login"
    
    return render_template("admin_login.html")



# ADMIN PANEL
@app.route("/admin_panel", methods=["GET","POST"])
def admin_panel():
    if request.method == "POST":
        ticket = request.form["ticket"]
        new_status = request.form["status"]
        today = datetime.date.today()

        db = get_connection()
        cur = db.cursor()

       
        # Fetch user email & problem
        cur.execute("""
            SELECT employee_email, problem
            FROM complaints
            WHERE ticket_id=%s
        """, (ticket,))
        row = cur.fetchone()
        

        if row:
            email, problem = row

            cur.execute("""
                UPDATE complaints
                SET status=%s, resolve_date=%s, complete_date=%s
                WHERE ticket_id=%s
            """, (new_status, today, today, ticket))

            db.commit()
            db.close()

           
            # Send status update email
            send_status_update(email, ticket, new_status, problem)
         
        else:
            db.close()

    return render_template("admin_panel.html")




app.run(debug=True)




