class Validation:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def email_validation(self):
        pass

    def password_validation(self):
        pass

    def website_validation(self):
        pass

    def website_validation(self, website):
    return 

    def email_validation(self, email):
        return '@' in email and '.' in email.split('@')[1]