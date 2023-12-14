import paramiko

# Remote server credentials
hostname = 'your_remote_server_ip'
port = 22  # default SSH port
username = 'your_username'
password = 'your_password'

# The path of the file you want to write on the remote server
remote_file_path = '/path/to/remote/file.txt'

def log_keys(client, content_to_write):
    # Connect to the server
    try:
        client.connect(hostname, port, username, password)

        # Use SFTP to write to the file
        with client.open_sftp() as sftp:
            with sftp.file(remote_file_path, 'w') as remote_file:
                remote_file.write(content_to_write)
        print("File written successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        client.close()
