class InvalidUsernameException(Exception):
    def __init__(self, message = "Invalid username"):
        self.message = message
        super().__init__(message)