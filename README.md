# httpclient

`httpclient` 是一个轻量 HTTP 调用封装，内置缓存、重试策略和限流组件，便于拼装简单请求客户端。

## 组件

- `HttpClient`：封装 GET/POST/PUT/DELETE 调用
- `ResponseCache`：基于 `OrderedDict` 的响应缓存容器
- `RetryPolicy`：提供重试状态码与退避时长计算
- `RateLimiter`：令牌桶风格的每秒请求控制

## 快速使用

```bash
pip install -e .
```

```python
from httpclient import HttpClient, ResponseCache, RetryPolicy, RateLimiter

cache = ResponseCache(capacity=100)
client = HttpClient(cache=cache)
policy = RetryPolicy(max_retries=3, backoff_factor=0.5, retry_on=[500, 502, 503])
limiter = RateLimiter(requests_per_second=5)

if limiter.acquire():
    resp = client.get("https://httpbin.org/get")
    print(resp.status_code)
    print(policy.get_backoff(1))
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
