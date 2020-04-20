import requests
from collections import Counter


auth_params = {
    'key': '3834098155ea3749d3ea796c75171ea3',
    'token': '9697200f110adea0bf2e0a50ddc3193a494cfb4f091c5a21528ee68fceb12008',
}

base_url = "https://api.trello.com/1/{}"
board_id = 'yybrPe0r'

global task_list, user_enter_list

def check_for_emptiness():
    '''Проверяет доску на пустоту, заполняет список задач'''
    task_list=[]
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                               params=auth_params).json()
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards',
                                    params=auth_params).json()
        if column_tasks == []:
            break
        elif column_tasks != []:
            for task in column_tasks:
                state = None
                task_list += ([{'name': task['name'], 'id': task['id'][-4: 24], 'state': state}])

def bloodhound():
    '''Ищет нужную колонку, задачу, получает id задачи, проверяет задачу на дубли'''
    global user_choice, column_tasks, column_name, carryover_elem
    user_enter_list = []
    carryover=[]
    task_id = None
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                               params=auth_params).json()
    task_name = input('Введите название перемещаемой задачи: ')
    col_name = input('Введите колонку, в которой расположена задача: ')

    for column in column_data:
        if col_name == column['name']:
            column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards',
                                        params=auth_params).json()
            for task in column_tasks:
                if task['name'] == task_name:
                    task_id = task['id']
                    user_enter_list+=([{'name': task['name'], 'id': task_id}])
    if len(user_enter_list)==1:
        user_choice= print('Эта задача уникальна!')
        column_name = input('В какую колонку переместить задачу? ')
        column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                                   params=auth_params).json()
        for column in column_data:
            if column['name'] == column_name:
                requests.put(base_url.format('cards') + '/' + task_id + '/idList',
                             data={'value': column['id'], **auth_params})
                break


    elif len(user_enter_list)>1:
        print("Найдены одинаковые задачи!")
        print(user_enter_list)
        user_choice = input('Введите id нужной Вам задачи: ')
        column_name=input('В какую колонку перенести задачу?')

    for elem in user_enter_list:
        elem_user_list = elem
        if user_choice == elem_user_list['id']:
            carryover+=([elem_user_list])

    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                               params=auth_params).json()

    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards',
                                    params=auth_params).json()
        for elem in carryover:
            carryover_elem = elem
        for task in column_tasks:
            if task['id'] == carryover_elem['id']:
                task_id = task['id']
                break
            if task_id:
                break

    for column in column_data:
        if column['name'] == column_name:
            requests.put(base_url.format('cards') + '/' + task_id + '/idList',
                         data={'value': column['id'], **auth_params})
            break
