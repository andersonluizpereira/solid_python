from isp.Violacao.models.user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def pay_bill(self):
        return "Paying Bills"

    def code(self):
        pass