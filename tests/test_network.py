import socket
import json

def test_valid_json_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080))
        
        test_data = {"action": "ping", "value": 1}
        s.sendall(json.dumps(test_data).encode('utf-8'))
        
        response = s.recv(1024)
        response_data = json.loads(response.decode('utf-8'))
        assert response_data["status"] == "success"
        print("Test valid berhasil")

def test_invalid_json_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080))
        
        s.sendall(b"Ini bukan JSON")
        
        response = s.recv(1024)
        response_data = json.loads(response.decode('utf-8'))
        assert response_data["status"] == "error"
        print("Test invalid berhasil")

if __name__ == "__main__":
    test_valid_json_request()
    test_invalid_json_request()