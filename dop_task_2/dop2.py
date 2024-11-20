import re


def load_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()


def yaml_to_json(raw_yaml: str) -> dict:
    raw_yaml = re.sub(r'(\S+): (.+)', r'"\1": "\2",', raw_yaml)
    raw_yaml = re.sub(r'(\S+):\n((?:      - \d+\n)+)', r'"\1": [\n\2    ],\n', raw_yaml)
    raw_yaml = re.sub(r'      - (\d+)', r'        \1,', raw_yaml)
    raw_yaml = re.sub(r'  - (.+(?:\n    .+){0,}),', r'    {\1},', raw_yaml)
    raw_yaml = re.sub(r'(.+):((?:\n    .+)+)', r'"\1": [\2\n],', raw_yaml)
    raw_yaml = re.sub(r',(?=\n.*])', r'', raw_yaml)
    raw_yaml = '{' + raw_yaml + '\n}'
    raw_yaml = re.sub(r',(?=\n})', r'', raw_yaml)
    raw_yaml = re.sub(r'""""', r'""', raw_yaml)
    return(raw_yaml)


def save_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(data)


if __name__ == '__main__':
    save_file('dop_task_2/result.json', yaml_to_json(load_file('shedule.yaml')))
