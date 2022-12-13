import pytest

from ..helpers.secrets import get_docker_secret


@pytest.fixture
def mock_secret_file(tmpdir_factory):
    testing_secret_name = "test_secret"
    testing_value = "val123"
    secret_base = tmpdir_factory.mktemp("secret")
    secret_path = secret_base.join(testing_secret_name)
    with open(secret_path, "w") as fp:
        fp.write(testing_value)
        return {
            "name": testing_secret_name,
            "value": testing_value,
            "path": secret_base,
        }


def test_docker_secret_get(mock_secret_file):
    secret = get_docker_secret(
        mock_secret_file["name"],
        secret_path=mock_secret_file["path"]
    )
    assert secret == mock_secret_file["value"]


def test_docker_secret_no_file():
    secret = get_docker_secret("test")
    assert secret is None


def test_docker_secret_empty_file(mock_secret_file):
    path = mock_secret_file["path"].join("empty")
    open(path, 'w').close()
    secret = get_docker_secret('empty', mock_secret_file["path"])
    assert not secret
