import random
import logging
cc1 = 0 
while cc1 != 1:  
    try:
        n = int(input('Компьютер загадал число: '))
        logging.info('Ввод числа, которое загадал компьютер')
        while n <= 0:  
            print("Введите положительное число!")
            logging.warning('Ввели число, меньшее единицы')
            n = int(input('Введите положительное число, которое загадывает компьютер: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
        logging.error('Ввели не число!')
    else:
        cc1 += 1
        logging.info('Ввели корректное число({})'.format(n))
