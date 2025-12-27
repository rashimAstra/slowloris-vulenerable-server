import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 8080
HEADER_TIMEOUT = 10       # seconds allowed per header chunk
MAX_HEADER_TIME = 120     # total time allowed to send headers

def handle_client(conn, addr):
    conn.settimeout(HEADER_TIMEOUT)
    start = time.time()
    data = b""

    try:
        while True:
            chunk = conn.recv(1)
            if not chunk:
                break

            data += chunk

            # End of headers
            if b"\r\n\r\n" in data:
                break

            # Only slow clients trigger this path
            if time.time() - start > MAX_HEADER_TIME:
                # Simulate Slowloris vulnerability
                time.sleep(60)
                break

        # Normal clients reach here quickly
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK")

    except socket.timeout:
        # Slow header trickle → keep connection open
        time.sleep(60)

    except Exception:
        pass

    finally:
        conn.close()


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(200)

    print(f"Slowloris-conditionally-vulnerable server on http://localhost:{PORT}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


start_server()
