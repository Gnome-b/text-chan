import bcrypt
from anyio import to_thread


async def hash_secret_code(secret_code: str) -> str:
    return await to_thread.run_sync(_hash_sync, secret_code)


def _hash_sync(secret_code: str) -> str:
    return bcrypt.hashpw(secret_code.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


async def verify_secret_code(secret_code: str, hashed: str) -> bool:
    return await to_thread.run_sync(_verify_sync, secret_code, hashed)


def _verify_sync(secret_code: str, hashed: str) -> bool:
    return bcrypt.checkpw(secret_code.encode("utf-8"), hashed.encode("utf-8"))
