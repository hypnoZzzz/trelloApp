import sys
import requests

auth_params = {
    'key': '3834098155ea3749d3ea796c75171ea3',
    'token': '9697200f110adea0bf2e0a50ddc3193a494cfb4f091c5a21528ee68fceb12008',
}

base_url = "https://api.trello.com/1/{}"
board_id = 'yybrPe0r'

def create_new_task():
    '''Создает задачу с произвольным названием в одной из колонок'''

    task_name=input('Задайте новую задачу: ')
    column_name=input('В какую колонку поместить эту задачу? ')

    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    for column in column_data:
        if column['name'] != column_name:
            continue
        else:
            column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards',
                                        params=auth_params).json()
            if column_tasks == []:
                requests.post(base_url.format('cards'),
                              data={'name': task_name, 'idList': column['id'], **auth_params})
            for task in column_tasks:
                task['id'] = id
                payload = {'name': task_name, 'idList': column['id'], 'id': id,
                           **auth_params}
                
                if task['name']!= task_name:
                    requests.post(base_url.format('cards'),
                                  data=payload)
                elif task['name'] == task_name:
                    choice = input('Такая задача есть в списке! Всё равно добавить? (y/n)')
                    if choice == 'n':
                        return create_new_task()
                    elif choice == 'y':
                        pay = {'name': task_name, 'idList': column['id'], 'id': id,
                               **auth_params}
                        requests.post(base_url.format('cards'),
                                      data=pay)
                        break
                    else:
                        print('Вводите "y" или "n"!')
                        return create_new_task()
