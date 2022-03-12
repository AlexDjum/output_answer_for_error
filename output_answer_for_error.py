errors = {
    'out': 'Вы вышли из системы',
    'noaccess': 'У вас нет доступа в этот раздел',
    'unknown': 'Неизвестная ошибка',
    'timeout': 'Система долго не отвечает',
    'robot': 'Ваши действия похожи на робота',
}

# Список ошибок
input_errors = []
# Список решений по ошибкам
answer_for_errors = []


def get_errors():
    '''
    Вывод списка ошибок
    '''
    input_errors = input('Input errors').split(', ')

    for error in input_errors:
        if error in errors:
            answer = errors.get(error)
            answer_for_errors.append(answer)
            continue
        else:
            break
    print('; '.join(answer_for_errors))


get_errors()
