import json
import os
from store.models import DATABASE as db
from django.contrib.auth import get_user



def viewInCart(rqst) -> dict:

    """
    Просматривает содержимое cart.json

    :return: Содержимое 'cart.json'
    """
    if os.path.exists('cart.json'):  # Если файл существует
        with open('cart.json', encoding='utf-8') as f:
            return json.load(f)
    user = get_user(rqst).username
    cart = {user:{'products': {}}}  # Создаём пустую корзину
    with open('cart.json', mode='x', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(cart, f)

    return cart

def viewInWish(rqst) -> dict:
   
    if os.path.exists('wishlist.json'):  # Если файл существует
        with open('wishlist.json', encoding='utf-8') as f:
            return json.load(f)
    user = get_user(rqst).username
    wishlist = {user:{'products': []}}  # Создаём пустую корзину
    with open('wishlist.json', mode='x', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(wishlist, f)

    return wishlist

def addToCart(rqst,id_product: str, db: str=db) -> bool:
    cart_users = viewInCart(rqst)
    cart = cart_users[get_user(rqst).username]
    if db.get(id_product):
        if cart['products'].get(id_product):
            cart['products'][id_product]+=1
        else:
            cart['products'][id_product]=1
    else:
        return False
    
    with open('cart.json', mode='w', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(cart_users, f)
            
    return True


def addToWish(rqst,id_product: str, db: str=db) -> bool:
    wish_users = viewInWish(rqst)
    wishlist = wish_users[get_user(rqst).username]
    if db.get(id_product):
        if wishlist['products'].get(id_product):
            wishlist['products'].append(id_product)
    else:
        return False
    
    with open('wishlist.json', mode='w', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(wish_users, f)
            
    return True



def removeFromCart(rqst,id_product: str) -> bool:
    cart_users = viewInCart(rqst)
    cart = cart_users[get_user(rqst).username] # TODO Помните, что у вас есть уже реализация просмотра корзины,
    if cart["products"].get(id_product):
       cart['products'].pop(id_product) 
    else:
        return False

    with open('cart.json', mode='w', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(cart_users, f)
    return True

def removeFromWish(rqst,id_product: str) -> bool:
    wish_users = viewInWish(rqst)
    wishlist = wish_users[get_user(rqst).username] # TODO Помните, что у вас есть уже реализация просмотра корзины,
    if wishlist["products"].get(id_product):
       wishlist['products'].pop(id_product) 
    else:
        return False

    with open('wishlist.json', mode='w', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(wish_users, f)
    return True


def addUserToCart(rqst,username: str)->None:
    cart_users = viewInCart(rqst)  # Чтение всей базы корзин

    cart = cart_users.get(username)  # Получение корзины конкретного пользователя

    if not cart:  # Если пользователя до настоящего момента не было в корзине, то создаём его и записываем в базу
        with open('cart.json', mode='w', encoding='utf-8') as f:
            cart_users[username] = {'products': {}}
            json.dump(cart_users, f)    

def addUserToWish(rqst,username: str)->None:
    wish_users = viewInWish(rqst)  # Чтение всей базы корзин

    wishlist = wish_users.get(username)  # Получение корзины конкретного пользователя

    if not wishlist:  # Если пользователя до настоящего момента не было в корзине, то создаём его и записываем в базу
        with open('cart.json', mode='w', encoding='utf-8') as f:
            wish_users[username] = {'products': []}
            json.dump(wish_users, f)    


def filtering_category(database: dict,
                       category_key: [int, str],
                       ordering_key: [None, str] = None,
                       rvrs: bool = False):
    """
    Функция фильтрации данных по параметрам

    :param database: База данных.
    :param category_key: [Опционально] Ключ для группировки категории. Если нет ключа, то рассматриваются все товары.
    :param ordering_key: [Опционально] Ключ по которому будет произведена сортировка результата.
    :param reverse: [Опционально] Выбор направления сортировки:
        False - сортировка по возрастанию;
        True - сортировка по убыванию.
    :return: list[dict] список товаров с их характеристиками, попавших под условия фильтрации. Если нет таких элементов,
    то возвращается пустой список
    """
    if category_key is not None:
        result = [product for product in database.values() if product['category']==category_key]  
        #  TODO При помощи фильтрации в list comprehension профильтруйте товары по категории. Или можете использовать
        # обычный цикл или функцию filter
    else:
        result = [product for product in database.values()]
        #  TODO Трансформируйте database в список словарей
    if ordering_key is not None:
        result.sort(key = lambda x: x[ordering_key], reverse=rvrs)
        #  TODO Проведите сортировку result по ordering_key и параметру reverse
    return result


if __name__ == "__main__":
    # Проверка работоспособности функций view_in_cart, add_to_cart, remove_from_cart
    # Для совпадения выходных значений перед запуском скрипта удаляйте появляющийся файл 'cart.json' в папке
    print(viewInCart())  # {'products': {}}
    print(addToCart('1'))  # True
    print(addToCart('0'))  # False
    print(addToCart('1'))  # True
    print(addToCart('2'))  # True
    print(viewInCart())  # {'products': {'1': 2, '2': 1}}
    print(removeFromCart('0'))  # False
    print(removeFromCart('1'))  # True
    print(viewInCart())  # {'products': {'2': 1}}



# if __name__ == "__main__":
#     from store.models import DATABASE as db

#     test = [
#         {'name': 'Клубника', 'discount': None, 'price_before': 500.0, 'price_after': 500.0,
#          'description': 'Сладкая и ароматная клубника, полная витаминов, чтобы сделать ваш день ярче.',
#          'category': 'Фрукты', 'id': 2, 'url': 'store/images/product-2.jpg', 'html': 'strawberry'
#          },

#         {'name': 'Яблоки', 'discount': None, 'price_before': 130.0, 'price_after': 130.0,
#          'description': 'Сочные и сладкие яблоки - идеальная закуска для здорового перекуса.',
#          'category': 'Фрукты', 'id': 10, 'url': 'store/images/product-10.jpg', 'html': 'apple'
#          }
#     ]
#     print(filtering_category(db, 'Фрукты', 'price_after', True))
#     #print(filtering_category(db, 'Фрукты', 'price_after', True) == test)  # True