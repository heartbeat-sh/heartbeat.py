import unittest
from datetime import timedelta

from heartbeat_sh import HeartbeatClient


class TestSend(unittest.TestCase):
    def test_example(self):
        HeartbeatClient("example").send_beat("example:python", timedelta(days=1, hours=2), timedelta(days=2))


if __name__ == "__main__":
    unittest.main()
