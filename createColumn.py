import requests

auth_params = {
    'key': '3834098155ea3749d3ea796c75171ea3',
    'token': '9697200f110adea0bf2e0a50ddc3193a494cfb4f091c5a21528ee68fceb12008',
}

base_url = "https://api.trello.com/1/{}"
board_id = 'yybrPe0r'

def create_new_column():
    name_new_column = input ('Введите название новой колонки: ')
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists',
                               params=auth_params).json()
    col_number=1
    for column in column_data:
        col_number += 1
        column['id']=id
        column['number']=col_number
        if column['name']==name_new_column:
            print('Колонка с таким названием есть! ')
            return create_new_column()

    payload = {'name': name_new_column, 'id': id, 'number': col_number}
    requests.post(base_url.format('boards') + '/' + board_id + '/lists',
                                 params=auth_params, data = payload).json()
    print("Номер созданной колонки: ", column['number'])

