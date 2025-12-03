import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    users = []

    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    users.append(line)
    except FileNotFoundError:
        pass

    user_id = len(users)
    hashed_pw = hash_password(PPassword)

    new_entry = f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed_pw}\n"

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(new_entry)


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hashed_pw = hash_password(PPassword)

    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                user_id, username, stored_hash = line.split(DELIMITER)

                if username == PUsername and stored_hash == hashed_pw:
                    return True
    except FileNotFoundError:
        return False

    return False


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                user_id, username, _ = line.split(DELIMITER)

                if username == PUsername:
                    return [user_id, username]

    except FileNotFoundError:
        return None

    return None


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    updated_lines = []
    hashed_new = hash_password(PNewPassword)

    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                user_id, username, stored_hash = line.split(DELIMITER)

                if username == PUsername:
                    updated_line = f"{user_id}{DELIMITER}{username}{DELIMITER}{hashed_new}"
                else:
                    updated_line = line

                updated_lines.append(updated_line)

    except FileNotFoundError:
        return

    with open(CREDENTIALS_FILE, "w") as f:
        for line in updated_lines:
            f.write(line + "\n")
