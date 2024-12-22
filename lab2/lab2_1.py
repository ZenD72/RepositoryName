# TODO Напишите функцию для поиска индекса товара
def index(item_list, item): # определяем функцию index
    if item in items_list:
        return items_list.index(item) # проверяем содержится ли внутри функции аргумент item
    else:
        return None # если товар не найден, возвращаем None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # создаем список
for find_item in ['банан', 'груша', 'персик']: # перебираем элементы списка
    index_item = index(items_list, find_item)
    # проверяем найден ли товар:
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
