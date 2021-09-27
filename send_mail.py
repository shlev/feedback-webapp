import smtplib,os
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = os.environ.get('MT_USER')
    password = os.environ.get('MT_PW')
    print(login, password)
    message=f"<h3>New feedback Submission</h3><ul><li>Customer: {customer}</li><li>Delaer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    reciever_email = 'email2@exmaple.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    # Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())