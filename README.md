# Heartbeat.sh Python Client

This is a Python client library for [heartbeat.sh](https://heartbeat.sh). Hosted on PyPI here: https://pypi.org/project/heartbeat-sh/

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
