import socket
import json

from core.ack_handler import validate_ack
from core.fault_injection import FaultInjector, make_incorrect_result
from core.service_registry import ServiceRegistry
from services.matrix_services import matrix_3x3
from services.string_services import char_count, word_count, reverse, remove_vowels

HOST = '0.0.0.0'
PORT = 5001
ERROR_RATE = 0.30

SERVICE_NAMES = ("char_count", "word_count", "reverse", "remove_vowels", "matrix_3x3")
STRING_SERVICES = {"char_count": char_count, "word_count": word_count, "reverse": reverse, "remove_vowels": remove_vowels}


def send_json(conn, data):
    conn.sendall((json.dumps(data) + "\n").encode())


def execute_service(service, params):
    if service in STRING_SERVICES:
        if "text" not in params:
            raise ValueError("params.text wajib diisi")

        response = STRING_SERVICES[service](params["text"])

        if response["status"] != "success":
            raise ValueError(response["message"])

        return response["result"]

    if service == "matrix_3x3":
        if "matrix" not in params:
            raise ValueError("params.matrix wajib diisi")

        return matrix_3x3(params["matrix"])

    raise ValueError("service tidak dikenal")


def process_request(message, registry, fault_injector):
    if not isinstance(message, dict) or message.get("type") != "request":
        return None, {"type": "response", "status": "error", "message": "request tidak valid"}

    request_id, service, params = message.get("request_id"), message.get("service"), message.get("params", {})

    if not request_id:
        return None, {"type": "response", "status": "error", "message": "request_id wajib diisi"}

    if service not in SERVICE_NAMES:
        return None, {"type": "response", "request_id": request_id, "status": "error", "message": "service tidak dikenal"}

    if not registry.is_active(service):
        return None, {"type": "response", "request_id": request_id, "service": service, "status": "error", "message": "service_disabled"}

    try:
        result = execute_service(service, params)
    except (ValueError, TypeError) as error:
        return None, {"type": "response", "request_id": request_id, "service": service, "status": "error", "message": str(error)}

    if fault_injector.should_inject():
        result = make_incorrect_result(service, result)

    return (request_id, service), {"type": "response", "request_id": request_id, "service": service, "status": "success", "result": result}


def handle_client(conn, addr, registry, fault_injector):
    print(f"Client terhubung: {addr}")
    pending = None

    with conn:
        reader = conn.makefile("r", encoding="utf-8")

        while True:
            try:
                line = reader.readline()

                if not line:
                    print(f"Client terputus: {addr}")
                    return False

                try:
                    message = json.loads(line)
                except json.JSONDecodeError:
                    send_json(conn, {"type": "error", "status": "error", "message": "JSON tidak valid"})
                    continue

                if pending:
                    error = validate_ack(message, pending)

                    if error:
                        send_json(conn, {"type": "ack_result", "status": "error", "message": error})
                        continue

                    request_id, service = pending
                    correct = message["correct"]

                    if not correct:
                        registry.disable(service)
                        print(f"Service dinonaktifkan: {service}")

                    pending = None
                    shutdown = registry.all_disabled()

                    send_json(conn, {"type": "ack_result", "request_id": request_id, "service": service, "status": "accepted", "correct": correct, "active_services": registry.active_services(), "server_status": "shutdown" if shutdown else "running"})

                    if shutdown:
                        print("Semua service nonaktif. Server berhenti.")
                        return True

                    continue

                pending, response = process_request(message, registry, fault_injector)
                send_json(conn, response)

            except (ConnectionResetError, BrokenPipeError, OSError):
                print(f"Koneksi client terputus: {addr}")
                return False


def start_server():
    registry = ServiceRegistry(SERVICE_NAMES)
    fault_injector = FaultInjector(error_rate=ERROR_RATE)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Server aktif di {HOST}:{PORT}")
        print("Service:", ", ".join(registry.active_services()))

        while not registry.all_disabled():
            try:
                conn, addr = server.accept()

                if handle_client(conn, addr, registry, fault_injector):
                    break

            except KeyboardInterrupt:
                break

    print("Server nonaktif")


if __name__ == "__main__":
    start_server()