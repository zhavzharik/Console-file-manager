import os
import sys
from functions import create_dir, display_program_creator, view_sys_info, read_number, read_list
from victory import gen_name_question


def test_create_dir():
    folder = 'for_test'
    assert create_dir(folder) == "Создана папка for_test!"
    os.rmdir(folder)


def test_display_program_creator():
    assert display_program_creator() == 'Создатель программы - Светлана Ж.'


def test_view_sys_info():
    assert view_sys_info() == f'Операционная система: {os.name}, {sys.platform}'


def test_read_number():
    number = 20000
    with open('test_number.json', 'w') as f:
        f.write(f'{number}')
    assert read_number('test_number.json') == 20000


def test_read_list():
    data = ['food', 'house']
    with open('test_list.json', 'w') as f:
        for item in data:
            f.write(f'{item}\n')
    assert read_list('test_list.json') == ['food', 'house']


def test_gen_name_question():
    assert len(gen_name_question()) == 5