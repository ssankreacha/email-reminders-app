import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants (Replace with your actual credentials)
""" 
- Your email provider may requires some changes.
- Modify the script with the correct settings and App Passwords relative to the email provider."""

EMAIL_ADDRESS = " "  # Your email
EMAIL_PASSWORD = " "  # App password (not regular password)

# Function to send email
def send_email(recipient, subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())

        print(f"✅ Email reminder sent to {recipient}")

    except Exception as e:

        print(f"❌ Error sending email: {e}")

# Function to schedule reminder
def schedule_reminder():
    recipient = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")
    date_str = input("Enter reminder date & time (YYYY-MM-DD HH:MM): ")

    try:
        scheduled_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        delay = (scheduled_time - datetime.now()).total_seconds()

        if delay > 0:
            print(f"⏳ Reminder scheduled for {scheduled_time}...")
            time.sleep(delay)
            send_email(recipient, subject, message)
        else:
            print("❌ Scheduled time is in the past. Please enter a future date/time.")

    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD HH:MM.")

# Run the program
if __name__ == "__main__":
    schedule_reminder()
