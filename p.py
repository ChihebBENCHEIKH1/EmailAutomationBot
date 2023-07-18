import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

# Define email credentials and settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'bencheikh.chiheb@gmail.com'
password = 'hopxcgmlqmtcvuep'

# Create a function to send an email
def send_email(recipient_email):
    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = 'Job application'

    # Attach resume
    resume_path = r'c:\Users\Chiheb Ben Cheikh\Downloads\chiheb_cv.pdf'
    with open(resume_path, 'rb') as resume_file:
        resume_part = MIMEApplication(resume_file.read(), Name='chiheb_cv.pdf')
        resume_part['Content-Disposition'] = f'attachment; filename="{resume_path}"'
        message.attach(resume_part)

    # Attach cover letter
    cover_letter_path = r'c:\Users\Chiheb Ben Cheikh\Downloads\Lettre_de_motivation.pdf'
    with open(cover_letter_path, 'rb') as cover_letter_file:
        cover_letter_part = MIMEApplication(cover_letter_file.read(), Name='cover_letter.pdf')
        cover_letter_part['Content-Disposition'] = f'attachment; filename="{cover_letter_path}"'
        message.attach(cover_letter_part)

    # Add email body
    body = 'Hello, I am sending this email to apply for the job X'
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, password)

        # Attach the multipart message to the email
        message['To'] = recipient_email
        server.send_message(message)

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"An error occurred while sending email to {recipient_email}: {str(e)}")

    finally:
        # Disconnect from the SMTP server
        server.quit()

# Initialize the previous email count
previous_count = 0

# Run the bot continuously to send emails
while True:
    # Open the CSV file
    with open(r'c:\Users\Chiheb Ben Cheikh\Downloads\my_emails.csv', 'r') as file:
        reader = csv.DictReader(file)

        # Extract emails from the 'Email' column
        emails = [row['Email'] for row in reader]

        # Check if new emails have been added
        if len(emails) > previous_count:
            print("number of emails changed")
            new_emails = emails[previous_count:]
            for recipient_email in new_emails:
                send_email(recipient_email)

            # Update the previous email count
            previous_count = len(emails)
            print(f"Processed {len(new_emails)} new emails.")

    # Sleep for a specific duration before checking for new emails again
    # You can adjust the duration based on your needs
    time.sleep(10)  # Sleep for 1 minute
