import unittest
import socket
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
class TestNetwork(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            [sys.executable, "server.py"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(20):
            try:
                with socket.create_connection(("127.0.0.1", 8080), timeout=0.1):
                    return
            except OSError:
                time.sleep(0.1)
        raise RuntimeError("Server gagal dijalankan")
    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait(timeout=2)

    def test_valid_json_request(self):
        with socket.create_connection(("127.0.0.1", 8080), timeout=2) as s:
            reader = s.makefile("r")
            request = {
                "type": "request",
                "request_id": "1",
                "service": "char_count",
                "params": {"text": "hello"},
            }
            s.sendall((json.dumps(request) + "\n").encode())
            response = json.loads(reader.readline())
            self.assertEqual(response["status"], "success")
            self.assertEqual(response["service"], "char_count")

            ack = {
                "type": "ack",
                "request_id": "1",
                "correct": response["result"] == 5,
            }

            s.sendall((json.dumps(ack) + "\n").encode())
            ack_response = json.loads(reader.readline())

            self.assertEqual(ack_response["status"], "accepted")

    def test_invalid_json_request(self):
        with socket.create_connection(("127.0.0.1", 8080), timeout=2) as s:
            reader = s.makefile("r")

            s.sendall(b"Ini bukan JSON\n")
            response = json.loads(reader.readline())

            self.assertEqual(response["status"], "error")


if __name__ == "__main__":
    unittest.main()