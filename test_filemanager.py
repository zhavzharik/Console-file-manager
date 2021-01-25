import os
import sys
from functions import create_dir, display_program_creator, view_sys_info


def test_create_dir():
    folder = 'for_test'
    assert create_dir(folder) == "Создана папка for_test!"
    os.rmdir(folder)


def test_display_program_creator():
    assert display_program_creator() == 'Создатель программы - Светлана Ж.'


def test_view_sys_info():
    assert view_sys_info() == f'Операционная система: {os.name}, {sys.platform}'