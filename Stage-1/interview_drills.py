"""
===============================================================================
🎯 BACKEND AI ENGINEER — INTERVIEW DRILLS (Sprint 1)
===============================================================================
Rules:
1. Replace every `___` with the correct Python keyword, attribute, or code.
2. Fix any intentional bugs marked with `# FIXME`.
3. Run `python Stage-1/interview_drills.py` to test your solutions!
===============================================================================
"""

from dataclasses import dataclass
from functools import wraps
from typing import Callable, Any

# -----------------------------------------------------------------------------
# DRILL 1: Property & Private State (Interview Question: Rate Limiter Class)
# -----------------------------------------------------------------------------
class RateLimiter:
    def __init__(self, max_requests: int) -> None:
        # Fill in private attribute for max_requests
        self._max_requests = max_requests
        self._current_requests = 0

    @property
    def max_requests(self) -> int:
        """Read-only access to max_requests."""
        return self._max_requests

    @property
    def current_requests(self) -> int:
        return self._current_requests

    @current_requests.setter
    def current_requests(self, value: int) -> None:
        if value < 0:
            raise ValueError("Current requests cannot be negative")
        self._current_requests = value


# -----------------------------------------------------------------------------
# DRILL 2: Decorators & Wraps (Interview Question: API Endpoint Auth Guard)
# -----------------------------------------------------------------------------
def require_auth(func: Callable[..., Any]) -> Callable[..., Any]:
    # Fill in the decorator preservation helper
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Check if 'user_role' in kwargs equals 'admin'
        if kwargs.get("user_role") != "admin":
            raise PermissionError("Access denied: Admin role required")
        return func(*args, **kwargs)
    return wrapper


# -----------------------------------------------------------------------------
# DRILL 3: Dataclass & Magic Methods (Interview Question: API Response DTO)
# -----------------------------------------------------------------------------
@dataclass
class APIResponse:
    status_code: int
    data: dict

    def __len__(self) -> int:
        """Returns the number of keys in the data payload."""
        return len(self.data)


# -----------------------------------------------------------------------------
# TEST RUNNER (Do not modify — run this to verify your answers!)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Running Interview Drills Validation ===\n")

    # Test Drill 1
    limiter = RateLimiter(100)
    assert limiter.max_requests == 100, "Drill 1 Failed: max_requests getter"
    limiter.current_requests = 50
    assert limiter.current_requests == 50, "Drill 1 Failed: current_requests setter"
    try:
        limiter.current_requests = -10
        print("[FAIL] Drill 1 Failed: Setter did not raise ValueError for negative value")
    except ValueError:
        print("[PASS] Drill 1 PASSED: RateLimiter @property validation")

    # Test Drill 2
    @require_auth
    def delete_user(user_id: int, user_role: str = "guest") -> str:
        """Deletes a user account."""
        return f"User {user_id} deleted"

    assert delete_user.__name__ == "delete_user", "Drill 2 Failed: @wraps missing"
    try:
        delete_user(42, user_role="guest")
        print("[FAIL] Drill 2 Failed: Decorator did not raise PermissionError")
    except PermissionError:
        print("[PASS] Drill 2 PASSED: require_auth decorator")

    # Test Drill 3
    res = APIResponse(200, {"user_id": 1, "name": "Shivansh"})
    assert len(res) == 2, "Drill 3 Failed: __len__ method"
    print("[PASS] Drill 3 PASSED: Dataclass and __len__")

    print("\nALL DRILLS PASSED! You are ready for Sprint 1 Interview Questions.")
