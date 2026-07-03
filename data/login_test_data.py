from dataclasses import dataclass

@dataclass
class LoginResult:
    SUCCESS = "success"
    WRONG_USER = "wrong_user"
    WRONG_PASSWORD = "wrong_password"
