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


def mask_operation_from(operation):
    operation_from = operation.get('from')

    if operation_from:
        parts = operation_from.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            return f"{" ".join(parts[:-1])} {masked_numbers}"
        else:
            return f'Счёт **{numbers[-4:]}'


def mask_operation_to(operation):
    operation_to = operation.get('to')

    if operation_to:
        parts = operation_to.split(' ')
        numbers = parts[-1]
        if len(numbers) == 20:
            return f'Счёт **{numbers[-4:]}'

