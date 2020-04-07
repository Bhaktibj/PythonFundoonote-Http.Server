import smtplib
from email.mime.text import MIMEText
from setting import EMAIL, logger

print("email", EMAIL['email_host_username'])

class SendMail:
    """
    This class is for starting smtp and send email to other accounts.
    """

    def __init__(self):
        self.connnection = self.connect()  # initialize connect

    def connect(self):
        """ this method is used to connect the mail service"""
        try:
            s = smtplib.SMTP(EMAIL['email_host'], EMAIL['email_port'])
            s.starttls()
            s.login(EMAIL['email_host_username'], EMAIL['email_host_password'])
            logger.info("================> email service is started: {}".format(s))
            return s
        except:
            return "email service is failed"

    def send_mail(self, email, data):
        print(email)
        msg = MIMEText(data)
        print(msg)
        self.connnection.sendmail(EMAIL['email_host_username'], email, msg.as_string())
        self.connnection.quit()


# SendMail().send_mail()
