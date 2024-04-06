import json


def open_json_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)