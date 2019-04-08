# encoding=utf-8
class MyEmail:
    # def __init__(self):
    #     self.emailFrom = '';
    #     self.emailTo = '';
    #     self.emailSubject = '';
    #     self.emailText = '';
    #     self.annexPath = '';
    #     self.annexName = '';

    def __init__(self, emailFrom, emailTo, emailSubject, emailText, annexPath, annexName):
        self.emailFrom = emailFrom;
        self.emailTo = emailTo;
        self.emailSubject = emailSubject;
        self.emailText = emailText;
        self.annexPath = annexPath;
        self.annexName = annexName;

    def getEmailFrom(self):
        return self.emailFrom;

    def getEmailTo(self):
        return self.emailTo;

    def getEmailSubject(self):
        return self.emailSubject;

    def getEmailText(self):
        return self.emailText;

    def getAnnexPath(self):
        return self.annexPath;

    def getAnnexName(self):
        return self.annexName;
