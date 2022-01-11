class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = list(mails)
        self.domains = list(domains)

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        at = email.find('@')
        dot = email.find('.')
        name = email[0:at]
        mail = email[at + 1: dot]
        domain = email[dot + 1:]
        if self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain):
            return True
        return False