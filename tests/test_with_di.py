import unittest
from datetime import timedelta
from typing import Any

from heartbeat_sh import HeartbeatClient


class TestWithDi(unittest.TestCase):
    def setUp(self) -> None:
        self.client = HeartbeatClient(
            subdomain="example",
            request=self.request,
        )

    def request(self, *, method: str, url: str) -> Any:
        if method == "DELETE" and url == "https://example.heartbeat.sh/beat/kaboom":
            return {
                "Name": "kaboom",
                "Warning": 120,
                "Error": 300,
                "Age": 28,
                "Status": "OK",
                "LastBeat": "2022-05-03T06:38:02Z",
            }

        if method == "GET" and url == "https://example.heartbeat.sh/heartbeats":
            return {
                "Heartbeats": [
                    {
                        "Name": "foo",
                        "Warning": 7200,
                        "Error": 86400,
                        "Age": 1408,
                        "Status": "OK",
                        "LastBeat": "2022-05-03T06:15:02Z",
                    },
                    {
                        "Name": "bar",
                        "Warning": 7200,
                        "Error": 86400,
                        "Age": 1407,
                        "Status": "OK",
                        "LastBeat": "2022-05-03T06:15:03Z",
                    },
                ]
            }

        if (
            method == "POST"
            and url
            == "https://example.heartbeat.sh/beat/kaboom?warning=93600&error=172800"
        ):
            return {
                "Name": "kaboom",
                "Warning": 93600,
                "Error": 172800,
                "Age": 0,
                "Status": "OK",
                "LastBeat": "2022-05-03T06:40:48.420356888Z",
            }

        raise NotImplementedError(
            f"TODO: Implement mock response for `{method} {url}`."
        )

    def test_get_beats(self):
        self.assertEqual(
            [
                {
                    "Name": "foo",
                    "Warning": 7200,
                    "Error": 86400,
                    "Age": 1408,
                    "Status": "OK",
                    "LastBeat": "2022-05-03T06:15:02Z",
                },
                {
                    "Name": "bar",
                    "Warning": 7200,
                    "Error": 86400,
                    "Age": 1407,
                    "Status": "OK",
                    "LastBeat": "2022-05-03T06:15:03Z",
                },
            ],
            self.client.get_beats(),
        )

    def test_send_beat(self):
        self.assertEqual(
            {
                "Name": "kaboom",
                "Warning": 93600,
                "Error": 172800,
                "Age": 0,
                "Status": "OK",
                "LastBeat": "2022-05-03T06:40:48.420356888Z",
            },
            self.client.send_beat(
                name="kaboom",
                warning_timeout=timedelta(days=1, hours=2),
                error_timeout=timedelta(days=2),
            ),
        )

    def test_delete_beat(self):
        self.assertEqual(
            {
                "Name": "kaboom",
                "Warning": 120,
                "Error": 300,
                "Age": 28,
                "Status": "OK",
                "LastBeat": "2022-05-03T06:38:02Z",
            },
            self.client.delete_beat(name="kaboom"),
        )


if __name__ == "__main__":
    unittest.main()
