import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "weatherreporter4u@gmail.com"  # Replace with your Gmail address
receiver_email = "tvv0410@gmail.com"  # Replace with your test email
password = "zcmqyasvkwxulwjo"  # Replace with the app password you generated
subject = "Automated Notification"
body = "This is an automated notification email."

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

# Send the email
try:
    # Connect to the Gmail SMTP server securely
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Error occurred: {e}")
