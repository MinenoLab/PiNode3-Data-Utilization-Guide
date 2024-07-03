import paramiko
from scp import SCPClient

def download(hostname, port=22, username="pi", password="pi", sample_data_path="/home/pinode3/data/image/sample/", local_data_path="./"):
    _scp_get_files(sample_data_path, local_data_path, hostname, port, username, password)


def _create_ssh_client(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=port, username=username, password=password)
    return ssh

def _scp_get_files(remote_path, local_path, hostname, port=22, username=None, password=None):
    try:
        # SSHクライアントの作成
        ssh = _create_ssh_client(hostname, port, username, password)
        
        # SCPクライアントの作成
        scp = SCPClient(ssh.get_transport())
        
        # ファイルの取得
        scp.get(remote_path, local_path, recursive=True)
        
        print(f"Files from {remote_path} have been successfully copied to {local_path}")
        
        # SCPクライアントのクローズ
        scp.close()
        # SSHクライアントのクローズ
        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")