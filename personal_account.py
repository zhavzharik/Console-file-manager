# функция ведения персонального счета (пополнение, списание, учет покупок, информация о балансе счета)


def my_personal_account():
    personal_account = 0  # переменная для учета средств на личном счете пользователя
    sum_history = []  # здесь будет храниться история суммы покупок
    name_history = []  # здесь будет храниться история названий покупок
    total_sum_buy = 0 # переменная для учета суммы всех покупок
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
            break

        else:
            print('Неверный пункт меню')