import socket
from typing import List

def scan_ports(target: str, start_port: int, end_port: int) -> List[int]:
    """
    Scan a range of ports on a target IP address.
    
    :param target: IP address of the target.
    :param start_port: Starting port number.
    :param end_port: Ending port number.
    :return: List of open ports.
    """
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
import argparse
from toolkit.port_scanner import scan_ports
def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Port Scanner
    port_parser = subparsers.add_parser("scan", help="Scan open ports on a target")
    port_parser.add_argument("target", help="Target IP address")
    port_parser.add_argument("--start", type=int, default=1, help="Starting port")
    port_parser.add_argument("--end", type=int, default=1024, help="Ending port")

if __name__ == "__main__":
    main()
