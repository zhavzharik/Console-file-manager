from functions import *
from victory import play_victory
from personal_account import my_personal_account


while True:
    print('=' * 25)
    print('Меню:')
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. вернуться в директорию проекта "Консольного менеджера" ')
    print('13. сохранить содержимое рабочей директории в файл')
    print('14. выход')
    print('=' * 25)

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        print(create_folder())

    elif choice == '2':
        delete_folder_file()

    elif choice == '3':
        copy_folder_file()

    elif choice == '4':
        print(f'Файлы в рабочей директории: {get_only_files()}\nПапки в рабочей директории: {get_only_folders()}')

    elif choice == '5':
        print(f'Папки в рабочей директории: {get_only_folders()}')

    elif choice == '6':
        print(f'Файлы в рабочей директории: {get_only_files()}')

    elif choice == '7':
        print(view_sys_info())

    elif choice == '8':
        print(display_program_creator())

    elif choice == '9':
        play_victory()

    elif choice == '10':
        my_personal_account()

    elif choice == '11':
        change_dir()

    elif choice == '12':
        return_project_dir()

    elif choice == '13':
        dir_in_files()
        print('Содержимое рабочей директории сохранено в файл listdir.txt')

    elif choice == '14':
        break

    else:
        print('Неверный пункт меню')