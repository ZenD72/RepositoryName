data = 1.44
page = 100
str_coun = 50
str_symb = 25
symb_1 = 4
mb_byte = 1024 ** 2 #Перевод МБайт в Байты
book_size = page * str_coun * str_symb * symb_1 #Размер книги
data_byte = data * mb_byte #Перевод значения в Байты
count = book_size // data_byte #Целочисленное деление
print("Количество книг, помещающихся на дискету:", int(count))
