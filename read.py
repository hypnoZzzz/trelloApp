import requests


auth_params = {
    'key': '3834098155ea3749d3ea796c75171ea3',
    'token': '9697200f110adea0bf2e0a50ddc3193a494cfb4f091c5a21528ee68fceb12008',
}

base_url = "https://api.trello.com/1/{}"
board_id = 'yybrPe0r'

def read():
    '''Получим данные всех колонок на доске'''
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                               params=auth_params).json()
    # Теперь выведем название каждой колонки и всех заданий, которые к ней относятся:
    for column in column_data:
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards',
                                 params=auth_params).json()
        count = len(task_data)
        print(column['name'] + ',' + ' всего задач в колонке: ' + str(count))

        if not task_data:
            continue
        for task in task_data:
            print(task['name'], ',', 'id задачи: ', task['id'][-4: 24])
