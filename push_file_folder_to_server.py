import paramiko
from scp import SCPClient

server = '192.168.x.x'
port = '22'
user='USERNAME'
password= 'PASSWORD'
source = '/path/of/source/folder_or_file'
Destination = '/path/to/destination/folder/'


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client



ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
scp.put(source, Destination, recursive=True)
scp.close()
