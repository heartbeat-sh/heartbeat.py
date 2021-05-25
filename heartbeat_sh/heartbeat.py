from datetime import timedelta

import requests


class HeartbeatClient:
    def __init__(self, subdomain: str):
        self.subdomain = subdomain

        self.proto = "https"
        self.host = "heartbeat.sh"
        self.base_url = f"{self.proto}://{self.subdomain}.{self.host}/"

    def send_beat(self, name: str, warning_timeout: timedelta = None, error_timeout: timedelta = None):
        query = ""
        if warning_timeout is not None:
            query += f"?warning={int(warning_timeout.total_seconds())}"
        if error_timeout is not None:
            query += "&" if len(query) > 0 else "?"
            query += f"error={int(error_timeout.total_seconds())}"

        return requests.post(f"{self.base_url}beat/{name}{query}")

    def delete_beat(self, name):
        return requests.delete(f"{self.base_url}beat/{name}")
