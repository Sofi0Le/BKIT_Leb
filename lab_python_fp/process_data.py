import json
import sys
# Сделаем другие необходимые импорты
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1


path = r'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='UTF-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case = True), key = lambda let: let.lower())

@print_result
def f2(arg):
    return list(filter(lambda prog: (prog.lower()).startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda prog_py: prog_py + ' с опытом Python', arg))


@print_result
def f4(arg):
    return ['{}, зарплата {} руб.'.format(job, money) for job, money in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
