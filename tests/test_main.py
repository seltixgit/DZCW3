import os
import pytest
from config import ROOT_DIR
from src.main import open_json_file, filter_operations, sort_operations, mask_operation_from, mask_operation_to, format_date

TEST_PATH_OPERATIONS = os.path.join(ROOT_DIR, 'tests', 'test_data.json')


@pytest.fixture
def test_data():
    return [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'CANCELLED'}]


def test_open_json_file():
    assert type(open_json_file(TEST_PATH_OPERATIONS)) == dict
    assert open_json_file(TEST_PATH_OPERATIONS) == {"test": "test"}


def test_filter_operations(test_data):
    assert len(filter_operations(test_data)) == 2
    assert filter_operations(test_data) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]


def test_sort_operations():
    operations_data = []
    assert sort_operations(operations_data) == []


def test_mask_operation_from():
    operation = {'from': 'Payment from 1234 5678 91'}
    assert mask_operation_from(operation) == 'Счёт **91'


def test_mask_operation_to():
    operation = {'to': 'Счет 64686473678894779589'}
    assert mask_operation_to(operation) == 'Счёт **9589'


def test_format_date():
    operation = {'date': '2022-12-01T10:30:00.123'}
    assert format_date(operation) == '01.12.2022'
