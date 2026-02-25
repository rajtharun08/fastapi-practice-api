class HiringAppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class UserAlreadyExistsException(HiringAppException):
    def __init__(self):
        super().__init__("A user with this email already exists", status_code=400)

class JobNotFoundException(HiringAppException):
    def __init__(self):
        super().__init__(" requested job post was not found", status_code=404)

class UnauthorizedApplicationException(HiringAppException):
    def __init__(self):
        super().__init__("You are not authorized to apply for this position", status_code=403)