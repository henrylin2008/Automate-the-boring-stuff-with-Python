import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) # yes, using ssl encryption
conn.login('hlin@contextlogic.com', 'wftuyzbmxfurlhco') #("email address", "pw")
conn.select_folder('INBOX', readonly=True) # Inbox folder (99%), readonly mode (no deleting email)
UIDs = conn.search('SINCE 16-SEP-2019')
rawMessage = conn.fetch([one of UIDs num], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[UIDs_num]['BODY[]'])
message.get_subject()
# 'Hello!'
message.get_addresses('from')
# [('Edward Snowden', 'esnowden@nsa.gov')]
message.get_addresses('to')
# [(Jane Doe', 'jdoe@example.com')]
message.get_addresses('cc')
# []
message.get_addresses('bcc')
# []
# message.text_part != None
# True
message.text_part.get_payload().decode(message.text_part.charset)
# 'Follow the money.\r\n\r\n-Ed\r\n'
# message.html_part != None
# True
message.html_part.get_payload().decode(message.html_part.charset)
# '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-
# Al<br></div>\r\n'
# >>> imapObj.logout()