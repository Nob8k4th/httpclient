from httpclient.cache import ResponseCache
from httpclient.rate_limiter import RateLimiter

def test_capacity_one_fail():
    c=ResponseCache(capacity=1)
    c.set('a',1)
    c.set('b',2)
    assert len(c.store)==1

def test_get_none_pass():
    assert ResponseCache().get('x') is None

def test_update_existing_pass():
    c=ResponseCache()
    c.set('a',1)
    c.set('a',2)
    assert c.get('a')==2

def test_rate_limiter_fail_boundary():
    rl=RateLimiter(1)
    rl.tokens=0
    rl.last = rl.last - 0.9
    assert rl.acquire() is True

def test_cache_lru_order_pass():
    c=ResponseCache(capacity=10)
    c.set('a',1)
    c.set('b',2)
    c.get('a')
    assert list(c.store.keys())==['b','a']
