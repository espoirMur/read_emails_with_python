from email import message_from_bytes
from imaplib import IMAP4_SSL


def get_unseen_emails(email_address, password):
    """
    Filter the email and return unseen emails
    Args:
        email_address (string): recipient email
        password (password): recipient password
    """
    with IMAP4_SSL("sample.imap.server.com") as mail_connection:
        mail_connection.login(email_address, password)
        mail_connection.list()
        mail_connection.select('INBOX')
        (retcode, messages) = mail_connection.search(
            None, '(OR (UNSEEN) (FROM your.email@gmail.com))')
        if retcode == 'OK' and messages[0]:
            for index, num in enumerate(messages[0].split()):
                typ, data = mail_connection.fetch(num, '(RFC822)')
                message = message_from_bytes(data[0][1])
                typ, data = mail_connection.store(num, '+FLAGS', '\\Seen')
                yield message


def get_mail_attachments(message, condition_check):
    """
    Get attachments files from mail
    Args:
        message (email ): email object to retrieve attachment from
        condition_check ([function]): the function to use when filtering the
        email should return specific condition we are filtering
    Returns:
        [filename, file]: the file name, input stream from the files
    """
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if not part.get('Content-Disposition'):
            continue
        file_name = part.get_filename()
        if condition_check(file_name):
            yield part.get_filename(), part.get_payload(decode=1)
