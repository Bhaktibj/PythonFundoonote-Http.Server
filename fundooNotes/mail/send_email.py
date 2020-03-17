import smtplib
from email.mime.text import MIMEText
from setting import ConfigService

obj = ConfigService()


class SendMail:
    """
    This class is for starting smtp and send email to other accounts.
    """

    def __init__(self):
        self.con = self.connect()

    def connect(self):
        try:
            s = smtplib.SMTP(obj.EMAIL['email_host'], obj.EMAIL['email_port'])
            s.starttls()
            s.login(obj.EMAIL['email_host_username'], obj.EMAIL['email_host_password'])
            obj.logger.info("================> email service is started: {}".format(s))
            return s
        except:
            return "email service is failed"

    def send_mail(self, email, data):
        print(email)
        msg = MIMEText(data)
        print(msg)
        self.con.sendmail(obj.EMAIL['email_host_username'], email, msg.as_string())
        self.con.quit()

# SendMail().send_mail()
