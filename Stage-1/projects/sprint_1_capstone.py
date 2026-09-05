# """📋 Capstone Requirements Checklist

# 1. Custom Exception: SecurityViolationError
# Inherits from Exception.
# Stores message: str in self.message.
# __str__() returns f"[SECURITY VIOLATION] {self.message}".

class SecurityViolationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
    def __str__(self):
        return f"[SECURITY VIOLATION] {self.message}"
    
# 2. Class: User
# __init__(self, username: str, role: str) -> None
# Getter @property def role(self) -> str: returns self._role
# Setter @role.setter def role(self, value: str) -> None:
# Validates value in ("admin", "user"). If invalid, raises ValueError.
# Sets self._role = value.

class User:
    def __init__(self, username: str, role: str) ->None:
        self.username = username
        self.role = role
    @property
    def role(self) -> str:
        return self._role
    @role.setter
    def role(self,value: str) -> None:
        if value not in ("admin", "user"):
            raise ValueError(" Invalid role.")
        self._role = value
# 3. Decorator: @require_admin
# Uses @wraps(func).
# wrapper(user: User, *args, **kwargs):
# If user.role != "admin", raises SecurityViolationError(...).
# Otherwise, calls and returns func(user, *args, **kwargs).

import functools
def require_admin(func):
    @functools.wraps(func)
    def wrapper(user: User, *args, **kwrgs):
        if user.role != "admin":
            raise SecurityViolationError(f"User {user.username} is not an admin!")
        return func(user, *args, **kwrgs)
    return wrapper

# 4. Function: log_security_event()
# python
# @require_admin
# def log_security_event(user: User, storage_dir: Path, event_name: str, status: str) -> Path:
# Creates storage_dir if missing (storage_dir.mkdir(...)).
# Creates path event_file = storage_dir / f"{event_name}.json".
# Writes {"user": user.username, "event": event_name, "status": status} into event_file as JSON (with open(..., "w") + json.dump).
# Returns event_file.

from pathlib import Path
import json

@require_admin
def log_security_event(user: User, storage_dir: Path, event_name: str, status: str) -> Path:
    storage_dir.mkdir(parents = True, exist_ok = True)
    event_file = storage_dir / f"{event_name}.json"
    with open(event_file, "w", encoding = "utf-8") as f:
        data = {"user": user.username, "event": event_name, "status": status}
        json.dump(data, f)
    return event_file
    
# 5. Generator Function: stream_audit_logs()
# python
# def stream_audit_logs(storage_dir: Path) -> Generator[dict, None, None]:
# Loops through all JSON files: for file_path in storage_dir.glob("*.json"):
# Reads each file using with open(..., "r") + json.load()
# yield each dictionary one by one.
# """
from typing import Generator
def stream_audit_logs(storage_dir: Path) -> Generator[dict, None, None]:
    for file_path in storage_dir.glob("*.json"):
        with open(file_path, "r", encoding = "utf-8") as f:
            content = json.load(f)
            yield content

#Test

if __name__ == "__main__":
    vault_dir = Path("stage2_storage/capstone_vault")

    admin_user = User("shivansh_admin", "admin")
    regular_user = User("guest_user", "user")

    # Test 1: Admin can log security events
    file1 = log_security_event(admin_user, vault_dir, "event_01", "SUCCESS")
    file2 = log_security_event(admin_user, vault_dir, "event_02", "WARNING")
    assert file1.exists()

    # Test 2: Non-admin fails with SecurityViolationError
    try:
        log_security_event(regular_user, vault_dir, "event_03", "FAIL")
        print("BUG: Non-admin should have failed!")
    except SecurityViolationError as e:
        print(f"Correctly caught: {e}")

    # Test 3: Generator streams all audit logs
    logs = list(stream_audit_logs(vault_dir))
    assert len(logs) == 2
    assert logs[0]["user"] == "shivansh_admin"

    print("\nCAPSTONE PASSED! YOU BUILT A PRODUCTION-GRADE BACKEND MODULE!")
