from httpclient.retry import RetryPolicy

def test_backoff_fail_first_attempt():
    p=RetryPolicy(backoff_factor=1)
    assert p.get_backoff(1)==1

def test_backoff_fail_second_attempt():
    p=RetryPolicy(backoff_factor=1)
    assert p.get_backoff(2)==2

def test_backoff_zero_factor_pass():
    p=RetryPolicy(backoff_factor=0)
    assert p.get_backoff(1)==0

def test_custom_retry_on_pass():
    p=RetryPolicy(retry_on=[429,503])
    assert 429 in p.retry_on and 502 not in p.retry_on
