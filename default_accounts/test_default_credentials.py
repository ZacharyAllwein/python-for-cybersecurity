from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
import paramiko
import telnetlib


def ssh_login(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(
                f"ssh login success ful on {host}:{port} username:{username} password:{password}"
            )
    except:
        return
    ssh.close()


def telnet_login(host, port, username, password):

    # uhhhhh mostly I just wondered if I could
    username, password = map(
        lambda cred: bytes(f"{cred}\n", "utf-8"), (username, password)
    )

    tn = telnetlib.Telnet(host, port)
    tn.read_until(b"login: ")
    tn.write(username)

    tn.read_until(b"Password: ")
    tn.write(password)

    try:
        result = tn.expect([b"Last login"], 2)
        if result[0] > 0:
            print(
                f"telnet login success ful on {host}:{port} username:{username} password:{password}"
            )
        tn.close()
    except EOFError:
        print(f"Login failed {username} {password}")


if __name__ == "__main__":
    host = "127.0.0.1"
    with open("defaults.txt", "r") as file:
        for line in file:
            username, password = line.split(",")

            ssh_login(host, 22, username, password)
            telnet_login(host, 23, username, password)
