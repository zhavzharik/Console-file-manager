# функции для главного меню консольного файлового менеджера
import os
import shutil
import sys

this_path = os.getcwd()

# функция создания папки


def create_folder():
    folder = input('Введите название папки, которую нужно создать: ')
    full_path = os.path.join(this_path, folder)
    if not os.path.exists(full_path):
        os.mkdir(folder)
        print(f'Создана папка {folder}!')
    else:
        print(f'Папка {folder} уже существует!')


# функция удаления папки или файла


def delete_folder_file():
    folder = input('Введите название папки/файла, которую(ый) нужно удалить: ')
    full_path = os.path.join(this_path, folder)
    if not os.path.exists(full_path):
        print('Такой(го) папки/файла не существует!')
    elif os.path.isdir(full_path):
        os.rmdir(full_path)
        print(f'Папка {folder} удалена!')
    else:
        os.remove(full_path)
        print(f'Файл {folder} удален!')

# функция копирования папки или файла


def copy_folder_file():
    folder = input('Введите название папки/файла, которую(ый) нужно скопировать: ')
    full_path = os.path.join(this_path, folder)
    if not os.path.exists(full_path):
        print('Такой(го) папки/файла не существует!')
    elif os.path.isdir(full_path):
        new_folder = input('Введите название для копии папки: ')
        new_full_path = os.path.join(this_path, new_folder)
        shutil.copytree(full_path, new_full_path)
        print(f'Папка {folder} скопирована в папку {new_folder}!')
    else:
        new_folder = input('Введите название для копии файла: ')
        new_full_path = os.path.join(this_path, new_folder)
        shutil.copyfile(full_path, new_full_path)
        print(f'Файл {folder} скопирован в файл {new_folder}!')


# функция просмотра содержимого рабочей директории


def view_this_dir():
    print('Содержимое рабочей директории: ')
    print(os.listdir())


# функция просмотра только папок


def view_only_folders():
    content_list = list(os.listdir())
    folders = []
    for folder in content_list:
        if os.path.isdir(folder):
            folders.append(folder)
    print('Папки в рабочей директории:')
    print(folders)


# функция просмотра только файлов

def view_only_files():
    content_list = list(os.listdir())
    files = []
    for file in content_list:
        if os.path.isfile(file):
            files.append(file)
    print('Файлы в рабочей директории:')
    print(files)


# функция просмотра информации об операционной системе


def view_sys_info():
    print(f'Операционная система: {os.name}, {sys.platform}')


# функция вывода создателя программы


def display_program_creator():
    print('Создатель программы - Светлана Ж.')


# функция смены рабочей директории

def change_dir():
    new_path = input('Введите полный путь, куда следует перейти: ')
    try:
        os.chdir(new_path)
        print(f'Вы перешли в директорию: {new_path}')
        view_this_dir()
    except OSError:
        print(f'Директории: {new_path} не существует!')

# функция возврата в директорию проекта "Консольный файловый менеджер"


def return_project_dir():
    if os.getcwd() == os.path.join('D:' + os.sep, 'Python', 'Projects', 'Консольный файловый менеджер'):
        print('Вы уже находитесь в директории "Консольного файлового менеджера" ')
    else:
        new_path = os.path.join('D:' + os.sep, 'Python', 'Projects', 'Консольный файловый менеджер')
        os.chdir(new_path)
        print('Вы перешли в директорию проекта "Консольный менеджер" ')
        view_this_dir()