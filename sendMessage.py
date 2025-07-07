import socket

HOST = "127.0.0.1"
PORT = 12345

def notifyInStock(itemName):
    msg = f"Item in stock: {itemName}"
    try:
        with socket.create_connection((HOST, PORT), timeout=2) as sock:
            sock.sendall(msg.encode("utf-8"))
    except Exception as e:
        print(f"Failed to send Discord notification: {e}")