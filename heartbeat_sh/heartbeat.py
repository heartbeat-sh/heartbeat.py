from datetime import timedelta
from typing import Any, Protocol


class RequestCallable(Protocol):
    def __call__(self, *, method: str, url: str) -> Any:
        ...


class HeartbeatClient:
    def __init__(self, subdomain: str, request: RequestCallable = None):
        self.subdomain = subdomain
        self.request = request or _default_request

        self.proto = "https"
        self.host = "heartbeat.sh"
        self.base_url = f"{self.proto}://{self.subdomain}.{self.host}/"

    def get_beats(self):
        r = self.request(method="GET", url=f"{self.base_url}heartbeats")
        return r["Heartbeats"]

    def send_beat(
        self,
        name: str,
        warning_timeout: timedelta = None,
        error_timeout: timedelta = None,
    ):
        query = ""
        if warning_timeout is not None:
            query += f"?warning={int(warning_timeout.total_seconds())}"
        if error_timeout is not None:
            query += "&" if len(query) > 0 else "?"
            query += f"error={int(error_timeout.total_seconds())}"

        return self.request(method="POST", url=f"{self.base_url}beat/{name}{query}")

    def delete_beat(self, name):
        return self.request(method="DELETE", url=f"{self.base_url}beat/{name}")


def _default_request(*, method: str, url: str) -> Any:
    # noinspection PyUnresolvedReferences
    import requests  # Local import, because this is an optional dependency.

    return requests.request(
        method=method,
        url=url,
        timeout=3,
    ).json()
