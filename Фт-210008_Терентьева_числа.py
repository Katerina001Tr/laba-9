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
cc2 = 0  
while cc2 != 1:  
    try:
        k = int(input('Введите количество попыток: '))
        logging.info('Вводят число попыток')
        while k <= 0:  
            print("Число попыток не может быть 0 или отрицательным числом!")
            logging.warning('Ввели число, меньшее единицы')
            k = int(input('Введите число попыток отгадать число: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
        logging.error('Ввели не число!')
    else:
        cc2 += 1
        logging.info('Ввели корректное число попыток({})'.format(k))        
i = 1  
while i != k + 1:  
    print(i, 'попытка')
    logging.info('Попытка отгадать число №({})'.format(i))
    cc3 = 0  
    while cc3 != 1:  
        try:
            answer = int(input('Какое число загадал компьютер? '))
            logging.info('Вводят предполагаемое число, которое загадал компьютер')
        except ValueError:
            print('Вы ввели не число!\nПробуйте снова\n')
            logging.error('Ввели не число!')
        else:
            cc3 += 1
            logging.info('Ввели корректное предполагаемое число, которое загадал компьютер({})'.format(answer))
        
