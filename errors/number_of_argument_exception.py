class NumberOfArgumentException(Exception):
    def __init__(self, message = "The number of arguments is invalid"):
        self.message = message
        super().__init__(message)