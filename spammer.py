import smtplib,message
from email.mime.text import MIMEText
msg = message.message
msg['Subject'] = message.subj
msg['From'] = message.From
msg['To'] = message.To
s = smtplib.SMTP['']
s.sendmail(message.From,message.To,msg)
s.quit()
