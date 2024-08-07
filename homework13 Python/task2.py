def plus_two(number):
    return(f"Result: {number + 2}")

try:
    number = input("Enter a number: ")
    print(plus_two(number))
except:
    print("Ожидаемый тип данных — число!")

'''
Я хотел сделать через TypeError, однако оно совсем тут не подходит.
Если я задам ожидаемый тип данных как int/float, то программа выдаст ошибку независимо от того что я введу
(даже если корректно число), так как input() всегда возвращает str.
Если я задам ожидаемый тип данных как int/float и сделаю float(input()), то программа выдаст ошибку ValueError,
так как попытка преобразования строки в число начинается раньше и просто TypeError не сработает.
Конечно есть вариант вводить прямо в код данные вручную, не через консоль. Однако это слишком просто.
В итоге я решил сделать через просто except без уточнения ошибки. Я честно не вижу способа стриггерить TypeError. 
'''