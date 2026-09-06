import bcrypt


def hash_secret_code(secret_code: str) -> str:
    return bcrypt.hashpw(secret_code.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_secret_code(secret_code: str, hashed: str) -> bool:
    return bcrypt.checkpw(secret_code.encode("utf-8"), hashed.encode("utf-8"))
