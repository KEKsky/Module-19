from api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()


def test_get_api_key_for_invalid_username(email='sobaka@sobaka.sobaka', password=valid_password):
    '''Негативный сценарий
    Вводим неверный адрес почты и пытамеся получить ключ'''
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_password(email=valid_email, password='1111'):
    '''Негативный сценарий
    Вводим неверный пароль и пытаемся получить ключ'''
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_invalid_key(filter=''):
    '''Негативный сценарий
    Вводим несуществующий ключ и пытаемся получить список питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = 'abc123'
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert 'pets' not in result


def test_get_all_pets_with_invalid_filter(filter='free'):
    '''Негативный сценарий
    Вводим несуществующий фильтр и пытаемся получить список питомцев'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert 'pets' not in result



def test_post_new_pet_simple_with_invalid_data(name='', animal_type='', age=''):
    '''Негативный сценарий
    Поля не должны принимать пустые значения'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_simple(auth_key, name, animal_type, age)
    assert status != 200
    assert result['name'] != ''
    assert result['animal_type'] != ''
    assert result['age'] != ''


def test_post_new_pet_simple_with_invalid_age(name='', animal_type='', age='abcde'):
    '''Негативный сценарий
    Поле возраст не должно принимать буквенные значения'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_simple(auth_key, name, animal_type, age)
    assert status != 200
    assert result['age'] != ''


def test_post_new_pet_simple_with_invalid_animal_type(name='', animal_type='12345', age=''):
    '''Негативный сценарий
    Поле порода не должно принимать числовые значения'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_simple(auth_key, name, animal_type, age)
    assert status != 200
    assert result['animal_type'] != animal_type


def test_post_new_pet_simple_with_invalid_name(name='987654321', animal_type='', age=''):
    '''Негативный сценарий
    Поле имя не должно принимать числовые значения'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_simple(auth_key, name, animal_type, age)
    assert status != 200
    assert result['name'] != name


def test_put_pet_new_info_with_invalid_key(name='Китя', animal_type='Кошка', age='6'):
    '''Негативный сценарий
    Вводим несуществующий ключ и пытаемся изменить данные питомца'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key['key'] = 'abc123'
    if len(my_pets['pets']) > 0:
        status, result = pf.put_pet_new_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status != 200
        assert 'name' not in result
    else:
        raise Exception('Ни одного питомца не создано')


def test_delete_my_pet_with_invalid_key():
    '''Негативный сценарий
    Вводим несуществующий ключ и пытаемся удалить питомца'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key['key'] = 'abc123'
    if len(my_pets['pets']) > 0:
        status, result = pf.delete_pet(auth_key, my_pets['pets'][0]['id'])
        assert status != 200
    else:
        raise Exception('Ни одного питомца не создано')
