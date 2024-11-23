# import streamlit as st
# from datetime import datetime
# from emailer import send_email
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

# # Simulate user input through Streamlit
# def main():
#     st.title("Weather Notification System Tester 🌤️")
#     st.write("Use this tool to test the functionalities of the emailer and scheduler modules.")

#     # Collect user inputs
#     username = st.text_input("👤 Username")
#     email = st.text_input("✉️ Email")
#     location = st.text_input("📍 Location")
#     frequency = st.selectbox("⏰ Frequency", ["Daily", "Weekly"])
#     preferred_time = st.time_input("🕒 Preferred Notification Time")
#     language = st.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Others"])

#     if st.button("Test Emailer"):
#         # Test emailer functionality
#         subject = f"Weather Notification Test for {username}"
#         body = f"""
#         Hi {username},

#         This is a test email from the Weather Notification System.
#         - Location: {location}
#         - Frequency: {frequency}
#         - Preferred Time: {preferred_time}
#         - Language: {language}

#         Regards,
#         Weather Notification System
#         """
#         try:
#             send_email(subject, email, body)
#             st.success(f"Test email sent successfully to {email}. Check your inbox!")
#         except Exception as e:
#             st.error(f"Failed to send email: {e}")

#     if st.button("Test Scheduler"):
#         # Test scheduler functionality
#         def notify_user():
#             """
#             Simulated notification function to test scheduler.
#             Sends a test email to the user.
#             """
#             subject = f"Scheduled Weather Notification for {username}"
#             body = f"""
#             Hi {username},

#             This is a scheduled email test for the Weather Notification System.
#             - Location: {location}
#             - Language: {language}

#             Regards,
#             Weather Notification System
#             """
#             send_email(subject, email, body)

#         try:
#             scheduler = BackgroundScheduler()
#             hour, minute = preferred_time.hour, preferred_time.minute

#             if frequency == "Daily":
#                 scheduler.add_job(
#                     notify_user,
#                     trigger=CronTrigger(hour=hour, minute=minute),
#                 )
#             elif frequency == "Weekly":
#                 scheduler.add_job(
#                     notify_user,
#                     trigger=CronTrigger(day_of_week="mon", hour=hour, minute=minute),
#                 )

#             scheduler.start()
#             st.success("Scheduler started successfully! Notification emails will be sent as scheduled.")
#         except Exception as e:
#             st.error(f"Failed to start scheduler: {e}")

# if __name__ == "__main__":
#     main()




from emailer import send_email

# Replace with your email for testing
test_email = "tvv0410@gmail.com"
subject = "Test Email"
body = "This is a test email from the weather notifier."

send_email(subject, test_email, body)
