# Heartbeat.sh Python Client

This is a Python client library for [heartbeat.sh](https://heartbeat.sh).

## Usage

Install with `pip install heartbeat-sh`

```Python
from datetime import timedelta
from heartbeat_sh import HeartbeatClient

HeartbeatClient("example").send_beat(
    "example:python",
    timedelta(days=1, hours=2),
    timedelta(days=2)
)
```

## Links
- PyPI: https://pypi.org/project/heartbeat-sh/
