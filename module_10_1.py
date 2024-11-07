import time
from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Какое-то слово №  {i+1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

stop_time = time.time()

res_time = stop_time - start_time
print(f'Время работы функций {res_time}')

start_time2 = time.time()

thr_first = Thread(target=write_words, args= (10, 'example5.txt'))
thr_second = Thread(target=write_words, args= (30, 'example6.txt'))
thr_third = Thread(target=write_words, args= (200, 'example7.txt'))
thr_fourh = Thread(target=write_words, args= (100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourh.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourh.join()

stop_time2 = time.time()
res_time2 = stop_time2 - start_time2
print(f'Время работы потоков {res_time2}')
print(f'Использование Потоков быстрее функций на {res_time-res_time2} секунд')