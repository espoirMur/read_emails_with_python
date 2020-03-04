from unittest import TestCase
from unittest.mock import Mock, patch
from read_emails_scripts import (get_unseen_emails,
                                 get_mail_attachments)
from tests.mocks import MockIMAP4SSL
from types import GeneratorType


class TestReadingMail(TestCase):

    email_address = 'test@test.com'
    password = 'jdjdhskjhjkf'

    @patch('read_emails_scripts.IMAP4_SSL')
    def test_read_email(self, mock_imap_lib):
        """
        Test if read mails return the email

        """

        mail_text = 'this is a mail test'
        # context manager
        mock_imap_lib.return_value = MockIMAP4SSL('test.home.com')
        mails = get_unseen_emails(self.email_address, self.password)
        self.assertIsInstance(mails, GeneratorType)
        for mail in mails:
            self.assertEqual(str(mail).strip(), mail_text)

    @patch('read_emails_scripts.IMAP4_SSL')
    def test_read_email_fails(self, mock_connect):
        """
        Test if read mails return none when there is no email

        """
        # context manager
        connection = mock_connect.return_value.__enter__.return_value
        connection.login.return_value = None
        connection.search.return_value = (None, None)
        mails = get_unseen_emails(self.email_address, self.password)
        for mail in mails:
            self.assertIsNone(mail)


class TestDownloadAttachment(TestCase):

    def test_download_attachment_function_xml(self):
        """
        Test if it download attachment as xml file
        Args:
            TestCase ([type]): [description]
        """
        def mock_get_payload(decode=1):
            return bytes('mail_text', encoding='UTF-8')
        filename = 'something.xml'
        mail = Mock(get_content_maintype=lambda: "multipart...",
                    get_filename=lambda: filename,
                    get_payload=mock_get_payload)
        mail.__setattr__('Content-Disposition', "Something")
        mock_email = Mock(walk=lambda: [mail])
        attachments = get_mail_attachments(
            mock_email, lambda x: x.endswith('.xml'))
        self.assertIsInstance(attachments, GeneratorType)
        for name, payload in attachments:
            self.assertEqual(name, filename)
            self.assertEqual(payload, bytes('mail_text', encoding='UTF-8'))
