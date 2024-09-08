import csv

res = ''
krit = False
name_file = input('[!] Наименование файла\n'
            'Ввод: ')

for temp_start in range (True):
    try:
        user_conf = int(input('[0] Завершение работы\n'
                              '[1] Проверить все носители на всех устройствах\n'
                              '[2] Проверить носители с указанием серийного номера\n'
                              '[3] Проверить носители с указанием модели\n'
                              '[4] Список уязвимых носителей\n'
                              '[5] Последняя дата проверки носителей\n'
                              'Ввод: '))

        if (user_conf == 1 or user_conf == 2 or user_conf == 5):
            break
        elif (user_conf == 3 or user_conf == 4):
            break
        elif (user_conf == 0):
            exit()
        else:
            pass
    except:
        pass

def main ():
    global vg, sl, res, krit
    vg = ((int(row['capacity_bytes']) / 1024) / 1024) / 1024
    try:
        sg = int(row['smart_1_normalized'])
    except:
        for temp_ht in range(255, 0, -1):
            try:
                if (int(row['smart_' + str(temp_ht) + '_normalized']) > 0):
                    sg = int(row['smart_' + str(temp_ht) + '_normalized'])
                    break

                elif (int(row['smart_' + str(temp_ht) + '_raw']) > 0):
                    sg = int(row['smart_' + str(temp_ht) + '_raw'])
                    break
            except:
                pass
    try:
        sl = round((((vg * 2) - (sg * 10)) / 24) / 365, 1)
        sla = int(sl // 1.2)
        slm = int((sl - float(sla * 1.2)) * 10)
    except:
        pass
    if (krit == True):
        try:
            if (sla == 0 and slm <= 3):
                res += ('\nСерийный номер: ' + row['serial_number'] + '\nМодель: ' + row['model'] + '\nСрок службы: ' + '\033[31m{}'.format(str(sla) + '/' + str(slm) + ' (год/месяц)') + '\033[0m\n\n')
            else:
                pass
        except:
            pass
        krit = False
    elif (krit == False):
        if (sla == 0 and slm <= 6):
            res += ('\nСерийный номер: ' + row['serial_number'] + '\nМодель: ' + row['model'] + '\nСрок службы: ' + '\033[33m{}'.format(str(sla) + '/' + str(slm) + ' (год/месяц)') + '\033[0m\n\n')
        else:
            res += ('\nСерийный номер: ' + row['serial_number'] + '\nМодель: ' + row['model'] + '\nСрок службы: ' + str(sla) + '/' + str(slm) + ' (год/месяц) \n\n')
    else:
        pass

with open(name_file + '.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    to = 0 #все сектора smart сумировать
    tp = 0 #все суммированные smart_raw
    ht = 0 #последняя забитая клетка smart заполненная

    if (user_conf == 1):
        for row in csv_reader:
            main()

    elif (user_conf == 2):
        for temp_start in range(True):
            try:
                user_conf = input('[0] Завершение работы\n'
                                  '[!] Серийный номер\n'
                                  'Ввод: ')

                if (user_conf != 0):
                    break
                elif (user_conf == 0):
                    exit()
                else:
                    pass
            except:
                pass
        for row in csv_reader:
            if (row['serial_number'] == user_conf):
                main()
            else:
                pass

    elif (user_conf == 3):
        for temp_start in range(True):
            try:
                user_conf = input('[0] Завершение работы\n'
                                  '[!] Модель\n'
                                  'Ввод: ')

                if (user_conf != 0):
                    break
                elif (user_conf == 0):
                    exit()
                else:
                    pass
            except:
                pass

        for row in csv_reader:
            if (row['model'] == user_conf):
                main()
            else:
                pass

    elif (user_conf == 4):
        for row in csv_reader:
            krit = True
            main()

    elif (user_conf == 5):
        for row in csv_reader:
            print('Последняя дата проверки носителей: ' + row['date'])
            break
    else:
        pass

if (res != ''):
    for temp_stop in range (True):
        try:
            user_form = int(input('[0] Завершение работы\n'
                        '[1] Вывести результат в консоль\n'
                        'Ввод: '))

            if (user_form == 1):
                print(res)
                break
            elif (user_form == 0):
                exit()
            else:
                pass
        except:
            pass
else:
    pass