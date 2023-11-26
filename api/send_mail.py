import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config

TOKEN = config('TOKEN')

def csv_file_name():
    csv_file_name.file_name = input("Enter File Name:")
    return csv_file_name.file_name
def csv_send_mail():
    # Email configuration
    sender_email = config('sender_email')
    receiver_email = input("Enter the email address you want to send to: ")
    subject = input("Enter the Subject of Mail: ")
    body = input("Enter the Body Messages of Mail: ")

    # Attach CSV file
    csv_fileName = csv_file_name.file_name
    csv_file_path = csv_fileName # the file name come from insert.py file

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach CSV file
    attachment = open(csv_file_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + csv_file_path)
    msg.attach(part)

    # Connect to the SMTP server
    smtp_server = config('SmtpServer')
    smtp_port = config('SmtpPort')
    smtp_username = config('sender_email')
    smtp_password = config('smtp_password')

    server = smtplib.SMTP(smtp_server, smtp_port)
    # server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Quit the server
    server.quit()
    print(f'Data mailed Successfully to: {receiver_email}')
