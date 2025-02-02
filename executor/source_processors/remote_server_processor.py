import io
import logging
import subprocess

import paramiko

from executor.source_processors.processor import Processor

logger = logging.getLogger(__name__)


def reconstruct_rsa_key(key_string):
    key_string = key_string.replace('-----BEGIN RSA PRIVATE KEY-----', '').replace('-----END RSA PRIVATE KEY-----', '')

    # Remove any whitespace or line breaks
    key_string = ''.join(key_string.split())

    # Add line breaks to reconstruct the key
    reconstructed_key = '-----BEGIN RSA PRIVATE KEY-----\n'
    reconstructed_key += '\n'.join([key_string[i:i + 64] for i in range(0, len(key_string), 64)])
    reconstructed_key += '\n-----END RSA PRIVATE KEY-----'

    return reconstructed_key


class RemoteServerProcessor(Processor):
    client = None

    def __init__(self, remote_host=None, remote_user=None, remote_password=None, remote_pem=None):
        self.remote_host = remote_host
        self.remote_user = remote_user
        self.remote_password = remote_password
        self.remote_pem = remote_pem

    def get_connection(self):
        try:
            if self.remote_host and self.remote_user and self.remote_password:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=self.remote_host, username=self.remote_user, password=self.remote_password)
            elif self.remote_host and self.remote_user and self.remote_pem:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                key = paramiko.RSAKey.from_private_key(io.StringIO(reconstruct_rsa_key(self.remote_pem)))
                client.connect(hostname=self.remote_host, username=self.remote_user, pkey=key)
            elif self.remote_host and self.remote_user:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=self.remote_host, username=self.remote_user)
            else:
                client = None
            return client
        except Exception as e:
            logger.error(f"Exception occurred while creating remote connection with error: {e}")
            raise e

    def test_connection(self):
        try:
            self.get_connection()
            return True
        except Exception as e:
            logger.error(f"Exception occurred while creating remote connection with error: {e}")
            raise e

    def execute_command(self, command):
        try:
            client = self.get_connection()
            if client:
                try:
                    stdin, stdout, stderr = client.exec_command(command)
                    output = stdout.read().decode('utf-8')
                    return output.strip()
                except paramiko.AuthenticationException as e:
                    logger.error(f"Authentication error: {str(e)}")
                    raise e
                except paramiko.SSHException as e:
                    logger.error(f"SSH connection error: {str(e)}")
                    raise e
                except Exception as e:
                    logger.error(f"Error: {str(e)}")
                    raise e
                finally:
                    client.close()
            else:
                try:
                    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            universal_newlines=True)
                    return result.stdout.strip()
                except subprocess.CalledProcessError as e:
                    logger.error(f"Error executing command{command}: {e}")
                    raise e
        except Exception as e:
            logger.error(f"Exception occurred while executing remote command with error: {e}")
            raise e
