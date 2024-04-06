import json


def open_json_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


def filter_operations(data):
    filtered_list = []
    for operation in data:
        if operation.get('state') == 'EXECUTED':
            filtered_list.append(operation)
    return filtered_list


def sort_operations(operations_data: list[dict]) -> list[dict]:
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list
