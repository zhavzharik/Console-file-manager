# функция ведения персонального счета (пополнение, списание, учет покупок, информация о балансе счета)

from functions import read_number, read_list


def my_personal_account():
    personal_account = read_number('sum_account.json')  # читаем информацию о балансе счета
    total_sum_buy = read_number('total_buy.json')       # читаем информацию об общей сумме покупок
    sum_history = read_list('sum_history.json')         # читаем список сумм покупок
    name_history = read_list('name_history.json')       # читаем список названий покупок

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. баланс счета')
        print('5. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            refill = float(input('Введите сумму для пополнения счета: '))
            personal_account += refill

        elif choice == '2':
            sum_buy = float(input('Введите сумму покупки: '))
            if sum_buy > personal_account:
                print('Денег на счете недостаточно!')

            else:
                name_buy = input('Введите название покупки: ')
                personal_account -= sum_buy
                total_sum_buy += sum_buy
                sum_history.append(sum_buy)
                name_history.append(name_buy)

        elif choice == '3':
            if len(sum_history) == 0:
                print('Покупок не было!')
            else:
                print('*' * 39)
                print('История покупок:')
                for i in range(len(name_history)):
                    print(f" {name_history[i]} {'_' * (25 - len(name_history[i]))} {sum_history[i]} руб.")
                print(f" ИТОГО {'_' * (25 - len(str(total_sum_buy)))} {total_sum_buy} руб.")
                print('*' * 39)

        elif choice == '4':
            print(f'Баланс счета: {personal_account} руб.')

        elif choice == '5':
            with open('sum_account.json', 'w') as f:
                f.write(f'{personal_account}')
            with open('sum_history.json', 'w') as f:
                for item in sum_history:
                    f.write(f'{item}\n')
            with open('name_history.json', 'w') as f:
                for item in name_history:
                    f.write(f'{item}\n')
            with open('total_buy.json', 'w') as f:
                f.write(f'{total_sum_buy}')
            break

        else:
            print('Неверный пункт меню')