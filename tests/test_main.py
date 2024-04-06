import pytest
from src.main import open_json_file, filter_operations


@pytest.fixture
def test_data():
    return [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'CANCELLED'}]


def test_open_json_file():
    assert type(open_json_file('test_data.json')) == dict
    assert open_json_file('test_data.json') == {"test": "test"}


def test_filter_operations(test_data):
    assert len(filter_operations(test_data)) == 2
    assert filter_operations(test_data) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
