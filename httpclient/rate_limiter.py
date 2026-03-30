import time

class RateLimiter:
    def __init__(self, requests_per_second=1):
        self.rate=requests_per_second
        self.tokens=requests_per_second
        self.last=time.time()
    def acquire(self):
        now=time.time()
        elapsed=now-self.last
        self.tokens=min(self.rate, self.tokens + int(elapsed*self.rate))
        self.last=now
        if self.tokens>=1:
            self.tokens-=1
            return True
        return False
