from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture()
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/16453890?v=4'
    resp_mock.json.return_value = {
        'login': 'gelhen', 'id': 16453890,
        'node_id': 'MDQ6VXNlcjE2NDUzODkw',
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('gelhen')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('gelhen')
    assert 'https://avatars1.githubusercontent.com/u/16453890?v=4' == url