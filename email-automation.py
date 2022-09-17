from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


email_sender = 'Enter your email here'
email_password = "Enter your password here"
email_receiver = ['Enter 1st receiver email',
                  'Enter 2nd receiver email', 'and so on']
email_name = ['Enter 1st receiver name here',
              'Enter 2nd receiver name here', 'and so on']

# Note: Write email_receiver and email_name in same order otherwise wrong names will be attached to the emails


subject = "Write your Subject text here"

for receiver, name in zip(email_receiver, email_name):

    body = f"""
    Respected {name},

    I'm Syed Imaduddin, currently in 3rd year electronics engineering at Zakir Husain College of Engineering and Technology, AMU. I'm from the batch 2020-24. I have written this code to save my time for personalized emails to other people. This code will be helpful for those who want to mail to a lot of Professors for research internship and also helpful for those who is in marketing of any product. 

    Regards,

    Syed Imaduddin,

    3rd Year B-Tech, Electronics Engineering,

    Zakir Husain College of Engineering and Technology, 
    Aligarh Muslim University (AMU)


    E-mail: imaduddinsyed09@gmail.com 

    LinkedIn: https://www.linkedin.com/in/syed-imaduddin-227169205/
    """

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())
