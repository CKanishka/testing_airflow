import smtplib, ssl
def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"  
    receiver_email = "receiver@gmail.com"
    password = "senderemailpassword"
    message = """\
    Subject:Mail from Python

    Testing DAGS in Airflow."""


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)