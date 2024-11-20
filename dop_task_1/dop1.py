import yaml
import json


def parse(filename_in: str, filename_out: str) -> None:
    with open(filename_in, 'r', encoding='utf8') as yaml_in, open(filename_out, 'w', encoding='utf8') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parse('shedule.yaml', 'dop_task_1/result.json')
