numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

num_1 = numbers[:4] # Правая граница (8 включительно)
num_2 = numbers[5:] # Пропуск None в подсчете
amount = len(numbers) # Введение переменной количества символов
sum_num = num_1 + num_2 #Возвращение результа сложения множества
none_1 = round(sum(sum_num) / amount)
numbers[4] = none_1
print("Измененный список:", numbers)
