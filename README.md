# Email Sending Bot
The Email Sending Bot is a Python script that automates the process of sending emails to recipients listed in a CSV file. It reads the email addresses from the file, attaches files such as resumes and cover letters, and sends personalized emails to each recipient.

## Features
Reads email addresses from a CSV file
Attaches files (resume, cover letter ...) to the email
Personalizes the email body
Sends emails using an SMTP server
## Prerequisites
Before running the bot, ensure you have the following:

Python 3 installed on your machine
Required Python packages (csv, smtplib, email.mime) installed. You can install the dependencies using pip:
``` shell
pip install csv smtplib
```
## Usage
Clone the repository or download the source code.
Prepare a CSV file with email addresses. Each email should be listed in a separate row under the 'Email' column.
Update the sender_email and password variables in the script with your own email credentials.
Optionally, update the file paths for attachments, email subject, and body text.
Open a terminal or command prompt and navigate to the project directory.
Run the script:
``` shell
python email_sending_bot.py
```
The bot will continuously monitor the CSV file for new email addresses and send emails automatically.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Python Documentation - Official Python documentation
Feel free to customize the README.md file based on your specific project requirements and provide additional details or instructions as needed
