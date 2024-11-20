import re


def parse_value(value):
    # Убираем лишние пробелы
    value = value.strip()
    # Проверяем на строку
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    elif value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    # Если это число
    elif re.match(r"^-?\d+(\.\d+)?$", value):
        return float(value) if '.' in value else int(value)
    # Логические значения
    elif value in ["true", "false"]:
        return value == "true"
    # Null
    elif value in ["null", "Null", "NULL", "~"]:
        return None
    return value  # Если ничего не подошло, оставляем как есть


def parse_block(lines, indent_level=0):
    # print('parse_block', lines, indent_level)
    result = {}
    value_list = []
    key, value = None, None

    for i in range(len(lines)):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith('#'):  # Пропускаем пустые строки и комментарии
            continue

        current_indent = len(line) - len(line.lstrip())
        if current_indent != indent_level: # Пропускаем строки не того отступа
            continue

        line = line.strip()
        if line.startswith('- '):  # Если это элемент списка
            if len(lines) == i + 1 or '- ' in lines[i + 1]:
                value = parse_value(line[2:])
            else:
                # Выбираем внутренний блок (вложенный)
                inner_block = [lines[i].replace('- ', '  ')]
                for j in lines[i + 1:]:
                    if re.match(f"(?:^\s{{{indent_level}}}- )|(?:^\s{{0,{indent_level - 2}}}\w)", j):
                        break
                    inner_block.append(j)
                value = parse_block(inner_block, indent_level + 2)
                if not value:
                    value = parse_value(line[2:])
            value_list.append(value)
        elif ': ' in line:  # Если это словарь
            if value_list:
                return value_list
            key, value = line.split(': ', 1)
            result[key] = parse_value(value)
        elif line.endswith(':'):  # Словарь с вложенностью
            if value_list:
                return value_list
            key = line[:-1].strip()
            inner_block = []
            for j in lines[i + 1:]:
                if re.match(f"^\s{{0,{indent_level}}}\w", j):
                    break
                inner_block.append(j)
            result[key] = parse_block(inner_block, indent_level + 2)

    if value_list:
        return value_list
    else:
        return result


def custom_json_dump(data, indent=4, level=1):
    bypass_python_311 = ',\n'

    def format_value(value, level):
        if isinstance(value, dict):
            return custom_json_dump(value, indent, level + 1)
        elif isinstance(value, list):
            items = [format_value(item, level + 1) for item in value]
            return f"[\n{' ' * (level + 1) * indent + (bypass_python_311 + ' ' * (level + 1) * indent).join(items)}\n{' ' * level * indent}]"
        elif isinstance(value, str):
            return f'"{value}"'
        elif value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    items = []
    for key, value in data.items():
        formatted_value = format_value(value, level)
        items.append(f'{" " * level * indent}"{key}": {formatted_value}')
    return f"{{\n{bypass_python_311.join(items)}\n{' ' * (level - 1) * indent}}}"


def load_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()
    

def save_file(filename: str, data: str) -> None:
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(data)


if __name__ == '__main__':
    save_file('dop_task_3/result.json', custom_json_dump(parse_block(load_file('shedule.yaml').splitlines())))
