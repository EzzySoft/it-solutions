class InvalidSessionError(ValueError):
    def __init__(self):
        super().__init__("Invalid session ID")


class InvalidCredentialsError(ValueError):
    def __init__(self):
        super().__init__("Invalid credentials")


class UsernameInUseError(ValueError):
    def __init__(self):
        super().__init__("The username is already taken")


class EmailInUseError(ValueError):
    def __init__(self):
        super().__init__("The email is already taken")


class UserNotFoundError(ValueError):
    def __init__(self):
        super().__init__("User not found")


class AdNotFoundError(ValueError):
    def __init__(self):
        super().__init__("Advertisement not found")
