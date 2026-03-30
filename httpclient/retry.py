class RetryPolicy:
    def __init__(self, max_retries=2, backoff_factor=1.0, retry_on=None):
        self.max_retries=max_retries
        self.backoff_factor=backoff_factor
        self.retry_on=retry_on or [500,502,503]
    def get_backoff(self, attempt):
        return self.backoff_factor * (2 ** attempt)
