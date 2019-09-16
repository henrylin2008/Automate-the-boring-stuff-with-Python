import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) # object for smtplib
conn.ehlo()  #start connection
conn.starttls() #start encryption
conn.login('(email_address)', '(pw)') #("email address", "pw")
conn.sendmail('(from_email_address)', '(to_email_address)', 'Subject: ... \n\n hi xx, \n msg')
# {}: mean email sent successfully

# conn.quit()  # disconnect from SMTP server