import socket
import json

HOST = '127.0.0.1'
PORT = 8080

def handle_client(conn, addr):
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                
                request = json.loads(data.decode('utf-8'))
                
                response = {
                    "status": "success",
                    "data_received": request
                }
                conn.sendall(json.dumps(response).encode('utf-8'))
                
            except json.JSONDecodeError:
                error_response = {"status": "error", "message": "Format JSON tidak valid"}
                conn.sendall(json.dumps(error_response).encode('utf-8'))
            except ConnectionResetError:
                break
            except Exception as e:
                error_response = {"status": "error", "message": str(e)}
                conn.sendall(json.dumps(error_response).encode('utf-8'))
                break

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server aktif")
        
        while True:
            try:
                conn, addr = server_socket.accept()
                handle_client(conn, addr)
            except KeyboardInterrupt:
                print("Server nonaktif")
                break

if __name__ == "__main__":
    start_server()