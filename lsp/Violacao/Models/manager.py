from lsp.Violacao.Models.user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        raise Exception('Member is not authorized to do this!')