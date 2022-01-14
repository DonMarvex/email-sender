# Sending mails from gmail.com using Python

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

recipient_list = ['sampleemail1@gmail.com', 'sampleemail2@gmail.com',
                  'sampleemail3@gmail.com']
# add recipient emails in your script as much as you can.
# recipient_list can be read from a csv or txt file containing email addresses
# You can loop through a csv or txt and append to a list

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Recipient Name'
email['to'] = recipient_list    # use one mail address for simple use case
email['subject'] = 'Subject of Email'

email.set_content(html.substitute({'name': 'Custom Substitution name'}), 'html')
# Template allows substitution of $ value. The dictionary passed should contain this
# set_content to recognize html file otherwise, it'll print as plain text

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('senderemail@gmail.com', '***sender_password***')
    smtp.send_message(email)
    print('Message has been sent')  # Just a confirmation on your terminal/environment.

# Now we have been able to create a program to send emails with Python, how cool is that!
