# Heartbeat.sh Python Client

This is a Python client library for [heartbeat.sh](https://heartbeat.sh).

## Quick start

Install with `pip install heartbeat-sh requests`

```python
from datetime import timedelta
from heartbeat_sh import HeartbeatClient

HeartbeatClient("example").send_beat(
    "example:python",
    timedelta(days=1, hours=2),
    timedelta(days=2)
)
```

## Use a custom requests library (Dependency Injection)

By default, this module uses the [`requests`](https://docs.python-requests.org/en/latest/) library to make HTTP 
requests. This is not a requirement. You may inject any request library:

```python
from datetime import timedelta
from heartbeat_sh import HeartbeatClient

def request(url: str, method: str):
    return {
        "fake": "json result"
    }

HeartbeatClient(
    subdomain="example",
    request=request,
).send_beat(
    "example:python",
    timedelta(days=1, hours=2),
    timedelta(days=2)
)
```

## Links
- PyPI: https://pypi.org/project/heartbeat-sh/
