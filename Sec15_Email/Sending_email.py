import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) # object for smtplib
conn.ehlo()  #start connection
conn.starttls() #start encryption
conn.login('hlin@contextlogic.com', 'wftuyzbmxfurlhco') #("email address", "pw")
conn.sendmail('hlin@wish.com', 'hlin@wish.com', 'Subject: Email test \n\n 2nd test, \n')
# {}: mean email sent successfully

# conn.quit()  # disconnect from SMTP server