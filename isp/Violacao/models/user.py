class User():
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def pay_bill(self):
        raise NotImplementedError

    def code(self):
        raise NotImplementedError

    def __str__(self):
        return self._username + " " + self._email