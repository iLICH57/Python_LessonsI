# *** Коллекции (контейнеры) ***

# ** Список (list)

# Создание пустого списка
# my_list = []
# my_list = list()

# PEP8

# добавление объекта (элемента) в Список
# my_list.append(100)
# my_list.append(3.14)
# my_list.append("hello")
# my_list.append([10, 20, 30])

# print(my_list)

# Чтение значений элемента
# прямая индексация
# в квадратную скобочку указываем индекс
# el = my_list[3]
# el = my_list[3][1]

# обратная индексация
# el = my_list[-1]

# Замена значения элемента
# my_list[0] = 2000

#  Удаление элемента по значению
# my_list.remove(3.14)

# Удаление элемента по индексу
# del my_list[-1] 


#  Срез списка
# s = "Hello world!"
# my_list = list(s)

# my_slice = my_list[2:]
# my_slice = my_list[2:5]

# print(my_list)
# print(my_slice)





# с шагом 2








# len() возвращает длину (кол-во элементов) коллекции
# print(len(my_list))
# print(my_list)
# print(my_slict)


# *** Кортеж (tuple) ***

#  Неизменяемая (immutable) коллекция
# легковестнее, чем список

# создание кортежа
# my_tuple = (10, 20, 30, 40, 50)

# my_tuple[0] = 100

# print(my_tuple)

# чтение значений элементов
# print(my_tuple[0])

# срез
# print(my_tuple[2:])


#  *** Словарь (dict) ***

# изменяемый, упорядоченный тип коллекции

# пара "ключ-значение"
# {ключ_1:значение_1, ключ_2:значение_2}

#  создание словаря
my_dict = {10:3.14, "abc":[1,2,3]} 

# print(my_dict)

# # чтение значений
# print(my_dict[10]
# print(my_dict["abc"])

data0 = {"name":"ILYA", "age":42, "id":123.5}
data1 = {"name":"Vasya", "age":9, "id":12.5}
data2 = {"name":"Lena", "age":29, "id":3.0}

total_data = {"p0":data0, "p1":data1, "p2":data2}

# print(total_data["p2"]["age"])

# изменение значений
my_dict["abc"] = "hello"

# при присвоении нового значения по несуществующему ключу
# создается новая пара
my_dict['A'] = 777


# удаление пары (элемента)
del my_dict[10]

# обновление данных

data0 = {"name":"ILYA", "age":42, "id":123.5}

data0.update({"age":43, "id":300})

print(data0)