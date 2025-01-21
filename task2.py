# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(str1_, str2_, n=","): # Определение функции с тремя параметрами (1-я строка с участниками и 2-я строка)
    list_words = set(str1_.split(n)) # Разбиваем 1-ю строку на участников с разделителем "n"
    list_wordssecond = set(str2_.split(n)) # Разбиваем 2-ю строку на участников с разделителем "n"
    common_list = list_words.intersection(list_wordssecond) # Метод .intersection ищет общие пересечения участников
    common_list = list(common_list) # Преобразование из множества в список
    common_list.sort() # Сортируем список в алфавитном порядке
    return (common_list) # Возвращаем отсортированный список участников
print(find_common_participants(participants_first_group, participants_second_group, n="|"))
