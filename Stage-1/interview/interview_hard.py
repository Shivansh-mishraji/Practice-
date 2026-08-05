
import time
import functools

class RateLimitExceed(Exception):
    def __init__(self,retry_after:float) -> None :
        self.retry_after = retry_after
    def __str__(self):
        return f"Rate limit exceeded. Retry after {self.retry_after:.2f} seconds."

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        self._capacity = capacity
        self._refill_rate = refill_rate

    @property
    def refill_rate(self):
        return self._refill_rate
    
    @refill_rate.setter
    def refill_rate(self,token:float) -> None:
        if token < 0.0:
            raise ValueError(f"Token must be greater than 0, got {token}") 
        self._refill_rate += token

    @property
    def capacity(self):
            return self._capacity
        
    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Capacity must be > 0")
        self._capacity = value

    @property
    def tokens(self):
        time.time() - self._last_refill_time
    def consume(self, amount: int = 1) -> bool:
        if amount <=0:
            raise ValueError(f"Amount must be greater than 0, got {amount}")
        refill_tokens()
        if self.tokens >=amount:
            self.tokens -=amount
            return True
        return False

def rate_limit(bucket):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
            if bucket.consume(1):
                return func(*args,**kwargs)
            raise RateLimitExceeded(bucket.tokens)
    return wrapper

if __name__ == "__main__":
    my_bucket = TokenBucket(capacity=5, refill_rate=1) # 5 tokens, refill 1 per second

    @rate_limit(bucket=my_bucket)
    def generate_ai_response(prompt: str) -> str:
        """Generates a mock AI response."""
        return f"AI Answer for: {prompt}"

    


