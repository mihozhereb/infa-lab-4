import time

import main_task.main
import dop_task_1.dop1
import dop_task_2.dop2
import dop_task_3.dop3


if __name__ == '__main__':
    print('Время выполнения основного задания:')
    start = time.time()
    for _ in range(100):
        main_task.main.save_file('main_task/result.json', main_task.main.yaml_to_json(main_task.main.load_file('shedule.yaml')))
    finish = time.time() - start
    print(finish)

    print('Время выполнения дополнительного задания 1:')
    start = time.time()
    for _ in range(100):
        dop_task_1.dop1.parse('shedule.yaml', 'dop_task_1/result.json')
    finish = time.time() - start
    print(finish)

    print('Время выполнения дополнительного задания 2:')
    start = time.time()
    for _ in range(100):
        dop_task_2.dop2.save_file('dop_task_2/result.json', dop_task_2.dop2.yaml_to_json(dop_task_2.dop2.load_file('shedule.yaml')))
    finish = time.time() - start
    print(finish)

    print('Время выполнения дополнительного задания 3:')
    start = time.time()
    for _ in range(100):
        dop_task_3.dop3.save_file('dop_task_3/result.json', dop_task_3.dop3.custom_json_dump(dop_task_3.dop3.parse_block(dop_task_3.dop3.load_file('shedule.yaml').splitlines())))
    finish = time.time() - start
    print(finish)