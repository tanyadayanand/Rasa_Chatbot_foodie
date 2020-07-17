# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''https://myaccount.google.com/lesssecureapps'''
def send_mail_gmail(body,recivermail,mailsubject):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security

    sender_address = "tanya.ishan.chatbot@gmail.com" # enter senders mail
    sender_pass = '!zxcvbnm' # password
    receiver_address = recivermail


    message = MIMEMultipart()
    message['From'] =  sender_address
    message['To'] =   recivermail
    message['Subject'] =  mailsubject
    message.attach(MIMEText(body, 'plain'))
    s.starttls()
    # Authentication
    s.login(sender_address,sender_pass)
    # message to be sent
    text = message.as_string()
    # sending the mail
    s.sendmail(sender_address, receiver_address, text)
    # terminating the session
    s.quit()
    print('mail send')
# tanyadayanand@gmail.com
#send_mail_gmail('body','tanyadayanand@gmail.com','subject')