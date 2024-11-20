def load_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()


def yaml_to_json(raw_yaml: str) -> dict:
    raw_yaml = raw_yaml.replace(': ', '": "')
    raw_yaml = raw_yaml.replace(':\n', '": [\n')
    raw_yaml = raw_yaml.replace('\n', '",\n')
    raw_yaml = raw_yaml.replace('    ', '    "')
    raw_yaml = raw_yaml.replace('    "  - ', '         "')
    raw_yaml = raw_yaml.replace('[",', '[')
    raw_yaml = raw_yaml.replace(' - ', '  {"')
    raw_yaml = raw_yaml.replace(',\n   {', '},\n   {')
    raw_yaml = raw_yaml.replace(',\n    "r', '\n    ],\n    "r')
    raw_yaml = raw_yaml.replace(',\nsaturday', '}\n],\n"saturday')
    raw_yaml = raw_yaml.replace('""""', '""')
    raw_yaml = '{"' + raw_yaml + '"}\n]\n}'
    return(raw_yaml)


def save_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(data)


if __name__ == '__main__':
    save_file('main_task/result.json', yaml_to_json(load_file('shedule.yaml')))
