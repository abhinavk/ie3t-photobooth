import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
    print("connecting..")
    flag = 0
    f = open("emails.txt",'w')
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'AUTOMATED PHOTOBOOTH @JUIT'
    From = 'ieee.photobooth@gmail.com'
    text = MIMEText("Thank you for being a part of it.Hope you enjoyed :)\n\n\n\n\n\n\n\n\n-IEEE ThinkLab")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    Server='smtp.gmail.com'
    Port='587'
    
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    UserName='ieee.photobooth'
    UserPassword='clickphoto'
    s.login(UserName, UserPassword)
    print("connected")
    mail = raw_input("Enter Email[Seperated by comma] : ")
    mail = mail.split(',')
    print(mail)
    for To in mail:
        print("Sending") 
        s.sendmail(From, To, msg.as_string())
        print("Sent")
        if flag==0:
            f.write(To)
            flag = 1
            f.close()
    s.quit()
    execfile('store.py')
SendMail('capt0000.jpg')


