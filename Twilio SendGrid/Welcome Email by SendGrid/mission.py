import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email: str, name: str):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=BODY.format(name))
    sg.send(message)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
