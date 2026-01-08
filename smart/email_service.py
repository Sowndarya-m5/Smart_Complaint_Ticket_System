import smtplib
from email.mime.text import MIMEText

# ===============================
# EMAIL CONFIG
# ===============================
SENDER_EMAIL = "murugacool15@gmail.com"
APP_PASSWORD = "voho snel kibb srja"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# ===============================
# COMMON MAIL FUNCTION (FAST)
# ===============================
def send_mail(to_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email sending failed:", e)


# ===============================
# COMPLAINT REGISTER MAIL
# ===============================
def send_email(to_email, ticket, status, problem):
    body = f"""
Complaint Registered Successfully

Ticket ID : {ticket}
Problem   : {problem}
Status    : {status}
"""
    send_mail(
        to_email,
        "Complaint Confirmation",
        body
    )


# ===============================
# STATUS UPDATE MAIL
# ===============================
def send_status_update(to_email, ticket, new_status, problem):
    body = f"""
Complaint Status Updated

Ticket ID : {ticket}
Problem   : {problem}
New Status: {new_status}
"""
    send_mail(
        to_email,
        "Complaint Status Update",
        body
    )
