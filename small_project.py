

from pywebio.input import *
from pywebio.output import *





def verify(username,password):
    return username=='user' and password == '1234'

def login():
    data = input_group("Login",[
        input('Username', name='username', type=TEXT),
        input('Password', name='password', type=PASSWORD),
        actions('actions', [
            {'label': 'Login', 'type': 'submit','value': 'login'},
            {'label': 'Register', 'value': 'register'},
            {'label': 'Reset', 'type': 'reset'}
            ], name='action')
        ])
    username = data['username']
    password = data['password']
    if verify(username,password):
        return True
    else:
        with use_scope('msglabel', clear=True):
            put_text('Please enter a valid credential!')
        return login()
    
def user_info():
    data = input_group("User Info",[
        input('Name', name='name', type=TEXT),
        input('Surname', name='surname', type=TEXT),
        input('Date of Birth', name='birthday', type=DATE)
        ])  
    return data 
    
def user_address():
    country2city = {
        'Türkiye': ['Osmaniye', 'İstanbul', 'Ankara'],
        'USA': ['New York', 'Los Angeles', 'San Francisco'],
    }
    countries = list(country2city.keys())
    data = input_group("Select a location", [
        select('Country', options=countries, name='country',
            onchange=lambda c: input_update('city', options=country2city[c])),
        select('City', options=country2city[countries[0]], name='city'),
    ])
    return data 
    
def select_service():
    data = input_group("Select Service",[
        radio('Services',['Clean','Repair','Modify','Other'],name='service')
        ])  
    return data['service']
    
def get_invoice(info_data,address_data,service_data):
    put_table([
        ['User Info:',info_data],
        ['User Address:',address_data],
        ['Service Selection',service_data]
    ])

    
def main_menu():
    with use_scope('menu_scope', clear=True):
        responce = actions('Select Module', ['info', 'adress','service','invoice','close'])
    return responce


def index():
    response = main_menu()
    while response!='close':
        if response=='info':
            info_data= user_info()
        elif response=='adress':
            address_data= user_address()
        elif response== 'service':
            service_data =select_service()
        elif response== 'invoice':
            get_invoice(info_data,address_data,service_data)
            break
        response=main_menu()
            

def main():
    if login():
        clear('msglabel')
        index()
    else:
        put_text('Err')

main()
