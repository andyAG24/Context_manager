import os
import time
import json
from contextlib import contextmanager

start_time = time.time()

class json_loader:
    def __init__(self, path):
        self.file = open(path, encoding='utf8')
        print('\nВремя запуска кода: {}'.format(time.ctime()))
    def __enter__(self):
        try:
            json_data = json.load(self.file)
        except json.decoder.JSONDecodeError:
            json_data = []
        return json_data
    def __exit__(self, *args):
        self.file.close()
        print('\nВремя окончания работы кода: {}'.format(time.ctime()))
        print('\nВремя выполнения кода: {} секунд(а)\n'.format(time.time() - start_time))

if __name__ == '__main__':
    with json_loader('newsafr.json') as json_data:
        pass
    
    json_list = json_data['rss']['channel']['items']
    list_1 = list()

    i = 0 
    while i < len(json_list):
        list_1.append(json_list[i]['description'])
        i += 1

    str_2 = str(list_1)
    list_3 = list(str_2.split(' '))

    k = 0
    list_4 = list()

    while k < len(list_3): #отбор слов длиной от 6-и символов
        if len(list_3[k]) >= 6:
            list_4.append(list_3[k].replace("'", "").lower())
        k += 1

    list_4.sort()

    k = 1
    words_dict = {}
    while k < len(list_4): #подсчет кол-ва вхождений слов
        words_dict.update({list_4[k]: ''})
        count = 1
        while k < len(list_4):
            if list_4[k - 1] == list_4[k]:
                count += 1
                words_dict.update({list_4[k]: count})
            else:
                count = 1
                words_dict.update({list_4[k]: count})
            k += 1

    smth = list(words_dict.items())
    smth_1 = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))

    i = 0
    while i <= 9:
        print('На {} месте - слово \'{}\', оно встречается {} раз(а)'.format(i+1, smth_1[i][0], smth_1[i][1]))
        i += 1
        
