# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(group1, group2, delimiter="|"):
    # Разделяем строки на списки участников
    participants_set1 = set(group1.split(delimiter))
    participants_set2 = set(group2.split(delimiter))
    # Находим общих участников
    common_participants = participants_set1.intersection(participants_set2)
    # Преобразуем множество в список и сортируем его
    common_participants_list = list(common_participants)
    common_participants_list.sort()
    return common_participants_list
# Проверяем работу функции с заданными группами
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
# Выводим результат
print("Общие участники:", result)