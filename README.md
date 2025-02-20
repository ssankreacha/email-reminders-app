# 📧 Python Email Reminder App

A **simple console-based Email Reminder App** that allows users to schedule an email to be sent at a future date and time.

---

## 📌 Features

* ✅ **User enters recipient email, subject, and message**  
* ✅ **User sets a future date & time for sending the email**  
* ✅ **App waits until the scheduled time and sends the email automatically**  
* ✅ **Ensures the scheduled time is valid (not in the past)**  
* ✅ **Uses `smtplib` to send emails via Gmail**  

---

## 📌 Usage Guide

* 1️⃣ Enter recipient email, subject, and message
* 2️⃣ Set a future date & time (format: YYYY-MM-DD HH:MM)
* 3️⃣ The app will wait until the scheduled time
* 4️⃣ Email is sent automatically to the recipient
* 5️⃣ If the time is invalid or in the past, the app will display an error

---

## 📌 Future Enhancements

* ✅ Recurring Reminders (Daily/Weekly/Monthly)
* ✅ Store Sent Reminders in a Log File
* ✅ GUI Version (Tkinter or Web-Based UI)
* ✅ Support for Multiple Email Providers (Outlook, Yahoo, etc.)