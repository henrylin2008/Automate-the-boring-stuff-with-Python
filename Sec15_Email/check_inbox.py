import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) # yes, using ssl encryption
conn.login('hlin@contextlogic.com', 'wftuyzbmxfurlhco') #("email address", "pw")
conn.select_folder('INBOX', readonly=True) # Inbox folder (99%), readonly mode (no deleting email)
UIDs = conn.search(['SINCE 16-SEP-2019'])