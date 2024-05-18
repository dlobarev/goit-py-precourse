import socket
from cryptography.fernet import Fernet
key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
cipher = Fernet(key)
def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        with open("secret.txt", "rb") as fh:
            bdata = fh.read(1024)
            while (bdata):
                print(f'Send data: {bdata}')
                sock.send(cipher.encrypt(bdata))
                bdata = fh.read(1024)
    print(f'Data transfer completed')

if __name__ == '__main__':
    run_client('localhost', 8080)
