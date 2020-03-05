from utils import read_credentails
from read_emails_scripts import get_mail_attachments, get_unseen_emails


if __name__ == "__main__":
    email_address, password = read_credentails()
    messages = get_unseen_emails(email_address, password)
    if messages:
        for message in messages:
            attachments = get_mail_attachments(message,
                                               lambda x: x.endswith('.xml'))
            for attachment in attachments:
                if attachment:
                    with open('./data/{}'.format(attachment[0]), 'wb') as file:
                        file.write(attachment[1])
