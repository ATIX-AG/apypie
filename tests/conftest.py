import json

import py.path
import pytest

import apypie


@pytest.fixture
def fixture_dir():
    return py.path.local(__file__).realpath() / '..' / 'fixtures'


@pytest.fixture
def api(fixture_dir, requests_mock, tmpdir):
    with fixture_dir.join('dummy.json').open() as read_file:
        data = json.load(read_file)
    requests_mock.get('https://api.example.com/apidoc/v1.json', json=data)
    return apypie.Api(uri='https://api.example.com', apidoc_cache_dir=tmpdir.strpath)


@pytest.fixture
def resource(api):
    return api.resource('users')


@pytest.fixture
def action(resource):
    return resource.action('show')
