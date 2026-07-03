from dataclasses import dataclass


@dataclass
class RegisterResult:
    SUCCESS = "success"
    MISSING_FIELD = "missing_field"
    PASSWORD_MISSMATCH = "password_mismatch"
