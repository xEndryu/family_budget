import os


def get_docker_secret(secret_name, secret_path="/run/secrets"):
    """
    Function for getting docker secrets
    :param secret_name: name of the secret
    :param secret_path: used only for pytest
    :return: secret value
    """
    file_path = f"{secret_path}/{secret_name}"
    if os.path.exists(file_path):
        with open(file_path, 'r') as fp:
            secret_value = fp.read()
            return secret_value
    else:
        return None
